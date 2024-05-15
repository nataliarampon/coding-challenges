def main():
  while True:
    length = int(input())
    if length == 0:
      break
    deck = list(range(1, length+1))
    discarded = []
    
    count = 0
    while count < length - 1:
      discarded.append(deck.pop(0))
      deck.append(deck.pop(0))
      count += 1
    print(f"Discarded cards: {str(discarded)[1:-1]}")
    print(f"Remaining card: {deck[0]}")

if __name__ == '__main__':
  main()