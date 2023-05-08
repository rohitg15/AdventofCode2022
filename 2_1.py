import sys

shape_score = (
    1,  # Rock
    2,  # Paper
    3   # Scissor
)

outcome = {
    'A' : ( 
        3,  # Rock - Rock 
        6,  # Rock - Paper
        0   # Rock -Scissor
    ),
    'B' : (
        0,  # Paper - Rock
        3,  # Paper - Paper
        6   # Paper - Scissor
    ),
    'C':  (
        6,  # Scissor - Rock
        0,  # Scissor - Paper
        3   # Scissor - Scissor
    )
}

# day2 - part 1 aoc 2022 https://adventofcode.com/2022/day/2
if __name__ == "__main__":
    input_file = sys.argv[1]
    rounds = []
    with open(input_file, 'r') as file:
        rounds = file.read().strip('\n').split('\n')
    
    score = 0
    for round in rounds:
        elf_choice, my_choice = round.split(' ')
        my_index = ord( my_choice ) - ord( 'X' )
        score += shape_score[ my_index ] + outcome[ elf_choice ][ my_index ]
    
    print (score)
    
