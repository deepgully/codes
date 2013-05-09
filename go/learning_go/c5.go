package main

import (
	"bufio"
	"container/list"
	"flag"
	"fmt"
	"io"
	"os"
	"reflect"
)

func main() {
	fmt.Println("Chapter 5")

	Q19()

	Q20()

	Q21()

	Q22()
}

type everything interface{}

func ccmap(f func(everything) everything, arr everything) everything {
	newarr := make([]everything, 0)

	slice := reflect.ValueOf(arr)

	for i := 0; i < slice.Len(); i++ {
		v := f(slice.Index(i).Interface())
		newarr = append(newarr, v)
	}
	return newarr
}

func Q19() {
	fmt.Println("Q19 MAP")
	f := func(a everything) everything {
		switch a.(type) {
		case int:
			return a.(int) * 2
		case string:
			return a.(string) + a.(string)
		}
		return a
	}
	intarr := []int{1, 2, 3, 44, 555, 666}
	intarr2 := ccmap(f, intarr)
	fmt.Println(intarr2)

	strarr := []string{"X", "B", "3", "44", "555", "666"}
	strarr2 := ccmap(f, strarr)
	fmt.Println(strarr2)

}

func Q20() {
	fmt.Println("Q20")

	type Person struct {
		name string
		age  int
	}

	var p1 Person
	fmt.Println(p1)
	p2 := new(Person)
	fmt.Println(p2)
}

type listElem struct {
	next  *listElem
	prev  *listElem
	Value interface{}
}

func (le *listElem) Next() *listElem { return le.next }

func (le *listElem) Prev() *listElem { return le.prev }

type cclist struct {
	first  *listElem
	last   *listElem
	length int
}

func NewList() *cclist {
	return new(cclist)
}

func (self *cclist) Front() *listElem {
	return self.first
}

func (self *cclist) Back() *listElem {
	return self.last
}

func (self *cclist) PushFront(value interface{}) *listElem {
	le := new(listElem)
	le.Value = value

	if self.first == nil {
		self.first, self.last = le, le
		self.length = 1
		return le
	}

	le.next = self.first
	self.first.prev = le
	self.first = le
	self.length++
	return le
}

func (self *cclist) PushBack(value interface{}) *listElem {
	le := new(listElem)
	le.Value = value

	if self.last == nil {
		self.first, self.last = le, le
		self.length = 1
		return le
	}

	le.prev = self.last
	self.last.next = le
	self.last = le
	self.length++
	return le
}

func (self *cclist) InsertBefore(value interface{}, mark *listElem) *listElem {
	if mark.prev == nil {
		return self.PushFront(value)
	}
	le := new(listElem)
	le.Value = value

	le.next = mark
	le.prev = mark.prev

	mark.prev.next = le
	mark.prev = le

	self.length++

	return le
}

func (self *cclist) InsertAfter(value interface{}, mark *listElem) *listElem {
	if mark.next == nil {
		return self.PushBack(value)
	}
	le := new(listElem)
	le.Value = value

	le.next = mark.next
	le.prev = mark

	mark.next.prev = le
	mark.next = le

	self.length++

	return le
}

func Q21() {
	fmt.Println("Q21 List")
	li := list.New()

	fmt.Println("List 1")
	li.PushBack(1)
	e := li.Front()
	li.InsertAfter(2, e)
	li.InsertAfter(3, e)
	li.InsertBefore(4, e)
	li.InsertBefore(5, e)
	li.PushFront(6)
	li.PushBack(7)

	p := li.Front()
	for {
		if p != nil {
			fmt.Println(p.Value)
		} else {
			break
		}
		p = p.Next()
	}

	fmt.Println("List 2")
	li2 := NewList()

	li2.PushBack(1)
	e2 := li2.Front()
	li2.InsertAfter(2, e2)
	li2.InsertAfter(3, e2)
	li2.InsertBefore(4, e2)
	li2.InsertBefore(5, e2)
	li2.PushFront(6)
	li2.PushBack(7)

	p2 := li2.Front()
	for {
		if p2 != nil {
			fmt.Println(p2.Value)
		} else {
			break
		}
		p2 = p2.Next()
	}
}

func Q22() {
	fmt.Println("Q22 Cat")
	var lineNumFlag = flag.Bool("n", false, "Line Num Mode")

	flag.Parse()

	if flag.NArg() == 0 {
		fmt.Fprintf(os.Stdout, "Usage: cat [-n] filename\n")
		return
	}

	f, err := os.OpenFile(flag.Arg(0), os.O_RDONLY, 0)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error reading file %s\n", flag.Arg(0))
		return
	}
	defer f.Close()

	line := 1
	reader := bufio.NewReader(f)
	for {
		buf, err := reader.ReadBytes('\n')
		if err == io.EOF {
			break
		}
		if *lineNumFlag {
			fmt.Fprintf(os.Stdout, "%d: %s", line, buf)
			line++
		} else {
			fmt.Fprintf(os.Stdout, "%s", buf)
		}
	}
}
