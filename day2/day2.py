colors = {"red": 12, "green": 13, "blue": 14}


def valid_set(set: str):
    draws = set.split(',')
    for draw in draws:
        num, color = draw.split()
        if int(num) > colors[color]:
            return False
    
    return True

def valid_game(game: str):
    sets = game.split(";")
    for set in sets:
        if not valid_set(set):
            return False
    
    return True
        
def parse_game(string: str):
    game = string.split(":")
    id = game[0].split()[1].strip()
    if valid_game(game[1]):
        return int(id)
    return 0

def main():
    with open('day2/day2.txt') as f:
        lines = [line.rstrip() for line in f]

    sum = 0
    for line in lines:
        sum += parse_game(line)

    print(sum)

if __name__ == "__main__":
    main()