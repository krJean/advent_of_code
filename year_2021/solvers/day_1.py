from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List[int]:
    input_path = get_input_path(1, input_type)
    with open(input_path, 'r') as input_file:
        input = [int(line.rstrip()) for line in input_file]
    return input

def part_1(input: List[int]) -> int:
    ans = 0
    for i in range(1,len(input)):
        ans += input[i] > input[i-1]
    return ans

def part_2(input: List[int]) -> int:
    ans = 0
    for i in range(3,len(input)):
        # Sum three consecutive ints
        sum_1 = sum(input[i-3:i])
        # Sum next three consecutive ints
        sum_2 = sum(input[i-2:i+1])
        # If the sum has increased, tally it
        ans += sum_2 > sum_1
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
