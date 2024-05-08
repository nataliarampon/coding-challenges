if __name__ == '__main__':
  cases = int(input())
  for _ in range(cases):
    triangle_lines = int(input())
    sum_lines = 0
    for i in range(triangle_lines):
      sum_lines += 2**i
    print(sum_lines)