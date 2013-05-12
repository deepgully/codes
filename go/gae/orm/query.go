package orm

import (
	"appengine/datastore"
)

// Query combine datastore.Query and Model together
type Query struct {
	*datastore.Query
	model *Model
}

// NewQuery creates a new Query from a datastore.Query for a specific Model.
func NewQuery(query *datastore.Query, model *Model) *Query {
	return &Query{query, model}
}

// Paginate returns a derivative query that paginated
func (self *Query) Paginate(page int, perPage int) *Query {
	return self.Offset(page * perPage).Limit(perPage)
}

// Offset returns a derivative query that has an offset of how many keys to
// skip over before returning results. A negative value is invalid.
func (self *Query) Offset(offset int) *Query {
	return NewQuery(self.Query.Offset(offset), self.model)
}

// Start returns a derivative query with the given start point.
func (self *Query) Start(c datastore.Cursor) *Query {
	return NewQuery(self.Query.Start(c), self.model)
}

// End returns a derivative query with the given end point.
func (self *Query) End(c datastore.Cursor) *Query {
	return NewQuery(self.Query.End(c), self.model)
}

// KeysOnly returns a derivative query that yields only keys, not keys and
// entities.
func (self *Query) KeysOnly() *Query {
	return NewQuery(self.Query.KeysOnly(), self.model)
}

// Limit returns a derivative query that has a limit on the number of results
// returned. A negative value means unlimited.
func (self *Query) Limit(limit int) *Query {
	return NewQuery(self.Query.Limit(limit), self.model)
}

// Order returns a derivative query with a field-based sort order. Orders are
// applied in the order they are added. The default order is ascending; to sort
// in descending order prefix the fieldName with a minus sign (-).
func (self *Query) Order(fieldName string) *Query {
	return NewQuery(self.Query.Order(fieldName), self.model)
}

// Filter returns a derivative query with a field-based filter.
// The filterStr argument must be a field name followed by optional space,
// followed by an operator, one of ">", "<", ">=", "<=", or "=".
// Fields are compared against the provided value using the operator.
// Multiple filters are AND'ed together.
func (self *Query) Filter(filterStr string, value interface{}) *Query {
	return NewQuery(self.Query.Filter(filterStr, value), self.model)
}

// Ancestor returns a derivative query with an ancestor filter.
// The ancestor should not be nil.
func (self *Query) Ancestor(ancestor *datastore.Key) *Query {
	return NewQuery(self.Query.Ancestor(ancestor), self.model)
}

// GetAll returns array of Model entires, 
// should convert to custom model type for custom functions
func (self *Query) GetAll() ([]*Model, error) {
	var result []Dict

	keys, err := self.Query.GetAll(self.model.Context, &result)
	if err != nil {
		return nil, err
	}

	var entries []*Model

	for i, key := range keys {
		newModel := self.model.Clone(false)
		newModel.key = key
		newModel.ParentKey = key.Parent()
		newModel.Data = result[i]

		entries = append(entries, newModel)
	}

	return entries, nil
}
