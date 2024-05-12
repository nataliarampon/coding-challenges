def main():
  plug_a = list(input().split())
  plug_b = list(input().split())

  for i in range(len(plug_a)):
    if plug_a[i] == plug_b[i]:
      print('N')
      return
  print('Y')

if __name__ == '__main__':
  main()