if __name__ == '__main__':
  available_meals = list(map(int, input().split()))
  passenger_choices = list(map(int, input().split()))

  rejected_requests = 0
  for i in range(len(passenger_choices)):
    if (available_meals[i] < passenger_choices[i]):
      rejected_requests += (passenger_choices[i] - available_meals[i])
  print(rejected_requests)