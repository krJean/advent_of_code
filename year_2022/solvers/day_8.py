from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List[int]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [[int(c) for c in line.rstrip()] for line in input_file]
    return input

def part_1(input: List[List[int]]) -> int:
    ans = 0

    visible_grid = np.full_like(input, False)
    max_row = len(input)
    max_col = len(input[0])

    for i in range(max_row):
        max_tree_left = -1
        max_tree_right = -1
        for j in range(max_col):
            if input[i][j] > max_tree_left:
                visible_grid[i][j] = True
                max_tree_left = input[i][j]
            if input[i][-(j+1)] > max_tree_right:
                visible_grid[i][-(j+1)] = True
                max_tree_right = input[i][-(j+1)]

    for j in range(max_col):
        max_tree_up = -1
        max_tree_down = -1
        for i in range(max_row):
            if input[i][j] > max_tree_down:
                visible_grid[i][j] = True
                max_tree_down = input[i][j]
            if input[-(i+1)][j] > max_tree_up:
                visible_grid[-(i+1)][j] = True
                max_tree_up = input[-(i+1)][j]

    ans = np.sum(visible_grid)
    return ans

def part_2(input: List[List[int]]) -> int:
    ans = 0

    input = np.array(input)
    best_tree = 0

    def scan_trees(tree_list, curr_height, reverse=False):
        temp_sum = 0
        if reverse:
            tree_range = range(len(tree_list)-1,-1,-1)
        else:
            tree_range = range(len(tree_list))
        for t in tree_range:
            temp_sum += 1
            if tree_list[t] >= curr_height:
                break

        return temp_sum


    for i in range(1, len(input)-1):
        for j in range(1, len(input[0])-1):
            curr_height = input[i][j]
            left = input[i,:j]
            right = input[i,j+1:]
            up = input[:i,j]
            down = input[i+1:,j]

            prod  = scan_trees(left, curr_height, reverse=True)
            prod *= scan_trees(right, curr_height)
            prod *= scan_trees(up, curr_height, reverse=True)
            prod *= scan_trees(down, curr_height)

            best_tree = max(best_tree, prod)

    ans = best_tree
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
