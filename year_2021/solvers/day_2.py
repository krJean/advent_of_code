from typing import List, Tuple
from .common import get_input_path

def read_input(input_type: str) -> List[Tuple[str,int]]:
    input_path = get_input_path(2, input_type)
    with open(input_path, 'r') as input_file:
        # i love to comprehend lists
        input = [(line.rstrip().split()[0], int(line.rstrip().split()[1])) for line in input_file]
    return input

def part_1(input: List[Tuple[str,int]]) -> int:
    ans = 0
    depth = 0
    dist = 0    # horizontal distance
    for command, value in input:
        match command:
            case 'forward':
                dist += value
            case 'down':
                depth += value
            case 'up':
                depth -= value
            case _:
                print('uh oh')
    ans = depth * dist
    return ans

def part_2(input: List[Tuple[str,int]]) -> int:
    ans = 0
    depth = 0
    dist = 0    # horizontal distance
    aim = 0
    for command, value in input:
        match command:
            case 'forward':
                dist += value
                depth += (aim * value)
            case 'down':
                aim += value
            case 'up':
                aim -= value
            case _:
                print('uh oh')
    ans = depth * dist
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
