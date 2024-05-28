def main():
  a = input()
  b = input()
  c = input()

  print(f'A = {a}, B = {b}, C = {c}')
  print(f'A = {b}, B = {c}, C = {a}')
  print(f'A = {c}, B = {a}, C = {b}')

if __name__ == "__main__":
  main()