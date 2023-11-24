import sys
from collections import deque
import re
from typing import List, Tuple


# https://adventofcode.com/2022/day/5

def parse_stacks_moves(instructions: List[str]) -> Tuple[List[deque], List[List[int]]]: 
    """
        parse input using the following logic

        - 3 spaces per entry and 8 spaces between the 9 entries
        - first 9 rows depict items
        - 10th row indicates stack number
        - instructions from row 11

    """

    stacks = [deque() for _ in range(10)]
    
    # parse input stacks
    for i in range(8):
        # read 9 input values per line
        # entries at 1, 5, 9... are the values
        line = instructions[i]
        vals = ['' if line[j] == ' ' else line[j] for j in range(1, len(line), 4)]
        assert (len(vals) == 9)

        for stack, val in zip(stacks[1:], vals):
            if val != '':
                stack.appendleft(val)
        
    
    # parse moves
    moves = [ tuple(int(s) for s in re.findall('\d+', instructions[i])) for i in range(10, len(instructions)) ]
    return stacks, moves

if __name__ == "__main__":
    file_name = sys.argv[1]
    instructions = []
    with open(file_name, 'r') as file:
        instructions = file.read().strip('\n').split('\n')

    stacks, moves = parse_stacks_moves(instructions)

    for count, f_st, to_st in moves:
        for _ in range(count):
            item = stacks[f_st].pop()
            stacks[to_st].append(item)
    
    print (''.join(stack[-1] for stack in stacks[1:]))





    



