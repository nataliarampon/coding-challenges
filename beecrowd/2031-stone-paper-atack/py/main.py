def main():
  for _ in range(int(input())):
    player1 = input()
    player2 = input()
    
    if player1 == player2 and player1 == 'ataque':
      print('Aniquilacao mutua')
    elif player1 == player2 and player1 == 'papel':
      print('Ambos venceram')
    elif player1 == player2 and player1 == 'pedra':
      print('Sem ganhador')
    elif player1 == 'ataque' or (player1 == 'pedra' and player2 == 'papel'):
      print('Jogador 1 venceu')
    else:
      print('Jogador 2 venceu')

if __name__ == '__main__':
  main()