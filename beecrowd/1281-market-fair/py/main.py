def main():
  for _ in range(int(input())):
    nb_products = int(input())
    products = {}
    for _ in range(nb_products):
      name, price = input().split()
      products[name] = float(price)

    nb_buy = int(input())
    total = 0
    for _ in range(nb_buy):
      name, qty = input().split()
      total += products[name]*int(qty)
    
    print(f'R$ {total:.2f}')

if __name__ == '__main__':
  main()