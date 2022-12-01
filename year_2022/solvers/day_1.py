from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [line.rstrip() for line in input_file]
    return input

def part_1(input: List) -> int:
    ans = 0
    current_total = 0
    for cal in input:
        if cal == '':
            ans = max(ans, current_total)
            current_total = 0
        else:
            current_total += int(cal)
    return ans

def part_2(input: List) -> int:
    ans = 0
    totals = []
    current_total = 0
    for cal in input:
        if cal == '':
            totals.append(current_total)
            current_total = 0
        else:
            current_total += int(cal)
    totals.append(current_total)
    totals.sort(reverse=True)

    ans = sum(totals[0:3])
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
