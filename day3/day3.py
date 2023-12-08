def is_symbol(string):
  return string != "." and not string.isnumeric()

def find_symbol(x, y) -> bool:
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if i >= 0 and i < len(map) and j >= 0 and j < len(map[0]):
        if is_symbol(map[i][j]):
          return True
  
  if y < len(map[0]) - 1 and map[x][y + 1].isnumeric():
    return find_symbol(x, y + 1)
  
  return False

def calcuate_part() -> int:
  sum = 0
  for i in range(len(map)):
    j = 0
    while j < len(map[0]):
      if map[i][j].isnumeric():
        if find_symbol(i, j):
          num = ""
          while j < len(map[0]) and map[i][j].isnumeric():
            num += map[i][j]
            j += 1
          print(num)
          sum += int(num)

      j += 1
          
  return sum

def main():
  global map 
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
  
  map = []
  with open('day3/day3.txt') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    map.append(line)
  
  print(calcuate_part())
  

if __name__ == "__main__":
  main()