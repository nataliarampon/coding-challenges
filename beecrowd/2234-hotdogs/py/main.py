def main():
  hotdogs, people = map(int, input().split())
  print('{:.2f}'.format(hotdogs/people))

if __name__ == '__main__':
  main()