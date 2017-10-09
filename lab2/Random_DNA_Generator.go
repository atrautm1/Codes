package main

import (
	"fmt"
	"math/rand"
)

func main() {

	dnaNumString := make([]int, 0)
	for i := 0; i < 3000; i++ {
		dnaNumString = append(dnaNumString, (rand.Intn(4) + 1))
	}
	tripleAAACount := 0
	dnaTrip := ""

	for i := 0; i < len(dnaNumString); i++ {
		if dnaNumString[i] == 1 {
			dnaTrip += "A"
		} else if dnaNumString[i] == 2 {
			dnaTrip += "G"
		} else if dnaNumString[i] == 3 {
			dnaTrip += "T"
		} else if dnaNumString[i] == 4 {
			dnaTrip += "C"
		}
		if len(dnaTrip) == 3 {
			if dnaTrip == "AAA" {
				tripleAAACount++
			}
			fmt.Println(dnaTrip)
			dnaTrip = ""
		}
	}
	fmt.Println("The amount of AAA's generated was: ", tripleAAACount)
}
