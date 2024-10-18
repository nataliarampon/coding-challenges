# Also giving Time Limit Exceeded
# Tried putting all write operations into a single call to speed up I/O
# Also, putting things in lists instead of having a gigantic string concatenation
# And removing the classes and keeping everything in a tuple
# But it's still not good enough... C++ it's I guess

import math
from sys import stdin, stdout

def printCityStatistics(properties, city_number):
    res = ["Cidade# {}:\n".format(city_number)]

    property_stats = []
    sum_consumption = 0
    sum_residents = 0

    for property in properties:
        property_stats.append("{}-{} ".format(property[RESIDENTS], property[AVERAGE]))
        sum_consumption += property[CONSUMPTION]
        sum_residents += property[RESIDENTS]

    res.append(' '.join(property_stats) + '\n')
    res.append("Consumo medio: {:.2f} m3.\n".format(math.floor(sum_consumption/sum_residents * 100)/100.0))
    stdout.write(''.join(res))

city_number = 1
RESIDENTS = 0
CONSUMPTION = 1
AVERAGE = 2

while True:
    nb_properties = int(stdin.readline())

    if nb_properties == 0:
        break
    
    if city_number > 1:
        stdout.write('\n')

    properties = []

    for i in range(nb_properties):
        residents, consumption  = map(int, stdin.readline().split())
        avg = residents // consumption
        properties.append((residents, consumption, avg))
    properties.sort(key=lambda property: property[AVERAGE])
    
    printCityStatistics(properties, city_number)

    city_number += 1