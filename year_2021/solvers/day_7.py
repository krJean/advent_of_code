from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List[int]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [int(c) for c in input_file.readline().strip().split(',')]
    return input

def part_1(input: List[int]) -> int:
    ans = 0
    least_fuel = float('inf')

    for pos in range(max(input)+1):
        curr_fuel = 0
        for crab in input:
            curr_fuel += abs(crab-pos)
        least_fuel = min(least_fuel, curr_fuel)

    ans = least_fuel
    return ans

def part_2(input: List[int]) -> int:
    ans = 0
    least_fuel = float('inf')

    for pos in range(max(input)+1):
        curr_fuel = 0
        for crab in input:
            steps = abs(crab-pos)
            curr_fuel += int((steps/2)*(steps+1))
        least_fuel = min(least_fuel, curr_fuel)

    ans = least_fuel
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
