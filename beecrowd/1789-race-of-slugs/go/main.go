package main

import (
	"fmt"
	"io"
)

func main() {
	var nb_slugs, current_slug_speed, current_slug_level int

	for {
		_, err := fmt.Scanf("%d\n", &nb_slugs)

		if err == io.EOF {
			break
		}

		max_level := 1

		for i := 0; i < nb_slugs; i++ {
			fmt.Scanf("%d", &current_slug_speed)

			if current_slug_speed < 10 {
				current_slug_level = 1
			} else if current_slug_speed < 20 {
				current_slug_level = 2
			} else {
				current_slug_level = 3
			}

			if current_slug_level > max_level {
				max_level = current_slug_level
			}
		}

		fmt.Printf("%d\n", max_level)
	}
}
