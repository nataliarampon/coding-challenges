def main():
  length = int(input())
  nums = list(map(int, input().split()))

  min_index = 1
  min_value = nums[0]
  for i in range(length):
    if nums[i] < min_value:
      min_index = i + 1
      min_value = nums[i]
  print(min_index)

if __name__ == '__main__':
  main()
