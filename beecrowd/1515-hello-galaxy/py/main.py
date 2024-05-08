if __name__ == '__main__':
  MAX_DATE = 2115

  while True:
    cases = int(input())
    if cases == 0:
      break
    
    first_planet = (MAX_DATE,'') # min_date, planet_name
    for _ in range(cases):
      planet, arrival_date, travel_time = input().split()
      if (int(arrival_date) - int(travel_time)) < first_planet[0]:
        first_planet = (int(arrival_date) - int(travel_time), planet)
    print(first_planet[1])