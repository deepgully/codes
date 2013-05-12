orm 
=====

GAE go orm model

usage
=====

define custom model type

    package depot

    import (
        "appengine"
        "orm"
    )

    // define a custom model type
    type uploadFile struct {
        *orm.Model
    }

    // New Upload File Store
    func NewUploadFile(c appengine.Context) *uploadFile {
        file := new(uploadFile)
        file.Model = orm.NewModel(c, "UploadFile")
        file.Data = orm.Dict{
            "Signature": "",
            "BlobKey":   "",
            "Hits":      int64(0),
            "Active":    false,
            "User":      "nobody",
        }
        return file
    }

    // Convert orm.Model to uploadFile struct
    func UploadFile(model *orm.Model) *uploadFile {
        return &uploadFile{model}
    }

    // custom functions
    func (self *uploadFile) IsActived() bool {
        active, ok := self.Data["Active"].(bool)
        if ok {
            return active
        }
        panic("Wrong Data")
    }

use in http handler

    func testHandler(w http.ResponseWriter, r *http.Request) {
        c := appengine.NewContext(r)

        upload_file := NewUploadFile(c)
        upload_file.Data["Signature"] = "signature"
        upload_file.Data["Active"] = false
        upload_file.Data["User"] = "user"
        upload_file.Save()

        uploadFile := NewUploadFile(c)

        models, err := uploadFile.Query().Paginate(0, 2).
            Filter("Hits >", 0).Order("Hits").GetAll()

        for i, model := range models {
            fmt.Fprintf(w, "%d: %v, %v\n", i, model.Data, err)
        }

        ids := []int64{5796350423728128, 5937087912083456, 6500037865504768, 6359300377149440}

        models, err = uploadFile.GetMultiByIDs(ids)
        for i, model := range models {
            fmt.Fprintf(w, "%d: %v, %v", i, model.Data, err)
            file := UploadFile(model)
            fmt.Fprintf(w, " Actived? %s\n", file.IsActived())
        }       
    } 

