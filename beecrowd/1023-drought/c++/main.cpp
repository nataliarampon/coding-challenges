#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>

using namespace std;

struct Property {
    int residents;
    int consumption;
    int average;
};

void printCityStatistics(const map<int,int>& properties_map, int city_number, int total_consumption, int total_residents) {
    printf("Cidade# %d:\n", city_number);

    string property_stats = "";
    for (auto const& [key, val] : properties_map) {
        property_stats += to_string(val) + "-" + to_string(key) + " ";
    }
    property_stats.pop_back();
    cout << property_stats << endl;

    double average_consumption = floor(total_consumption / (double) total_residents * 100) / 100.0;
    printf("Consumo medio: %.2f m3.\n", average_consumption);
}

int main() {
    int city_number = 1;

    while (true) {
        int nb_properties;
        cin >> nb_properties;

        if (nb_properties == 0) {
            break;
        }

        if (city_number > 1) {
            cout << endl;
        }

        map<int, int> properties;
        int total_consumption = 0;
        int total_residents = 0;

        for (int i = 0; i < nb_properties; ++i) {
            int residents, consumption;
            cin >> residents >> consumption;

            total_consumption += consumption;
            total_residents += residents;

            int avg = consumption / residents;
            if (properties.count(avg)) {
                properties[avg] += residents;
            } else {
                properties[avg] = residents;
            }
        }

        // Maps in C++ are ordered in key crescent order by default,
        // so no need to sort the map by average consumption
        printCityStatistics(properties, city_number, total_consumption, total_residents);

        city_number++;
    }

    return 0;
}
