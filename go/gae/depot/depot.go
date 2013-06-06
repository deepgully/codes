package depot

import (
	"appengine"
	"appengine/blobstore"
	"appengine/urlfetch"
	"encoding/json"
	"text/template"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"orm"
)

var (
	DEBUG                   bool
	ENABLE_ANONYMOUS_UPLOAD bool
	CHECK_SIGN_URL          string
)

func init() {
	http.HandleFunc("/", MainHandler)
	http.HandleFunc("/getuploadurl", GetUploadUrlHandler)
	http.HandleFunc("/notify", UploadDoneHandler)
	http.HandleFunc("/upload", UploadHandler)
	http.HandleFunc("/files", FilesHandler)

	DEBUG = appengine.IsDevAppServer()
	ENABLE_ANONYMOUS_UPLOAD = false
	if DEBUG {
		CHECK_SIGN_URL = `http://localhost/apis/rest/`
	} else {
		CHECK_SIGN_URL = `http://www.magicycles.com/apis/rest/`
	}
}

// helper function for server error
func serveError(c appengine.Context, w http.ResponseWriter, err interface{}) {
	w.WriteHeader(http.StatusInternalServerError)
	w.Header().Set("Content-Type", "text/plain")
	fmt.Fprint(w, "Internal Server Error")
	c.Errorf("%v", err)
}

// main handler for root path
func MainHandler(w http.ResponseWriter, r *http.Request) {
	context := orm.Dict{}
	context["CHECK_SIGN_URL"] = CHECK_SIGN_URL
	context["Host"] = r.Host
	myTemplate := template.Must(template.ParseFiles("templates/test.html"))
	err := myTemplate.Execute(w, context)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

// handler for /getuploadurl jsonp callback
func GetUploadUrlHandler(w http.ResponseWriter, r *http.Request) {
	c := appengine.NewContext(r)

	signature := r.FormValue("signature")
	callback := r.FormValue("callback")

	res := orm.Dict{"status": "error", "message": "", "signature": signature}

	if signature != "" && callback != "" {
		upload_file := NewUploadFile(c)
		if upload_file.IsExist("Signature =", signature) {
			c.Infof("used signature %s", signature)
			res["message"] = "used signature"
			jsonCallback(w, callback, res)
			return
		}

		user := checkSignature(signature, c)
		if user == "" {
			c.Infof("wrong signature %s", signature)
			res["message"] = "wrong signature"
			jsonCallback(w, callback, res)
			return
		}

		upload_file.Data["Signature"] = signature
		upload_file.Data["Active"] = false
		upload_file.Data["User"] = user

		_, err := upload_file.Save()
		if err != nil {
			c.Infof("datastroe save error %v", err)
			res["message"] = "datastroe save error"
			jsonCallback(w, callback, res)
			return
		}

		uploadURL, err := blobstore.UploadURL(c, "/upload", nil)
		if err != nil {
			c.Infof("generate blobstore UploadURL error: %v", err)
			res["message"] = "blobstore error"
			jsonCallback(w, callback, res)
			return
		}

		res["status"] = "ok"
		res["upload_url"] = uploadURL.String()

	} else {
		res["message"] = "wrong signature or callback"
		res["upload_url"] = ""
	}

	jsonCallback(w, callback, res)
}

// helper function to check signature and return user
func checkSignature(sign string, c appengine.Context) string {
	if ENABLE_ANONYMOUS_UPLOAD {
		return "anonymous"
	} else {
		data, err := getJson(CHECK_SIGN_URL, url.Values{"method": {"check_upload_signature"}, "signature": {sign}}, c)
		if err != nil {
			log.Fatal(err)
			return ""
		}

		status := data["status"]
		if status == "ok" {
			if user, ok := data["user"].(string); ok {
				return user
			}
		}
	}
	return ""
}

// helper function to get json data using urlfetch
func getJson(url string, payload url.Values, c appengine.Context) (orm.Dict, error) {
	client := urlfetch.Client(c)
	resp, err := client.PostForm(url, payload)
	defer resp.Body.Close()

	if err != nil {
		return nil, err
	}
	if resp.StatusCode != 200 {
		return nil, fmt.Errorf("wrong http status code %d", resp.StatusCode)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	data := orm.Dict{}
	err = json.Unmarshal(body, &data)
	if err != nil {
		return nil, err
	}

	return data, nil
}

// helper function to return json callback script
func jsonCallback(w http.ResponseWriter, callback string, parameters orm.Dict) {
	jsonStr, err := json.Marshal(parameters)
	if err == nil {
		fmt.Fprintf(w, "%s(%s);", callback, jsonStr)
	} else {
		fmt.Fprintf(w, "%s(%s);", callback, `{"status":"error", "message": "json encode error"}`)
	}
}

// handle blobstore upload
func UploadHandler(w http.ResponseWriter, r *http.Request) {
	c := appengine.NewContext(r)

	blobs, params, err := blobstore.ParseUpload(r)
	if err != nil {
		serveError(c, w, err)
		return
	}

	signature := params["signature"][0]
	notify_url := params["notify_url"][0]
	notify_callback := params["notify_callback"][0]

	var (
		status   string = "error"
		message  string = "server error"
		file_url string = ""
	)

	file := blobs["file"]
	if len(file) == 0 {
		message = "no file uploaded"
	} else {
		blobKey := string(file[0].BlobKey)
		saved_file := UploadFile(NewUploadFile(c).FilterOne("Signature =", signature))
		if saved_file == nil || saved_file.IsActived() {
			c.Infof("wrong signature %s, delete blob file %s", signature, blobKey)

			blobstore.Delete(c, file[0].BlobKey)

			message = "wrong signature"
		} else {
			c.Infof("signature %s OK, save blobkey %s", signature, blobKey)

			saved_file.Data["Signature"] = signature
			saved_file.Data["BlobKey"] = blobKey
			saved_file.Data["Active"] = true
			_, err := saved_file.Save()

			if err == nil {
				status = "ok"
				message = "done"
			} else {
				status = "error"
				message = "error in save file"
			}
			file_url = fmt.Sprintf("//%s/files?blobKey=%s", r.Host, blobKey)
		}
	}

	notify := fmt.Sprintf("%s?callback=%s&status=%s&message=%s&file_url=%s",
		notify_url, notify_callback, status, message, file_url)

	http.Redirect(w, r, notify, http.StatusFound)
}

// handle upload done, for cross domain, implement this on your server
func UploadDoneHandler(w http.ResponseWriter, r *http.Request) {
	callback := r.FormValue("callback")
	status := r.FormValue("status")
	message := r.FormValue("message")
	file_url := r.FormValue("file_url")

	fmt.Fprintf(w, `<script>%s({"status":"%s", "message": "%s", "file_url": "%s"})</script>`,
		callback, status, message, file_url)
}

// serve blobstore files
func FilesHandler(w http.ResponseWriter, r *http.Request) {
	blobKey := r.FormValue("blobKey")

	w.Header().Set("Cache-Control", "public, max-age=31536000")

	blobstore.Send(w, appengine.BlobKey(blobKey))

	updateHits(blobKey, appengine.NewContext(r))

}

func updateHits(blobKey string, c appengine.Context) {
	uploadFile := NewUploadFile(c)
	saved_file := uploadFile.FilterOne("BlobKey =", blobKey)
	if saved_file != nil {
		hits, ok := saved_file.Data["Hits"].(int64)
		if !ok {
			hits = int64(0)
		}
		saved_file.Data["Hits"] = hits + 1
		saved_file.Save()
	}
}
