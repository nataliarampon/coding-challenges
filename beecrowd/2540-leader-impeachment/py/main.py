def main():
  while True:
    try:
      total = int(input())
      votes = sum(list(map(int, input().split())))
      if votes >= 2*total/3:
        print('impeachment')
      else:
        print('acusacao arquivada')
    except EOFError:
      break

if __name__ == "__main__":
  main()