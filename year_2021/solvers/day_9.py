from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List[int]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [[int(c) for c in line.strip()] for line in input_file]
    return input

def part_1(input: List[List[int]]) -> int:
    ans = 0
    total_risk_level = 0

    # pad of max height + 1 around the grid so there are less conditionals
    input = np.pad(input, [(1,1),(1,1)], constant_values=10)

    for i in range(1,len(input)-1):
        for j in range(1,len(input[0])-1):
            curr_height = input[i][j]
            adj_heights = [
                input[i-1][j],
                input[i+1][j],
                input[i][j-1],
                input[i][j+1]]
            if min(adj_heights) > curr_height:
                total_risk_level += curr_height+1

    ans = total_risk_level
    return ans

def part_2(input: List[List[int]]) -> int:
    ans = 0
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
