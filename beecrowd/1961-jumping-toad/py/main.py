def main():
  result = 'YOU WIN'
  jump, nb_pipes = map(int, input().split())
  pipes = list(map(int, input().split()))

  for i in range(nb_pipes-1):
    if abs(pipes[i] - pipes[i+1]) > jump:
      result = 'GAME OVER'
      break
  print(result)  

if __name__ == '__main__':
  main()