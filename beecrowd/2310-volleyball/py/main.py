def main():
  players = int(input())
  total_attemps = [0, 0, 0]
  total_successes = [0, 0, 0]
  for _ in range(players):
    _ = input()
    attempts = list(map(int, input().split()))
    success = list(map(int, input().split()))
    for i in range(3):
      total_attemps[i] += attempts[i]
      total_successes[i] += success[i]
  
  print(f'Pontos de Saque: {(total_successes[0]/total_attemps[0])*100:.2f} %.')
  print(f'Pontos de Bloqueio: {(total_successes[1]/total_attemps[1])*100:.2f} %.')
  print(f'Pontos de Ataque: {(total_successes[2]/total_attemps[2])*100:.2f} %.')

if __name__ == '__main__':
  main()