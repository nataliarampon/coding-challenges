def main():
  n_str = input()
  n = float(n_str)
  print(f"{'+' if n_str[0] != '-' else ''}{n:.4E}")

if __name__ == '__main__':
  main()