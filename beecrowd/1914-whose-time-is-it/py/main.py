def main():
  cases = int(input())
  for _ in range(cases):
    player_1, choice_1, player_2, _ = input().split()
    number_1, number_2 = map(int, input().split())
    if (number_1 + number_2) % 2 == 0:
      if choice_1 == 'PAR':
        print(player_1)
      else: 
        print(player_2)
    else:
      if choice_1 == 'IMPAR':
        print(player_1)
      else:
        print(player_2)

if __name__ == '__main__':
  main()