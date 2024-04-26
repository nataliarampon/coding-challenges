import math

def isRobberReachable(distance, speed_robber, speed_guard):
  DISTANCE_LIMIT = 12
  hypotenuse = math.sqrt(DISTANCE_LIMIT**2 + distance**2)
  return (hypotenuse/speed_guard) <= (DISTANCE_LIMIT/speed_robber)

if __name__ == "__main__":
  while True:
    try:
      distance, speed_robber, speed_guard = map(int, input().split())
      print('S' if isRobberReachable(distance, speed_robber, speed_guard) else 'N')
    
    except EOFError:
      break