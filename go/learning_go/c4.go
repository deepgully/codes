package main

import (
	"./stack"
	"errors"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Chapter 4")
	Q16()
	Q17()
}

func Q16() {
	fmt.Println("Package stack")

	stack := stack.New()
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
	stack.Push(6)

	fmt.Println(stack)

	stack.Pop()
	stack.Pop()
	stack.Pop()
	stack.Pop()

	fmt.Println(stack)
}

func EvalRPN(strRPN string) (int, error) {
	arr := strings.Split(strRPN, " ")
	stack := stack.New()

	for _, s := range arr {
		i, err := strconv.Atoi(s)
		if err == nil {
			stack.Push(i)
		} else {
			var d int
			switch s {
			case "+":
				d = stack.Pop() + stack.Pop()
			case "-":
				d1, d2 := stack.Pop(), stack.Pop()
				d = d2 - d1
			case "*":
				d = stack.Pop() * stack.Pop()
			case "/":
				d1, d2 := stack.Pop(), stack.Pop()
				d = d2 / d1
			default:
				panic("wrong RPN string")
			}
			stack.Push(d)
		}
		fmt.Println(stack)
	}

	if stack.Size() == 1 {
		return stack.Pop(), nil
	}
	fmt.Println(stack)
	return -1, errors.New("wrong input")
}

var testing = map[string]string{"test1": "5 1 2 + 4 * + 3 -", "test2": "3 4 5 * -", "test3": "3 4 - 5 *"}

func Q17() {
	fmt.Println("RPN Calculator")

	for name, rpn := range testing {
		fmt.Println("\n", name, `"`, rpn, `"`)
		res, err := EvalRPN(rpn)
		fmt.Println("Result:", res, "Error:", err)
	}

}
