from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = input_file.readline().strip().split(',')
    return input

def part_1(input: List) -> int:
    ans = 0
    num_days = 80
    current_fish = np.array(input,dtype=int)
    for _ in range(num_days):
        new_fish_count = np.sum(current_fish == 0)
        mask = current_fish != 0
        current_fish[mask] -= 1
        current_fish[~mask] = 6
        current_fish = np.concatenate((current_fish, [8]*new_fish_count))

    ans = len(current_fish)
    return ans


# i do not like recursion :(
def make_babies(current_fish: List[int], num_days: List[int]) -> int:
    new_fish_count = 0
    for fish_timer, current_num_days in zip(current_fish, num_days):
        if current_num_days > fish_timer:
            current_num_days -= fish_timer
            new_day_list = list(range(current_num_days, -1, -7))
            new_fish_count += 1 + make_babies([8]*len(new_day_list), new_day_list)
        # else:
        #     new_fish_count += 1
    return new_fish_count


def part_2(input: List) -> int:
    ans = 0
    # num_days = 256
    num_days = 80
    current_fish = np.array(input,dtype=int)
    # breakpoint()
    # instead of looping through days, loop through each fish, make recursive calls to children
    total_fish_count = make_babies(current_fish, [num_days]*len(current_fish))
    # ans = total_fish_count
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
