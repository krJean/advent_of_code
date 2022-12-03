from typing import List, Tuple
from .common import get_input_path

def read_input(input_type: str) -> List[Tuple[str,str]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [tuple(line.strip().split()) for line in input_file]
    return input

# I was considering converting the chars to ints and really leaning into mathimagic.
# But I think that would be a pain to read in a year.
# This runs just fine.

def part_1(input: List[Tuple[str,str]]) -> int:
    ans = 0
    score = 0

    shape_dict = {
        'A' : {'score' : 1, 'beats' : 'C'},
        'B' : {'score': 2, 'beats' : 'A'},
        'C' : {'score': 3, 'beats' : 'B'},
        'X' : 'A',
        'Y' : 'B',
        'Z' : 'C',
    }

    for round in input:
        their_pick = round[0]
        my_pick = shape_dict[round[1]]

        score += shape_dict[my_pick]['score']
        if their_pick == my_pick:
            score += 3
        elif shape_dict[my_pick]['beats'] == their_pick:
            score += 6

    ans = score
    return ans

def part_2(input: List[Tuple[str,str]]) -> int:
    ans = 0
    score = 0

    shape_dict = {
        'A' : {'score' : 1, 'X' : 'C', 'Y' : 'A', 'Z' : 'B'},
        'B' : {'score' : 2, 'X' : 'A', 'Y' : 'B', 'Z' : 'C'},
        'C' : {'score' : 3, 'X' : 'B', 'Y' : 'C', 'Z' : 'A'},
        'X' : 0,
        'Y' : 3,
        'Z' : 6,
    }

    for round in input:
        # -vvv
        # their_pick = round[0]
        # my_strat = round[1]
        # my_pick = shape_dict[their_pick][my_strat]
        # score += shape_dict[my_pick]['score']
        # score += shape_dict[my_strat]

        my_pick = shape_dict[round[0]][round[1]]
        score += shape_dict[round[1]] + shape_dict[my_pick]['score']

    ans = score
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
