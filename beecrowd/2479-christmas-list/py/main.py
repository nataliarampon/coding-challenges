def main():
  total = int(input())
  children = []
  naughty = 0
  for _ in range(total):
    status, name = input().split()
    children.append(name)
    if status == '-':
      naughty += 1
  children.sort()
  for name in children:
    print(name)
  print(f'Se comportaram: {total - naughty} | Nao se comportaram: {naughty}')

if __name__ == "__main__":
  main()