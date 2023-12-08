def find_card_value(winning, own):
  count = 0

  for num in [int(x) for x in winning]:
    if num in [int(x) for x in own]:
      count += 1

  return pow(2, count - 1) if count != 0 else 0

def calculate_points():
  total = 0
  for card in cards:
    _, numbers = card.split(":")
    winning, own = numbers.split("|")
    total += find_card_value(winning.split(), own.split())

  return total

def main():
  global cards
  cards = []
  
  # cards = [
  #   "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
  #   "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
  #   "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
  #   "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
  #   "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
  #   "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
  # ]
  with open('day4/day4.txt') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    cards.append(line)

  print(calculate_points())

if __name__ == "__main__":
  main()