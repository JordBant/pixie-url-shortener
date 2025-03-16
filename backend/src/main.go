package main

import "fmt"

type GasEngine struct {
	mpg       uint8
	gallons   uint8
	ownerInfo Owner
}

type Owner struct {
	name []rune
	id   uint
}

func main() {
	var user1 Owner = Owner{[]rune("Kevin"), 1}
	var eng GasEngine = GasEngine{24, 9, user1}

	fmt.Println(eng)
	fmt.Println(user1)
}
