package main

import (
	"gonum.org/v1/gonum/mat"
	"math/rand"
	"fmt"
)

func main() {
	d := make([]float64, 25)
	for i := 0; i < len(d); i++ {
		d[i] = rand.Float64()
	}
	t := mat.NewDense(5, 5, d)
	fmt.Println(t)
}