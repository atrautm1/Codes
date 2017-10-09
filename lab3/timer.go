package main

import (
  "fmt"
  "time"

)

func main() {
  c2 := make(chan string, 1)
    go func() {
        time.Sleep(time.Second * 10)
        c2 <- "result 2"
    }()
    select {
    case res := <-c2:
        fmt.Println(res)
    case <-time.After(time.Second * 1):
        fmt.Println("timeout 2")
    }
}
