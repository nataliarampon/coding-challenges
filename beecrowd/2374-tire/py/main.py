def getTirePressureDifference(desired_pressure, current_presssure):
  return desired_pressure - current_presssure;

if __name__ == "__main__":
  desired_pressure, current_presssure = int(input()), int(input())
  print(getTirePressureDifference(desired_pressure, current_presssure))