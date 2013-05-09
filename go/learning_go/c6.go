package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println("Chapter 6")

	Q26()
}

type everything interface{}

func max(arr everything, less func(e1 everything, e2 everything) bool) everything {

	slice := reflect.ValueOf(arr)

	max := slice.Index(0).Interface()
	for i := 1; i < slice.Len(); i++ {
		v := slice.Index(i).Interface()
		if less(max, v) {
			max = v
		}
	}
	return max
}

func Q26() {
	fmt.Println("Q26 interface and max")

	less := func(e1 everything, e2 everything) bool {
		switch e1.(type) {
		case int:
			if _, ok := e2.(int); ok {
				return e1.(int) < e2.(int)
			}
		case float32:
			if _, ok := e2.(float32); ok {
				return e1.(float32) < e2.(float32)
			}
		case string:
			if _, ok := e2.(string); ok {
				return e1.(string) < e2.(string)
			}
		}
		return false
	}

	fmt.Println("int:", max([]int{2222, 333, 1, -4444, 13232, 222, 699}, less))
	fmt.Println("float32:", max([]float32{1.2, 99999.66, 1, -4444, 13232, 222, 6.993e9}, less))
	fmt.Println("string:", max([]string{"1111", "a99999.66", "A1", "b4444", "Ba213232", "222", "6.993e9"}, less))
}
