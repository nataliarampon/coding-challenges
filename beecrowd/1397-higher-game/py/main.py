def main():
  while True:
    matches = int(input())
    if matches == 0:
      break
    
    points = [0,0]
    for _ in range(matches):
      first_player, second_player = map(int, input().split())
      if first_player > second_player:
        points[0] += 1
      if first_player < second_player:
        points[1] += 1

    print('{} {}'.format(points[0], points[1]))

if __name__ == '__main__':
  main()