def main():
  available_time = int(input())
  time_a, time_b = map(int, input().split())

  if time_a + time_b <= available_time:
    print('Farei hoje!')
  else:
    print('Deixa para amanha!')                                                                                                                                                                                                                                                                          

if __name__ == '__main__':
  main()