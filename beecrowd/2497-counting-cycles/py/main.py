def main():
  i = 1
  while True:
    steps = int(input())

    if steps == -1:
      break
    
    print('Experiment {}: {} full cycle(s)'.format(i, steps//2))
    i += 1

if __name__ == "__main__":
  main()