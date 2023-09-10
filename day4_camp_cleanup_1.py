import sys
from typing import List


# https://adventofcode.com/2022/day/4#part1
if __name__ == "__main__":
    file_name = sys.argv[1]
    sections = []
    with open(file_name, 'r') as file:
        sections = file.read().strip('\n').split('\n')

    get_interval = lambda s: ( [int(ch) for ch in s[0].split('-')] , [int(ch) for ch in s[1].split('-')] )
    is_contained = lambda first_interval, second_interval: second_interval[0] <= first_interval[0] <= second_interval[1] and second_interval[0] <= first_interval[1] <= second_interval[1]

    count = 0
    for section in sections:
        first_interval, second_interval = get_interval( section.split(',') )
        count = count + 1 if is_contained(first_interval, second_interval) or is_contained(second_interval, first_interval) else count
    
    print (f'count = {count}') 

