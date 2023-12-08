def find_symbol(x, y) -> bool:
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if i >= 0 and i < len(map) and j >= 0 and j < len(map[0]):
        if map[i][j] == "*":
          return (i, j)
  
  if y < len(map[0]) - 1 and map[x][y + 1].isnumeric():
    return find_symbol(x, y + 1)
  
  return False

def calcuate_part() -> int:
  sum = 0
  for i in range(len(map)):
    j = 0
    while j < len(map[0]):
      if map[i][j].isnumeric():
        if coord := find_symbol(i, j):
          num = ""
          while j < len(map[0]) and map[i][j].isnumeric():
            num += map[i][j]
            j += 1
          print(num)
          gear_count[coord] = gear_count.get(coord, 0) + 1
          gear_ratio[coord] = gear_ratio.get(coord, 1) * int(num)

      j += 1
          
  return sum

def main():
  global map
  global gear_count
  global gear_ratio
  
  map = []
  with open('day3/day3.txt') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    map.append(line)

  # map = [
  #   "467..114..",
  #   "...*......",
  #   "..35..633.",
  #   "......#...",
  #   "617*......",
  #   ".....+.58.",
  #   "..592.....",
  #   "......755.",
  #   "...$.*....",
  #   ".664.598..",
  # ]
  
  gear_count = {}
  gear_ratio = {}
  print(calcuate_part())

  total = 0
  print(gear_count)
  print(gear_ratio)
  for key in gear_count:
    if gear_count[key] == 2:
      total += gear_ratio[key]
  print(total)

if __name__ == "__main__":
  main()