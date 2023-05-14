import sys
from functools import reduce

# day 3 part 2 - aoc 2022 https://adventofcode.com/2022/day/3#part2
if __name__ == "__main__":
    file_name = sys.argv[1]
    rucksacks = []
    with open(file_name, 'r') as file:
        rucksacks = file.read().strip('\n').split('\n')

    group_size = 3
    groups = [ rucksacks[i * group_size: (i + 1) * group_size ] for i in range( len(rucksacks) // 3 ) ]

    def calc_priority(common_set: set) -> int:
        priority = 0
        for ch in common_set:
            priority += 1 + ord(ch) - ord('a') if ch.islower() else 27 + ord(ch) - ord('A')
        return priority

    common_sets = [ set.intersection( set(group[0]), set(group[1]), set(group[2]) ) for group in groups]
    count = sum( map( calc_priority, common_sets ) )
    print (count)

