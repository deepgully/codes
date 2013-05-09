package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func main() {
	fmt.Println("Chapter 8")

	Q29()

	Q30()

	Q31()

	Q32()
}

func filter(c rune) rune {
	if c > 127 {
		return 64
	}
	return c
}

func Q29() {
	fmt.Println("Q29")

	cmd := exec.Command("cmd.exe", "/c", "tasklist")

	buf, err := cmd.Output()
	if err == nil {
		buf2 := bytes.Map(filter, buf)
		fmt.Print(string(buf2))
	} else {
		fmt.Println(err)
	}
}

func Q30() {
	fmt.Println("Q30 word count")

	reader := bufio.NewReader(os.Stdin)

	var chars, words, lines int

	for {
		input, ok := reader.ReadString('\n')
		if ok != nil {
			fmt.Println(chars, words, lines)
			return
		}
		chars += len(input)
		words += len(strings.Fields(input))
		lines++
	}
}

func Q31() {
	fmt.Println("Q31 Uniq")

	list := []string{"a", "b", "a", "a", "c", "d", "e", "f"}

	cur := list[0]
	fmt.Print(cur)
	for _, s := range list[1:] {
		if cur != s {
			cur = s
			fmt.Print(s)
		}
	}
}

func Q32() {
	fmt.Println("Q32 Quine")
	fmt.Printf("%s%c%s%c\n", self, 0x60, self, 0x60)
}

var self = `
func Q32() {
    fmt.Println("Q32 Quine")
    fmt.Printf("%s%c%s%c\n", self, 0x60, self, 0x60)
}

var self = `
