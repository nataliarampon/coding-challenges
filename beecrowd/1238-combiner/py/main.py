def main():
  cases = int(input())
  for _ in range(cases):
    str_a, str_b = input().split()
    combined_str = ''

    i = 0
    while i < len(str_a) and i < len(str_b):
      combined_str += str_a[i]
      combined_str += str_b[i]
      i += 1
    
    if len(str_a) > i:
      combined_str += str_a[i:]
    if len(str_b) > i:
      combined_str += str_b[i:]
    
    print(combined_str)

if __name__ == '__main__':
  main()