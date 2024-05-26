def main():
  beans = map(int, input().split())
  for i, bean in enumerate(beans):
    if bean:
      print(i+1)
      break

if __name__ == "__main__":
  main()