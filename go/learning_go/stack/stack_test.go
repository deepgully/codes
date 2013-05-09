package stack

import (
	"testing"
)

func TestNewStack(t *testing.T) {
	stack := new(Stack)
	if stack == nil {
		t.Fail()
	}
}

func TestStack(t *testing.T) {
	stack := new(Stack)
	i := 12
	stack.Push(i)
	j := stack.Pop()

	if i != j {
		t.Fail()
	}
}

func TestPop(t *testing.T) {
	defer func() {
		if e := recover(); e == nil {
			t.Log("except panic")
			t.Fail()
		}
	}()
	stack := new(Stack)
	stack.Push(12)
	stack.Pop()
	stack.Pop()
}

func TestBigSize(t *testing.T) {
	stack := new(Stack)

	big := 10000000
	for i := 0; i < big; i++ {
		stack.Push(i)
	}
	if stack.Size() != big {
		t.Log("wrong stack size")
		t.Fail()
	}
	for i := 0; i < big; i++ {
		stack.Pop()
	}
	if stack.Size() != 0 {
		t.Log("wrong stack size")
		t.Fail()
	}
}

func TestValue(t *testing.T) {
	stack := new(Stack)

	arr := []int{1, 2, 3, 4, 5, 6, 7}
	for i := 0; i < len(arr); i++ {
		stack.Push(arr[i])
	}
	for i := 0; i < len(arr); i++ {
		v := stack.Pop()
		if v != arr[len(arr)-i-1] {
			t.Log("value dismatch")
			t.FailNow()
		}
	}
}
