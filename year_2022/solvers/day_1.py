from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = []
    return input

def part_1(input: List) -> int:
    ans = 0
    return ans

def part_2(input: List) -> int:
    ans = 0
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
