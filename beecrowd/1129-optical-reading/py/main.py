if __name__ == '__main__':
  mapping = ['A', 'B', 'C', 'D', 'E']
  while True:
    cases = int(input())
  
    if cases == 0:
      break
    
    for _ in range(cases):
      filled_choices = []
      alternatives = list(map(int, input().split()))
      for i, choice in enumerate(alternatives):
        if choice <= 127:
          filled_choices.append(mapping[i])
      if len(filled_choices) != 1:
        print('*')
      else:
        print(filled_choices[0])
