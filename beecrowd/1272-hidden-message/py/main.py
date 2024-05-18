def main():
  cases = int(input())
  for _ in range(cases):
    message = input()
    hidden_msg = ""

    for word in list(message.split()):
      hidden_msg += word[0]
    print(hidden_msg)

if __name__ == '__main__':
  main()