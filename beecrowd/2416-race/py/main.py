if __name__ == "__main__":
  distance, course_length = map(int, input().split())
  print(distance % course_length)