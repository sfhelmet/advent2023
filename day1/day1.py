nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }

def contain_num(string: str):
    for num in nums:
        if num in string:
            return num
        
    return False

# part2
def find_letter_num(string: str):
    left = "" 
    right = ""  
    for i in range(len(string)):
        if string[i].isnumeric():
            left = string[i]
            break
        
        found_letter = contain_num(string[:i + 1])
        if found_letter:
            left = nums[found_letter]
            break

    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            right = string[i]
            break
    
        found_letter = contain_num(string[i:])
        if found_letter:
            right = nums[found_letter]
            break
    
    return int(left + right)

# part1
def find_num(string: str):
    left = ""
    right = ""
    for i in range(len(string)):
        if string[i].isnumeric():
            left = string[i]
            break

    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            right = string[i]
            break

    return int(left + right)

def main():
    with open('day1/day1.txt') as f:
        lines = [line.rstrip() for line in f]

    sum = 0
    for line in lines:
        sum += find_letter_num(line)

    print(sum)

if __name__ == "__main__":
    main()
