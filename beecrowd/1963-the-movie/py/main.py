def main():
  initial_price, final_price = map(float, input().split())
  percentage_increase = (final_price - initial_price) / initial_price * 100
  print(f'{percentage_increase:.2f}%')

if __name__ == '__main__':
  main()