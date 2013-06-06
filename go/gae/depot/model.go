package depot

import (
	"appengine"
	"orm"
)

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
