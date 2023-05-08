import sys

# day 1 - part 1 aoc2022 https://adventofcode.com/2022/day/1
if __name__ == "__main__":
    input_file = sys.argv[1]
    lines = []
    with open(input_file, "r") as file:
        lines = file.read().strip('\n').split('\n\n')
    
    elf_calories_cumulative = [ sum( ( int(elf_calories, 10) for elf_calories in line.split('\n') ) ) for line in lines ]

    print ( max(elf_calories_cumulative) )
    

