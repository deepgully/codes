package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	fmt.Println("Chapter 2")
	helloWorld()
	Q2_1()
	Q2_2()
	Q2_3([]int{1, 444, 666, 888, -11, 1e4})
	Q3()
	Q4_1()
	Q4_2()
	Q4_3()
	Q4_4()
	Q5()
}

func helloWorld() {
	fmt.Println("Hello World! Go")
}

func Q2_1() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}

func Q2_2() {
	i := 0
loop:
	if i < 10 {
		fmt.Println(i)
		i++
		goto loop
	}
}

func Q2_3(arr []int) {
	for i, val := range arr {
		fmt.Println(i, val)
	}
}

func Q3() {
	for i := 1; i <= 100; i++ {
		if i%3 == 0 {
			fmt.Print("Fizz")
			if i%5 == 0 {
				fmt.Print("Buzz")
			}
		} else if i%5 == 0 {
			fmt.Print("Buzz")
		} else {
			fmt.Print(i)
		}
		fmt.Println()
	}
}

func Q4_1() {
	for i := 1; i <= 100; i++ {
		fmt.Println(strings.Repeat("A", i))
	}
}

var str string

func Q4_2() {
	str = "asSASA ddd dsjkdsjs dk 中文"
	fmt.Println("Len:", len(str), "Bytes:", len([]byte(str)), "Count:", utf8.RuneCountInString(str))
}

func Q4_3() {
	str = "asSASA ddd dsjkdsjs dk 中文"
	str = strings.Replace(str, str[4:7], "abc", 1)
	fmt.Println(str)
}

func Q4_4() {
	str = "foobar中文"
	runeslice := []rune(str)
	start := 0
	end := len(runeslice) - 1
	for {
		if start < end {
			runeslice[start], runeslice[end] = runeslice[end], runeslice[start]
			start++
			end--
		} else {
			break
		}
	}
	fmt.Println(string(runeslice))
}

func Q5() {
	vals := []float64{4, 6, -1.222, -1.90e2, 1.11e-2}
	fmt.Println(vals)
	sum := 0.0
	for _, v := range vals {
		sum += v
	}
	avg := sum / float64(len(vals))
	fmt.Println(avg)
}
