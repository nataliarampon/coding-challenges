def checkLines(matrix):
  for i in range(9):
    positions = [False] * 9
    for n in matrix[i]:
      positions[n-1] = True
    if not all(positions):
      return False
  return True

def checkColumns(matrix):
  for i in range(9):
    positions = [False] * 9
    for j in range(9):
      positions[matrix[j][i]-1] = True
    if not all(positions):
      return False
  return True

def checkSubmatrix(matrix):
  for subLine in range(3):
    for subCol in range(3):
      positions = [False] * 9
      for i in range(3):
        for j in range(3):
          positions[matrix[3*subLine+i][3*subCol+j]-1] = True
      if not all(positions):
        return False
  return True

def main():
  for i in range(int(input())):
    matrix = []
    for _ in range(9):
      matrix.append(list(map(int, input().split())))
    ok = checkLines(matrix) and checkColumns(matrix) and checkSubmatrix(matrix)
    print(f'Instancia {i+1}')
    print('SIM' if ok else 'NAO')
    print('')

if __name__ == "__main__":
  main()