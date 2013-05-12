/*
GAE datastore ORM
*/
package orm

import (
	"appengine"
	"appengine/datastore"
	"reflect"
)

// Dict is type of map[string]interface{}
// implement interface PropertyLoadSaver to support datastore Load&Save
type Dict map[string]interface{}

// PropertyLoadSaver can be converted from and to a sequence of Properties.
// Load should drain the channel until closed, even if an error occurred.
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

// Save should close the channel when done, even if an error occurred.
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

// Create a Model, bind to current appengine context and Kind
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
// should convert to custom model type for custom functions
func (self *Model) Get(key *datastore.Key) *Model {
	data := Dict{}
	err := datastore.Get(self.Context, key, data)
	if err != nil {
		return nil
	}

	newModel := NewModel(self.Context, self.Kind)
	newModel.key = key
	newModel.ParentKey = key.Parent()
	newModel.Data = data

	return newModel
}

// GetMulti is a batch version of Get.
// return []*Model, appengine.MultiError
func (self *Model) GetMulti(keys []*datastore.Key) ([]*Model, appengine.MultiError) {
	data := make([]Dict, len(keys))
	for i := 0; i < len(keys); i++ {
		data[i] = Dict{}
	}

	errs := datastore.GetMulti(self.Context, keys, data)

	models := make([]*Model, len(keys))
	for i, entry := range data {
		if entry != nil {
			newModel := NewModel(self.Context, keys[i].Kind())
			newModel.key = keys[i]
			newModel.ParentKey = keys[i].Parent()
			newModel.Data = entry
			models[i] = newModel
		} else {
			models[i] = nil
		}
	}

	if errs, ok := errs.(appengine.MultiError); ok {
		return models, errs
	}
	return models, nil
}

// Get Entry by string key
func (self *Model) GetByStrKey(strKey string) *Model {
	key, err := datastore.DecodeKey(strKey)
	if err != nil {
		return nil
	}
	return self.Get(key)
}

// Get Multi Entries by string keys
func (self *Model) GetMultiByStrKeys(strKeys []string) ([]*Model, appengine.MultiError) {
	keys := make([]*datastore.Key, len(strKeys))
	for i, strKey := range strKeys {
		key, _ := datastore.DecodeKey(strKey)
		keys[i] = key
	}
	return self.GetMulti(keys)
}

// Get Entry by int64 id, return nil if there is no such entry for the Key
func (self *Model) GetByID(intID int64) *Model {
	key := datastore.NewKey(self.Context, self.Kind, "", intID, self.ParentKey)
	return self.Get(key)
}

// Get Multi Entries by int64 ids
func (self *Model) GetMultiByIDs(ids []int64) ([]*Model, appengine.MultiError) {
	keys := make([]*datastore.Key, len(ids))
	for i, id := range ids {
		keys[i] = datastore.NewKey(self.Context, self.Kind, "", id, self.ParentKey)
	}
	return self.GetMulti(keys)
}

// Get Entry by key name, return nil if there is no such entry for the Key
func (self *Model) GetByKeyName(keyName string) *Model {
	key := datastore.NewKey(self.Context, self.Kind, keyName, 0, self.ParentKey)
	return self.Get(key)
}

// Get Multi Entries by string key names
func (self *Model) GetMultiByKeyNames(keyNames []string) ([]*Model, appengine.MultiError) {
	keys := make([]*datastore.Key, len(keyNames))
	for i, keyName := range keyNames {
		keys[i] = datastore.NewKey(self.Context, self.Kind, keyName, 0, self.ParentKey)
	}
	return self.GetMulti(keys)
}

// Save entry
func (self *Model) Save() (*datastore.Key, error) {
	return datastore.Put(self.Context, self.Key(), &self.Data)
}

// Delete entry
func (self *Model) Delete() error {
	return datastore.Delete(self.Context, self.Key())
}

// Get data item
func (self *Model) GetItem(name string) interface{} {
	return self.Data[name]
}

// Update data item
func (self *Model) UpdateItem(name string, value interface{}) {
	self.Data[name] = value
}

// Remove data item
func (self *Model) RemoveItem(name string) {
	delete(self.Data, name)
}

// Get one entry using filter, return nil if there is no such entity for the key
func (self *Model) FilterOne(filterStr string, value interface{}) *Model {
	query := self.Query().Filter(filterStr, value).Limit(1)

	entries, err := query.GetAll()
	if err != nil || len(entries) < 1 {
		return nil
	}

	return entries[0]
}

// Check exist using filter
func (self *Model) IsExist(filterStr string, value interface{}) bool {
	query := self.Query().Filter(filterStr, value).Limit(1).KeysOnly()
	count, _ := query.Count(self.Context)
	return count > 0
}
