package orm

import (
	"appengine"
	"appengine/datastore"
	"reflect"
)

type Dict map[string]interface{}

func (self Dict) Load(c <-chan datastore.Property) error {
	for p := range c {
		if p.Multiple {
			value := reflect.ValueOf(self[p.Name])
			if value.Kind() != reflect.Slice {
				self[p.Name] = []interface{}{p.Value}
			} else {
				self[p.Name] = append(self[p.Name].([]interface{}), p.Value)
			}
		} else {
			self[p.Name] = p.Value
		}
	}
	return nil
}

func (self Dict) Save(c chan<- datastore.Property) error {
	defer close(c)
	for k, v := range self {
		c <- datastore.Property{
			Name:  k,
			Value: v,
		}
	}
	return nil
}

// Model define, implement Save, Key and ID
type Model struct {
	key       *datastore.Key
	ParentKey *datastore.Key
	Context   appengine.Context
	Kind      string
	Data      Dict
}

func NewModel(c appengine.Context, kind string) *Model {
	self := new(Model)
	self.Context = c
	self.Kind = kind
	self.Data = Dict{}
	return self
}

// Clone a model
func (self *Model) Clone(deepcopy bool) *Model {
	newModel := new(Model)
	newModel.Context = self.Context
	newModel.Kind = self.Kind
	newModel.key = self.key
	newModel.ParentKey = self.ParentKey
	newModel.Data = Dict{}
	if deepcopy {
		for k, v := range self.Data {
			newModel.Data[k] = v
		}
	}
	return newModel
}

func (self *Model) Key() *datastore.Key {
	if self.key == nil {
		self.key = datastore.NewIncompleteKey(self.Context, self.Kind, self.ParentKey)
	}
	return self.key
}

func (self *Model) StrKey() string {
	return self.Key().Encode()
}

func (self *Model) ID() int64 {
	return self.Key().IntID()
}

func (self *Model) KeyName() string {
	return self.Key().StringID()
}

func (self *Model) Query() *Query {
	query := datastore.NewQuery(self.Kind)
	return NewQuery(query, self)
}

// Get Entry by Key, return nil if there is no such entry for the Key
func (self *Model) Get(key *datastore.Key) *Model {
	data := Dict{}
	err := datastore.Get(self.Context, key, data)
	if err != nil {
		return nil
	}

	new_model := NewModel(self.Context, self.Kind)
	new_model.key = key
	new_model.Data = data

	return new_model
}

// Get Entry by string key
func (self *Model) GetByStrKey(strKey string) *Model {
	key, err := datastore.DecodeKey(strKey)
	if err != nil {
		return nil
	}
	return self.Get(key)
}

// Get Entry by int64 id, return nil if there is no such entry for the Key
func (self *Model) GetByID(intID int64) *Model {
	key := datastore.NewKey(self.Context, self.Kind, "", intID, self.ParentKey)
	return self.Get(key)
}

// Get Entry by key name, return nil if there is no such entry for the Key
func (self *Model) GetByKeyName(keyname string) *Model {
	key := datastore.NewKey(self.Context, self.Kind, keyname, 0, self.ParentKey)
	return self.Get(key)
}

func (self *Model) Save() (*datastore.Key, error) {
	return datastore.Put(self.Context, self.Key(), &self.Data)
}

func (self *Model) GetItem(name string) interface{} {
	return self.Data[name]
}

func (self *Model) UpdateItem(name string, value interface{}) {
	self.Data[name] = value
}

func (self *Model) RemoveItem(name string) {
	delete(self.Data, name)
}

func (self *Model) Delete() error {
	return datastore.Delete(self.Context, self.Key())
}

func (self *Model) FilterOne(filterStr string, value interface{}) *Model {
	query := self.Query().Filter(filterStr, value).Limit(1)

	entries, err := query.GetAll()
	if err != nil || len(entries) < 1 {
		return nil
	}

	return entries[0]
}

func (self *Model) IsExist(filterStr string, value interface{}) bool {
	query := self.Query().Filter(filterStr, value).Limit(1).KeysOnly()
	count, _ := query.Count(self.Context)
	return count > 0
}

type uploadFile struct {
	*Model
}

// Upload File Store
func UploadFile(c appengine.Context) *uploadFile {
	file := new(uploadFile)
	file.Model = NewModel(c, "UploadFile")
	file.Data = Dict{
		"Signature": "",
		"BlobKey":   "",
		"Hits":      int64(0),
		"Active":    false,
		"User":      "nobody",
	}
	return file
}

func Cast2UploadFile(model *Model) *uploadFile {
	return &uploadFile{model}
}

func (self *uploadFile) ActiveFile() {
	self.Data["Active"] = true
	self.Save()
}
