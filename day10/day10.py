import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)


def valid_right(x, y):
  return x < len(map[0]) and (map[y][x] == 'J' or map[y][x] == '7' or map[y][x] == "-")

def valid_left(x, y):
  return x >= 0 and (map[y][x] == 'L' or map[y][x] == 'F' or map[y][x] == "-")

def valid_down(x, y):
  return y < len(map) and (map[y][x] == 'L' or map[y][x] == 'J' or map[y][x] == "|")

def valid_up(x, y):
  return y >= 0 and (map[y][x] == 'F' or map[y][x] == '7' or map[y][x] == "|")

def move_right(x, y):
  if valid_right(x + 1, y):
    if is_new_path(x + 1, y, min_values[y][x]):
      min_values[y][x+1] = min_values[y][x] + 1
      traverse(x + 1, y)

def move_down(x, y):
  if valid_down(x, y + 1):
    if is_new_path(x, y + 1, min_values[y][x]):
      min_values[y+1][x] = min_values[y][x] + 1
      traverse(x, y + 1)

def move_left(x, y):
  if valid_left(x - 1, y):
    if is_new_path(x - 1, y, min_values[y][x]):
      min_values[y][x-1] = min_values[y][x] + 1
      traverse(x - 1, y)

def move_up(x, y):
  if valid_up(x, y - 1):
    if is_new_path(x, y - 1, min_values[y][x]):
      min_values[y-1][x] = min_values[y][x] + 1
      traverse(x, y - 1)

def is_new_path(x, y, count):
  return min_values[y][x] > count + 1 or min_values[y][x] == 0

def traverse(x, y):
  if map[y][x] == 'S':
    move_right(x, y)
    move_down(x, y)
    move_left(x, y)
    move_up(x, y)
  
  elif map[y][x] == 'L':
    move_right(x, y)
    move_up(x, y)

  elif map[y][x] == 'F':
    move_right(x, y)
    move_down(x, y)
    
  elif map[y][x] == '7':
    move_left(x, y)
    move_down(x, y)

  elif map[y][x] == 'J':
    move_up(x, y)
    move_left(x, y)

  elif map[y][x] == '-':
    move_right(x, y)
    move_left(x, y)

  elif map[y][x] == '|':
    move_up(x, y)
    move_down(x, y)

def find_further():
  for y in range(len(map)):
    for x in range(len(map[0])):
      if map[y][x] == 'S':
        min_values[y][x] = 0
        traverse(x, y)
        break


def main():
  global map
  global min_values
  map = []

  with open('day10/day10.txt') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    map.append([x for x in line])

  min_values = []
  for line in map:
    min_values.append([0 for x in range(len(map[0]))])

  find_further()
  # print(min_values)
  
  maxi = 0
  for line in min_values:
    for value in line:
      if value > maxi:
        maxi = value

  print(maxi)
if __name__ == "__main__":
  main()