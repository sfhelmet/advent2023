colors = {"red": 12, "green": 13, "blue": 14}


def read_set(set: str):
    red = 0
    blue = 0
    green = 0
    draws = set.split(',')
    for draw in draws:
        num, color = draw.split()
        if color == "red":
            red += int(num)
        elif color == "blue":
            blue += int(num)
        elif color == "green":
            green += int(num)
        
    return red, blue, green

def find_game_power(game: str):
    sets = game.split(";")
    red_max = 0
    blue_max = 0
    green_max = 0
    for set in sets:
        red, blue, green = read_set(set)
        red_max = max(red_max, red)
        blue_max = max(blue_max, blue)
        green_max = max(green_max, green)
    
    return red_max * blue_max * green_max
        
def parse_game(string: str):
    game = string.split(":")
    return find_game_power(game[1])

def main():
    with open('day2/day2.txt') as f:
        lines = [line.rstrip() for line in f]

    sum = 0
    for line in lines:
        sum += parse_game(line)

    print(sum)

if __name__ == "__main__":
    main()