from collections import Counter

def main():
  while True:
    n, m = input().split()
    if n == '0' and m == '0':
      break
    tickets = input().split()
    counter = Counter(tickets)
    false_tickets = 0
    for c in counter.most_common():
      if c[1] > 1:
        false_tickets += 1
      else:
        break
    print(false_tickets)

if __name__ == "__main__":
  main()