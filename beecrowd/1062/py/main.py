

def main():
    while True:
        n_wagons = int(input())
        if n_wagons == 0:
            break

        while True:
            station = []
            arrival = input()
            sorted_expected = n_wagons
            if arrival == '0':
                break
            arrival = list(map(int, arrival.split()))
            while len(arrival) > 0:
                wagon = arrival.pop()
                while len(station) > 0:
                    if station[-1] == sorted_expected:
                        station.pop()
                        sorted_expected -= 1
                    else:
                        break
                if wagon == sorted_expected:
                    sorted_expected -= 1
                else:
                    station.append(wagon)
            while len(station) > 0:
                wagon = station.pop()
                if wagon == sorted_expected:
                    sorted_expected -= 1
            print('Yes' if sorted_expected == 0 else 'No')
        print('')

if __name__ == "__main__":
    main()