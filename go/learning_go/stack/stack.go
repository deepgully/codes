/*
The stack package
*/
package stack

import (
	"fmt"
)

type Stack struct {
	data []int
}

func New() *Stack {
	return new(Stack)
}

func (s *Stack) Push(i int) {
	if s.data == nil {
		s.data = make([]int, 0)
	}
	s.data = append(s.data, i)
}

func (s *Stack) Pop() int {
	l := len(s.data)
	if l == 0 {
		panic("Empty Stack")
	}
	i := s.data[l-1]
	s.data = s.data[0 : l-1]
	return i
}

func (s *Stack) Size() int {
	return len(s.data)
}

func (s *Stack) String() string {
	str := "<Stack: [ "
	for _, d := range s.data {
		str += fmt.Sprintf("%v ", d)
	}
	return str + "]>"
}
