if __name__ == "__main__":
  MIN_QUANTITY_PHOTONS = 40000000
  telescope_surface = int(input())
  stars = int(input())
  visible_stars = 0
  for i in range(stars):
    star_flow = int(input())
    if (telescope_surface*star_flow >= MIN_QUANTITY_PHOTONS):
      visible_stars += 1
  print(visible_stars)