package main

import (
	"fmt"
	"math"
	"sort"
)

type Property struct {
	Residents   int
	Consumption int
}

func NewProperty(residents, consumption int) *Property {
	return &Property{
		Residents:   residents,
		Consumption: consumption,
	}
}

func PrintCityStatistics(properties []*Property, cityNumber int) {
	fmt.Printf("Cidade# %d:\n", cityNumber)

	propertyStats := ""
	sumConsumption := 0
	sumResidents := 0

	for _, property := range properties {
		propertyStats += fmt.Sprintf("%d-%d ", property.Residents, int(property.Consumption/property.Residents))
		sumConsumption += property.Consumption
		sumResidents += property.Residents
	}
	propertyStats = propertyStats[:len(propertyStats)-1] + "\n"

	fmt.Print(propertyStats)
	fmt.Printf("Consumo medio: %.2f m3.\n", math.Floor(float64(sumConsumption)/float64(sumResidents)))
}

func main() {
	var nbProperties int

	cityNumber := 1

	for {
		fmt.Scanln(&nbProperties)

		if nbProperties < 1 {
			break
		}

		properties := make([]*Property, nbProperties)

		for i := 0; i < nbProperties; i++ {
			var residents, consumption int
			fmt.Scanln(&residents, &consumption)
			properties[i] = NewProperty(residents, consumption)
		}

		sort.Slice(properties, func(i, j int) bool {
			return properties[i].Consumption/properties[i].Residents > properties[j].Consumption/properties[j].Residents
		})

		PrintCityStatistics(properties, cityNumber)

		cityNumber++
	}
}
