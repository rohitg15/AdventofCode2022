import sys

# X - lose
# Y - draw
# Z - win

# shape score + win/lose/draw score
round_score = {
    'A' : ( 
        3 + 0,  # Rock - X (Scissor)
        1 + 3,  # Rock - Y (Rock)
        2 + 6   # Rock - Z (paper)
    ),
    'B' : (
        1 + 0,  # Paper - X (Rock)
        2 + 3,  # Paper - Y (Paper)
        3 + 6   # Paper - Z (Scissor)
    ),
    'C':  (
        2 + 0,  # Scissor - X (Paper)
        3 + 3,  # Scissor - Y (Scissor)
        1 + 6   # Scissor - Z (Rock)
    )
}

# day2 - part 2 aoc 2022 https://adventofcode.com/2022/day/2#part2
if __name__ == "__main__":
    input_file = sys.argv[1]
    rounds = []
    with open(input_file, 'r') as file:
        rounds = file.read().strip('\n').split('\n')
    
    score = 0
    for round in rounds:
        elf_choice, my_choice = round.split(' ')
        my_index = ord( my_choice ) - ord( 'X' )
        score += round_score[ elf_choice ][ my_index ]
    
    print (score)
    
