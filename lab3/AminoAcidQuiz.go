package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

//Amino Acid code dictionary
// := is used to initialize any variable
// [20] is the length of the array, must be specified in this case
// string is the type of value in the array
// Also, if it's not used somewhere in the code, it will complain and not run
var aaCodes = [20]string{
	"A", "R", "N", "D", "C", "Q", "E",
	"G", "H", "I", "L", "K", "M", "F",
	"P", "S", "T", "W", "Y", "V"}

var aaFull = [20]string{
	"alanine", "arginine", "asparagine",
	"aspartic acid", "cysteine",
	"glutamine", "glutamic acid",
	"glycine", "histidine", "isoleucine",
	"leucine", "lysine", "methionine",
	"phenylalanine", "proline",
	"serine", "threonine", "tryptophan",
	"tyrosine", "valine"}

var score = 0

func quiz() {
	// New reader accepts standard in as the input
	reader := bufio.NewReader(os.Stdin)
	x := 0

	for x < len(aaFull) {
		fmt.Println("What is the one letter codon amino acid " + aaFull[x] + "? ")
		// input dubbed 'text' reads an entire string upto and including the byte, in this case the newline
		// adopted from https://tutorialedge.net/golang/reading-console-input-golang/
		text, _ := reader.ReadString('\n')

		// removes the newline char and converts to uppercase
		// replace following line with commented line for windows machines
		text = strings.ToUpper(strings.TrimSpace(text))
		// text = strings.Replace(text, "\r\n", "", -1)
		if text == aaCodes[x] {
			score++
		} else {
			fmt.Println("You entered: " + text + " ; The codon is actually: " + aaCodes[x])
			fmt.Println("Your score was: ", score)
			os.Exit(0)
		}
		x++
	}
	fmt.Println("Your score was: ", score)
}

func timer() {
	// Tell this function one to sleep for x seconds and then it executes the following code
	// Probably a better way to do this
	time.Sleep(time.Second * 5)
	fmt.Println("Time's up!")
	// score had to be converted to a printable type
	// string(int) didn't seem to work
	fmt.Println("Your score was: ", score)
	os.Exit(0)
}

func main() {
	// go <func> is a lightweight version of multithreading
	// Managed by go runtime
	// this main function starts the timer on a separate channel, and then starts the quiz
	go timer()
	quiz()

}
