def main():
  mapping = {
    0 : 'PROXYCITY',
    1 : 'P.Y.N.G.',
    2 : 'DNSUEY!',
    3 : 'SERVERS',
    4 : 'HOST!',
    5 : 'CRIPTONIZE',
    6 : 'OFFLINE DAY',
    7 : 'SALT',
    8 : 'ANSWER!',
    9 : 'RAR?',
    10: 'WIFI ANTENNAS'
  }
  for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    print(mapping[num1+num2])

if __name__ == "__main__":
  main()