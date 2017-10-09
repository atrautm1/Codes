package main

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"os"
	"sort"
	"strings"
)

//FastaSequence struct holds each header and sequence
type FastaSequence struct {
	Header   string
	Sequence string
}

//Pair is used as a constructor for a map(k,v) for accessing
type Pair struct {
	Key   string
	Value int
}

//PairList is a slice (list/array) of type Pair
//Holds key,value pairs from a map
type PairList []Pair

func main() {
	/*
		fastaList := readFastaFile("/Users/atrautm1/Desktop/gradFall2017/programming/rando.fasta")

		for _, seq := range fastaList {
			fmt.Println(getHeader(seq))
			fmt.Println(getSequence(seq))
			fmt.Println(getGCRatio(seq))
		}
	*/
	writeUnique("/Users/atrautm1/Desktop/gradFall2017/programming/rando2.fasta", "/Users/atrautm1/Desktop/gradFall2017/programming/goOut.txt")
}

func writeUnique(inFile string, outFile string) {

	//read the fasta file and generate a fastaList
	fastaList := readFastaFile(inFile)

	//Create an outFile, and check for errors
	f, err := os.Create(outFile)
	check(err)
	defer f.Close()

	//Buffered writer
	w := bufio.NewWriter(f)

	//Basic hashmap constructor with string keys and integer values
	myMap := make(map[string]int)

	//iterate through fastaList and insert into map count of sequences
	for _, seq := range fastaList {
		sequence := getSequence(seq)
		_, v := myMap[sequence]
		if v {
			myMap[sequence] = myMap[sequence] + 1
		} else {
			myMap[sequence] = 1
		}
	}

	//Using built-in make to make a PairList the length of the map
	seqList := make(PairList, len(myMap))

	//iterate through the map, and add pairs to seqList at specific places
	i := 0
	for k, v := range myMap {
		seqList[i] = Pair{k, v}
		i++
	}
	//sort the list
	sort.Sort(seqList)

	//write the list to a file
	for _, v := range seqList {
		w.WriteString(fmt.Sprintln(">", v.Value))
		w.WriteString(v.Key)
	}

	//flush the buffered writer, close is already called through the defer statement above
	w.Flush()

}

func getHeader(fastaSequence FastaSequence) string {
	return fastaSequence.Header
}

func getSequence(fastaSequence FastaSequence) string {
	return fastaSequence.Sequence
}

func getGCRatio(fastaSequence FastaSequence) float32 {
	seq := fastaSequence.Sequence
	count := 0
	for _, char := range seq {
		if string(char) == "G" {
			count++
		} else if string(char) == "C" {
			count++
		}
	}

	return (float32(count) / float32(len(seq)))

}

func readFastaFile(file string) []FastaSequence {
	f, err := os.Open(file)
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)

	myList := []FastaSequence{}

	var header = "NULL"
	var sequence bytes.Buffer

	for scanner.Scan() {
		line := scanner.Text()
		if header == "NULL" {
			if !strings.HasPrefix(line, ">") {
				fmt.Println(errors.New("your file appears to be missing a header"))
			} else {
				header = line
			}
		} else if strings.HasPrefix(line, ">") {
			fs := FastaSequence{Header: header, Sequence: strings.ToUpper(sequence.String())}
			myList = append(myList, fs)
			header = line
			sequence.Reset()
		} else {
			sequence.WriteString(line)
		}
	}
	check(err)
	fs := FastaSequence{Header: header, Sequence: strings.ToUpper(sequence.String())}
	myList = append(myList, fs)
	return myList
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

//https://stackoverflow.com/questions/18695346/how-to-sort-a-mapstringint-by-its-values
//Optimized from
func (p PairList) Len() int           { return len(p) }
func (p PairList) Less(i, j int) bool { return p[i].Value < p[j].Value }
func (p PairList) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
