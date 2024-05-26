def main():
  while True:
    try:
      pairs = {}
      count = 0
      for _ in range(int(input())):
        number, side = input().split()
        number = int(number)
        if number in pairs:
          if side == 'D' and 'E' in pairs[number]:
            count += 1
            pairs[number].remove('E')
          elif side == 'E' and 'D' in pairs[number]:
            count += 1
            pairs[number].remove('D')
          else:
            pairs[number].append(side)
        else:
          pairs[number] = [side]
      print(count)
    except EOFError:
      break

if __name__ == "__main__":
  main()