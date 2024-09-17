def main():
  cars = {
    'SALIDA': 0,
    'VUELTA': 0
  }

  people_in_park = 0

  while True:
    line = input().split()
    direction = line[0]
    if direction == 'ABEND':
      break
    else:
      nb_people = int(line[1])
      cars[direction] += 1
      if direction == 'SALIDA':
        people_in_park += nb_people
      else:
        people_in_park -= nb_people

  print(people_in_park)
  print(cars['SALIDA'] - cars['VUELTA'])

if __name__ == "__main__":
  main()