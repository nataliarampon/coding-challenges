# -*- coding: utf-8 -*-

def calculateFeynman(sides):
  result = 0
  for i in range(sides):
    result += (i+1)**2
  return result

if __name__ == '__main__':
  while True:
    sides = int(input())
    if sides == 0:
      break
    print(calculateFeynman(sides))