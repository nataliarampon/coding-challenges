if __name__ == "__main__":
  tabs, actions = map(int, input().split())
  for _ in range(actions):
    action = input()
    if action == "fechou":
      tabs += 1
    else:
      tabs -= 1
  print(tabs)