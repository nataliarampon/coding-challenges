def isSquareSafe(map, i, j):
  cameras = 0
  if map[i][j] == '1':
    cameras += 1
  if map[i+1][j] == '1':
    cameras += 1
  if map[i][j+1] == '1':
    cameras += 1
  if map[i+1][j+1] == '1':
    cameras += 1
  return cameras > 1

def main():
  size = int(input())
  map = []
  safetyMap = ''

  for _ in range(size+1):
    map.append(list(input().split()))

  for i in range(size):
    for j in range(size):
      safetyMap += 'S' if isSquareSafe(map, i, j) else 'U'
    safetyMap += '\n'
  
  print(safetyMap[:-1])

if __name__ == '__main__':
  main()