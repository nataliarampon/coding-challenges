# This is giving time limit exceeded

import math
from sys import stdin, stdout

class Property:
    def __init__(self, residents = 0, consumption = 0) -> None:
        self.residents = residents
        self.consumption = consumption
        self.avg = 0
    
    @staticmethod
    def printCityStatistics(properties, city_number):
        stdout.write("Cidade# {}:\n".format(city_number))

        property_stats = ""
        sum_consumption = 0
        sum_residents = 0

        for property in properties:
            property_stats += "{}-{} ".format(property.residents, property.avg)
            sum_consumption += property.consumption
            sum_residents += property.residents
        property_stats = property_stats[:-1] + '\n'

        stdout.write(property_stats)
        stdout.write("Consumo medio: {:.2f} m3.\n".format(math.floor(sum_consumption/sum_residents * 100)/100.0))

city_number = 1

while True:
    nb_properties = int(stdin.readline())

    if nb_properties < 1:
        break
    
    if city_number > 1:
        stdout.write('\n')

    properties = []

    for i in range(nb_properties):
        property = Property()
        property.residents, property.consumption  = map(int, stdin.readline().split())
        property.avg = property.residents // property.consumption
        properties.append(property)
    properties.sort(key=lambda property: property.avg)
    
    Property.printCityStatistics(properties, city_number)

    city_number += 1