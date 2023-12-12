def valid_right(x, y):
    return x < len(map[0]) and (map[y][x] == 'J' or map[y][x] == '7' or map[y][x] == "-")

def valid_left(x, y):
    return x >= 0 and (map[y][x] == 'L' or map[y][x] == 'F' or map[y][x] == "-")

def valid_down(x, y):
    return y < len(map) and (map[y][x] == 'L' or map[y][x] == 'J' or map[y][x] == "|")

def valid_up(x, y):
    return y >= 0 and (map[y][x] == 'F' or map[y][x] == '7' or map[y][x] == "|")

def move_right(x, y, stack):
    if valid_right(x + 1, y):
        if is_new_path(x + 1, y, min_values[y][x]):
            min_values[y][x + 1] = min_values[y][x] + 1
            stack.append((x + 1, y))

def move_down(x, y, stack):
    if valid_down(x, y + 1):
        if is_new_path(x, y + 1, min_values[y][x]):
            min_values[y + 1][x] = min_values[y][x] + 1
            stack.append((x, y + 1))

def move_left(x, y, stack):
    if valid_left(x - 1, y):
        if is_new_path(x - 1, y, min_values[y][x]):
            min_values[y][x - 1] = min_values[y][x] + 1
            stack.append((x - 1, y))

def move_up(x, y, stack):
    if valid_up(x, y - 1):
        if is_new_path(x, y - 1, min_values[y][x]):
            min_values[y - 1][x] = min_values[y][x] + 1
            stack.append((x, y - 1))

def is_new_path(x, y, count):
    return min_values[y][x] > count + 1 or min_values[y][x] == 0

def traverse(x_start, y_start):
    stack = [(x_start, y_start)]

    while stack:
        x, y = stack.pop()

        if map[y][x] == 'S':
            move_right(x, y, stack)
            move_down(x, y, stack)
            move_left(x, y, stack)
            move_up(x, y, stack)
  
        elif map[y][x] == 'L':
            move_right(x, y, stack)
            move_up(x, y, stack)

        elif map[y][x] == 'F':
            move_right(x, y, stack)
            move_down(x, y, stack)
    
        elif map[y][x] == '7':
            move_left(x, y, stack)
            move_down(x, y, stack)

        elif map[y][x] == 'J':
            move_up(x, y, stack)
            move_left(x, y, stack)

        elif map[y][x] == '-':
            move_right(x, y, stack)
            move_left(x, y, stack)

        elif map[y][x] == '|':
            move_up(x, y, stack)
            move_down(x, y, stack)

def find_further():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                min_values[y][x] = 0
                traverse(x, y)
                return

def traverse_value():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'S':
                min_values[y][x] = 0
                traverse(x, y)

def main():
    global map
    global min_values
    map = []

    with open('day10/day10.txt') as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        map.append([x for x in line])

    min_values = [[0 for x in range(len(map[0]))] for _ in range(len(map))]
    find_further()

    traverse_value()

    count = 0
    for i in range(len(min_values)):
      is_in = False
      temp_count = 0 
      for j in range(len(min_values[0])):
        if is_in:
          if min_values[i][j] == 0:
            temp_count += 1
          else:
            count += temp_count
            temp_count = 0
            is_in = False
        else:
          if min_values[i][j] != 0 and j + 1 < len(map[0]) and min_values[i][j+1] == 0:
            is_in = True
        
    print(count)
    print(min_values)

    with open('day10/day10itep2.txt', 'w') as f:
      for line in min_values:
        f.write(''.join([str(x) for x in line]) + '\n')

if __name__ == "__main__":
    main()
