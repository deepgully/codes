package main

import (
	"fmt"
)

func main() {
	fmt.Println("Chapter 7")

	Q27()

	Q28()

}

func shower(ch chan int, quit chan bool) {
	for {
		select {
		case d := <-ch:
			fmt.Println(d)
		case <-quit:
			fmt.Println("Quit")
			return
		}
	}
}

func Q27() {
	fmt.Println("Q27 Channel")
	ch := make(chan int)
	quit := make(chan bool)
	go shower(ch, quit)

	for i := 0; i < 10; i++ {
		ch <- i
	}
	quit <- false
}

func fib(count int) <-chan int {
	out := make(chan int, 1)
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

func Q28() {
	fmt.Println("Q28 Fibonacci")
	for i := range fib(10) {
		fmt.Println(i)
	}
}
