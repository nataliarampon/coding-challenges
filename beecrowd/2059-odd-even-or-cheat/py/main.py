def main():
  choice_even, p1, p2, cheat, accuse = map(int, input().split())
  winner = 1

  if cheat and accuse:
    winner = 2
  elif cheat and not accuse:
    winner = 1
  elif accuse and not cheat:
    winner = 1
  else:
    if choice_even and (p1 + p2) % 2 == 0:
      winner = 1
    elif not choice_even and (p1 + p2) % 2 == 1:
      winner = 1
    else:
      winner = 2
  
  print(f'Jogador {winner} ganha!')

if __name__ == '__main__':
  main()