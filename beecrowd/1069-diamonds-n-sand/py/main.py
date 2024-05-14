def main():
  cases = int(input())
  for _ in range(cases):
    place = input()
    stack = ['.']
    diamonds = 0
    for c in place:
      if c == '<':
        stack.append(c)
      if c == '>' and stack[-1] == '<':
        diamonds += 1
        stack.pop()
    print(diamonds)

if __name__ == '__main__':
  main()