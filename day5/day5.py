def map_seed_to_soil(seeds):
    for seed in seeds:
       pass
    

def find_lowest_location(seeds):
    map_seed_to_soil(seeds)

  

    return total

def main():
  global map
  map = []
  seeds = [79, 14, 55, 13]
  lines = [
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
  ]
  
#   with open('day4/day4.txt') as f:
#     lines = [line.rstrip() for line in f]

  for line in lines:
    map.append(line)

  print(find_lowest_location(seeds))

if __name__ == "__main__":
  main()