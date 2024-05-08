if __name__ == '__main__':
  priceTable = {
    1001: 1.5,
    1002: 2.5,
    1003: 3.5,
    1004: 4.5,
    1005: 5.5
  }

  itens = int(input())
  total = 0
  for _ in range(itens):
    product, quantity = map(int, input().split())
    total += priceTable[product] * quantity
  print("{:.2f}".format(total))