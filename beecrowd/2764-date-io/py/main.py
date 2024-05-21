from datetime import datetime

def main():
  date = datetime.strptime(input(),'%d/%m/%y')
  print(date.strftime('%m/%d/%y'))
  print(date.strftime('%y/%m/%d'))
  print(date.strftime('%d-%m-%y'))

if __name__ == '__main__':
  main()