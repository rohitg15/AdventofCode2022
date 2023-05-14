import sys

# day3 - part 1 aoc 2022 https://adventofcode.com/2022/day/3
if __name__ == "__main__":
    file_name = sys.argv[1]
    rucksacks = []
    with open(file_name, 'r') as file:
        rucksacks = file.read().strip('\n').split('\n')
    
    # priority 'a' - 'z' -> [1...26]
    # priority 'A" - 'Z' -> [27..52]
    calc_priority = lambda ch: 1 + ord(ch) - ord('a') if ch.islower() else 27 + ord(ch) - ord('A')
    sum = 0
    for rucksack in rucksacks:
        l = len(rucksack) // 2
        first, second = set( rucksack[0: l] ), set( rucksack[l: ] )
        for ch in first.intersection(second):
            sum += calc_priority(ch)
    
    print (sum)

