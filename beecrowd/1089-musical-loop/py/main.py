def isLocalMinOrMax(before, value, after):
  return (value > before and value > after) or (value < before and value < after)

def main():
  while True:
    length = int(input())
    if length == 0:
      break
    
    pcm = list(map(int, input().split())) 
    peakCount = 0

    for i in range(0, length):
      if isLocalMinOrMax(pcm[i-1], pcm[i], pcm[(i+1)%length]):
        peakCount += 1
    
    print(peakCount)

if __name__ == '__main__':
  main()