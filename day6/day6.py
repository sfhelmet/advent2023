def find_boat_chance(times, distances):
  left = 0
  right = 0
  for time in range(times):
    if time * (times - time) > distances:
      left = time
      break

  for time in range(times -1, -1, -1):
    if time * (times - time) > distances:
      right = time
      break
    

  print(left, right)
  return right - left + 1

def calculate_points(times, distances):
  total = 1
  for i in range(len(times)):
    total *= find_boat_chance(times[i], distances[i])

  return total

def main():
  times = [49, 78, 79, 80]
  distances = [298, 1185, 1066, 1181]

  print(calculate_points(times, distances))

if __name__ == "__main__":
  main()