def main():
  diameter = int(input())
  depth, length, height = map(int, input().split())
  print('S' if depth >= diameter and length >= diameter and height >= diameter else 'N')

if __name__ == "__main__":
  main()