def is_saber_here(matrix, i, j):
  conv_matrix = [[7, 7, 7], [7, 42, 7], [7, 7, 7]]
  return matrix[i-1][j-1:j+2] == conv_matrix[0] and matrix[i][j-1:j+2] == conv_matrix[1] and matrix[i+1][j-1:j+2] == conv_matrix[2]

def main():
  rows, cols = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(rows)]
  
  saber_position = (0, 0)

  for i in range(1, rows-1):
    for j in range(1, cols-1):
      if is_saber_here(matrix, i, j):
        saber_position = (i + 1, j + 1)
        break
  
  print(f'{saber_position[0]} {saber_position[1]}')

if __name__ == "__main__":
    main()