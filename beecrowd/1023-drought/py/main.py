# -*- coding: utf-8 -*-

import math

class Property:
    def __init__(self, residents = 0, consumption = 0) -> None:
        self.residents = residents
        self.consumption = consumption
    
    @staticmethod
    def printCityStatistics(properties, city_number):
        print("Cidade# {}:".format(city_number))

        property_stats = ""
        sum_consumption = 0
        sum_residents = 0

        for property in properties:
            property_stats += "{}-{} ".format(property.residents, property.consumption//property.residents)
            sum_consumption += property.consumption
            sum_residents += property.residents
        property_stats = property_stats[:-1] + '\n'

        print(property_stats, end='')
        print("Consumo medio: {:.2f} m3.".format(math.floor(sum_consumption/sum_residents)))

city_number = 1

while True:
    nb_properties = int(input())

    if nb_properties < 1:
        break;

    properties = []

    for i in range(nb_properties):
        property = Property()
        property.residents, property.consumption  = map(int, input().split())
        properties.append(property)
    properties.sort(key=lambda property: property.consumption//property.residents)
    
    Property.printCityStatistics(properties, city_number)

    city_number += 1
