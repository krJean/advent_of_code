from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List[List]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    input = []
    with open(input_path, 'r') as input_file:
        # i hate to list comprehend
        for line in input_file:
            point_1_str, point_2_str = line.strip().split(' -> ')
            point_1_list = point_1_str.split(',')
            point_2_list = point_2_str.split(',')
            input.append([
                [int(point_1_list[0]), int(point_1_list[1])],
                [int(point_2_list[0]), int(point_2_list[1])]
                ])
    return input

def part_1(input: List[List[List]]) -> int:
    ans = 0
    input_np = np.array(input)
    max_size = np.max(input_np)+1
    grid = np.zeros((max_size, max_size))
    for point_1, point_2 in input_np:
        x1, y1 = point_1
        x2, y2 = point_2
        if x1 == x2:
            grid[x1,min(y1,y2):max(y1,y2)+1] += 1
        if y1 == y2:
            grid[min(x1,x2):max(x1,x2)+1,y1] += 1
    # print(grid.transpose().astype(int))
    ans = np.sum(grid > 1)
    return ans

def part_2(input: List[List[List]]) -> int:
    ans = 0
    input_np = np.array(input)
    max_size = np.max(input_np)+1
    grid = np.zeros((max_size, max_size))
    for point_1, point_2 in input_np:
        x1, y1 = point_1
        x2, y2 = point_2
        x_min, x_max = (x1, x2) if x1 < x2 else (x2, x1)
        y_min, y_max = (y1, y2) if y1 < y2 else (y2, y1)
        if x1 == x2:
            grid[x1,y_min:y_max+1] += 1
        elif y1 == y2:
            grid[x_min:x_max+1,y1] += 1
        else:
            if x1 < x2:
                x_stride = np.arange(x1,x2+1)
            else:
                x_stride = np.arange(x1,x2-1,-1)
            if y1 < y2:
                y_stride = np.arange(y1,y2+1)
            else:
                y_stride = np.arange(y1,y2-1,-1)
            grid[x_stride,y_stride] += 1
    ans = np.sum(grid > 1)
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
