def main():
  PI = 3.14

  while True:
    try:
      volume = float(input())
      diameter = float(input())
      area = PI*(diameter/2)**2
      height = volume/area

      print('ALTURA = {:.2f}'.format(height))
      print('AREA = {:.2f}'.format(area))

    except EOFError:
      break

if __name__ == '__main__':
  main()