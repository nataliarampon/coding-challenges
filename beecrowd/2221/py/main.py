def power(atk, defe, bonus):
  return (atk + defe)/2 + bonus

def main():
  cases = int(input())
  for _ in range(cases):
    bonus = int(input())
    atk, defe, lvl = map(int, input().split())
    atk_dabriel, defe_dabriel, lvl_dabriel = map(int, input().split())
    pow_dabriel = power(atk, defe, bonus if lvl % 2 == 0 else 0)
    pow =  power(atk_dabriel, defe_dabriel, bonus if lvl_dabriel % 2 == 0 else 0)
    if (pow > pow_dabriel):
      print('Guarte')
    elif (pow == pow_dabriel):
      print('Empate')
    else:
      print('Dabriel')

if __name__ == "__main__":
    main()