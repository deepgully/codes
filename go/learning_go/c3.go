package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println("Chapter 3")
	Q6([]float64{4, 6, -1.222, -1.90e2, 1.11e-2})

	fmt.Println(Q7(7, 2))
	fmt.Println(Q7(2, 7))

	Q9()
	Q10(1e10, 2, 3, 4, 5)
	Q11()
	Q12()
	Q13()
	Q14()
	Q15()
}

func Q6(vals []float64) float64 {
	fmt.Println(vals)
	sum := 0.0
	if len(vals) == 0 {
		return sum
	}

	for _, v := range vals {
		sum += v
	}
	avg := sum / float64(len(vals))
	fmt.Println(avg)
	return avg
}

func Q7(first int, second int) (int, int) {
	if first > second {
		first, second = second, first
	}

	return first, second

}

type Stack struct {
	data []int
}

func (s *Stack) push(i int) {
	if s.data == nil {
		s.data = make([]int, 0)
	}
	s.data = append(s.data, i)
}

func (s *Stack) pop() int {
	l := len(s.data)
	if l == 0 {
		panic("Empty Stack")
	}
	i := s.data[l-1]
	s.data = s.data[0 : l-1]
	return i
}

func (s *Stack) String() string {
	str := ""
	for i, d := range s.data {
		str += fmt.Sprintf("[%d:%v] ", i, d)
	}
	return str
}

func Q9() {
	fmt.Println("Stack")
	defer func() {
		if e := recover(); e != nil {
			fmt.Println(e)
		}
	}()

	stack := new(Stack)
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(6)

	fmt.Println(stack)

	fmt.Println(stack.pop())
	fmt.Println(stack.pop())
	fmt.Println(stack.pop())
	fmt.Println(stack.pop())
	fmt.Println(stack.pop())
}

func Q10(args ...int64) {
	fmt.Println("args")
	for _, i := range args {
		fmt.Println(i)
	}
}

func fib(count int) <-chan int {
	out := make(chan int)
	go func() {
		i, j := 1, 1
		c := 0
		for {
			if c >= count {
				close(out)
				break
			}
			out <- i
			i, j = j, i+j
			c++
		}
	}()
	return out
}

func Q11() {
	fmt.Println("Fib")
	for i := range fib(10) {
		fmt.Println(i)
	}
}

func ccmap(f func(interface{}) interface{}, arr interface{}) interface{} {
	newarr := make([]interface{}, 0)

	slice := reflect.ValueOf(arr)

	for i := 0; i < slice.Len(); i++ {
		v := f(slice.Index(i).Interface())
		newarr = append(newarr, v)
	}
	return newarr
}

func Q12() {
	fmt.Println("MAP")
	f_int := func(a interface{}) interface{} {
		v, _ := a.(int)
		return v * v
	}
	intarr := []int{1, 2, 3, 44, 555, 666}
	intarr2 := ccmap(f_int, intarr)
	fmt.Println(intarr2)

	f_str := func(a interface{}) interface{} {
		v, _ := a.(string)
		return v + v
	}
	strarr := []string{"X", "B", "3", "44", "555", "666"}
	strarr2 := ccmap(f_str, strarr)
	fmt.Println(strarr2)

}

func max(slice []int) int {
	if len(slice) == 0 {
		panic("empty slice")
	}
	max := slice[0]
	for _, i := range slice {
		if max < i {
			max = i
		}
	}
	return max
}

func min(slice []int) int {
	if len(slice) == 0 {
		panic("empty slice")
	}
	min := slice[0]
	for _, i := range slice {
		if min > i {
			min = i
		}
	}
	return min
}

func Q13() {
	fmt.Println("Max&Min")
	fmt.Println(max([]int{2222, 333, 1, -4444, 13232, 222, 6e1}))
	fmt.Println(min([]int{2222, 333, 1, -4444, 13232, 222, 6e1}))
}

func bubbleSort(slice []int) {
	end := len(slice)
	pass := 0
	for {
		swapped := false
		for i := 1; i < end; i++ {
			if slice[i-1] > slice[i] {
				slice[i-1], slice[i] = slice[i], slice[i-1]
				swapped = true
			}
		}
		fmt.Println("Pass", pass, slice, "swapped", swapped)
		end--
		pass++
		if !swapped {
			break
		}
	}
}

func Q14() {
	fmt.Println("Bubble Sort")
	arr := []int{2222, 333, 1, -4444, 13232, 222, 6e1}
	fmt.Println("Begin:", arr)
	bubbleSort(arr)
	fmt.Println("Done:", arr)
}

func plusX(x int) func(int) int {
	return func(i int) int {
		return i + x
	}
}

func Q15() {
	fmt.Println("funcs")
	p := plusX(1)
	fmt.Printf("%v\n", p(2))
}
