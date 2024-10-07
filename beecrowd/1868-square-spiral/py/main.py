def printFrame(frame, size):
  for i in range(size):
    print(''.join(frame[i]))
  print('@')

def step(direction_index, spiral_point):
  if direction_index % 4 == 0: # RIGHT
    spiral_point[1] = spiral_point[1] + 1
  if direction_index % 4 == 1: # UP
    spiral_point[0] = spiral_point[0] - 1
  if direction_index % 4 == 2: # LEFT
    spiral_point[1] = spiral_point[1] - 1
  if direction_index % 4 == 3: # DOWN
    spiral_point[0] = spiral_point[0] + 1

def main():
  while True:
    size = int(input())
    if size == 0:
      break

    frame = [ ['O' for _ in range(size)] for _ in range(size)]
    spiral_point = [size//2,size//2]
    frame[spiral_point[0]][spiral_point[1]] = 'X'

    i = 1
    step_size = 1
    nb_frames = size**2
    direction_index = 0

    printFrame(frame, size)
    while i < nb_frames:
      for _ in range(step_size):
        if i == nb_frames:
          break
        frame[spiral_point[0]][spiral_point[1]] = 'O'
        step(direction_index, spiral_point)
        frame[spiral_point[0]][spiral_point[1]] = 'X'
        printFrame(frame, size)
        i += 1
      direction_index += 1
      if direction_index % 4 == 2 or direction_index % 4 == 0:
        step_size += 1
      
if __name__ == "__main__":
   main()