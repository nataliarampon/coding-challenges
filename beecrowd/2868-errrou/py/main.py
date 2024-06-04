import re

def main():
  for _ in range(int(input())):
    matches = re.findall('(\d+) (x|-|\+) (\d+) = (\d+)', input())[0]
    
    if matches[1] == '+':
      res = int(matches[0]) + int(matches[2])
    if matches[1] == '-':
      res = int(matches[0]) - int(matches[2])
    if matches[1] == 'x':
      res = int(matches[0]) * int(matches[2])

    errors = abs(int(matches[3]) - res)
    print(f"E{errors*'r'}ou!")

if __name__ == "__main__":
  main()