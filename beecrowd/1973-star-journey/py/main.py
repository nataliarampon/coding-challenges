# Use of stdin cause it's faster than input() and it was giving me a time limit error
from sys import stdin

def main():
  nb_stars = int(stdin.readline())
  stars = list(map(int, stdin.readline().split()))
  total_sheep = sum(stars)
  stolen_sheep = i = visited_count = 0
  visited = [False] * nb_stars

  while i >= 0 and i < nb_stars:
    if visited[i] == False:
      visited_count += 1
      visited[i] = True
    if stars[i] > 0:
      stolen_sheep += 1
      stars[i] -= 1
      i = i + ( 1 if (stars[i] + 1) % 2 != 0 else -1)
    else:
      i -= 1
  print(f'{visited_count} {total_sheep - stolen_sheep}')

if __name__ == '__main__':
  main()