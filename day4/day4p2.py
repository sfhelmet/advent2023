def find_card_value(winning, own):
  count = 0

  for num in [int(x) for x in winning]:
    if num in [int(x) for x in own]:
      count += 1

  return count

def calculate_points():
  for i in range(len(cards)):
    card_num, numbers = cards[i].split(":")
    winning, own = numbers.split("|")
    val = find_card_value(winning.split(), own.split())
    for j in range(i + 1, i + val + 1):
      card_count[j] += 1 * card_count[i]

  return None

def main():
  global cards
  global card_count

  card_count = [1 for x in range(197)]

  # cards = [
  #   "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
  #   "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
  #   "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
  #   "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
  #   "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
  #   "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
  # ]
  cards = []
  with open('day4/day4.txt') as f:
    lines = [line.rstrip() for line in f]

  for line in lines:
    cards.append(line)
  calculate_points()
  print(card_count)
  print(sum(card_count))

if __name__ == "__main__":
  main()