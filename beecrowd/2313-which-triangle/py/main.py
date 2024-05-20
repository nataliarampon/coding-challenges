def isTriangle(a, b, c):
  return a < b + c and b < c + a and c < b + a

def main():
  side = sorted(list(map(int, input().split())))
  type = ''
  rectangle = 'N'
  if isTriangle(side[0], side[1], side[2]):
    if side[0] == side[1] and side[1] == side[2]:
      type = 'Equilatero'
    elif side[0] != side[1] and side[1] != side[2] and side[0] != side[2]:
      type = 'Escaleno'
      if side[0]**2 + side[1] **2 == side[2]**2:
        rectangle = 'S'
    else:
      type = 'Isoceles'
    print(f'Valido-{type}')
    print(f'Retangulo: {rectangle}')
  else:
    print('Invalido')

if __name__ == '__main__':
  main()