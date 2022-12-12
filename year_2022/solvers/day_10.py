from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [line.rstrip().split() for line in input_file]
    return input

def part_1(input: List[List]) -> int:
    ans = 0

    x_reg = 1
    cycle = 0
    signal_counter = 20
    signal_sum = 0

    for command in input:
        if len(command) == 1:
            cycle += 1
            if cycle >= signal_counter:
                signal_sum += (x_reg*signal_counter)
                signal_counter += 40
        else:
            cycle += 2
            if cycle >= signal_counter:
                signal_sum += (x_reg*signal_counter)
                signal_counter += 40
            x_reg += int(command[1])
        if signal_counter > 220:
            break

    ans = signal_sum
    return ans

def part_2(input: List[List]) -> int:
    screen = np.full((6,40), '.')

    x_reg = 1
    cycle = 0

    def on_sprite() -> bool:
        crt_h = cycle % 40
        return crt_h in [x_reg-1,x_reg,x_reg+1]

    for command in input:
        if on_sprite():
            screen[cycle//40][cycle%40] = '#'
        if len(command) == 1:
            cycle += 1
        else:
            cycle += 1
            if on_sprite():
                screen[cycle//40][cycle%40] = '#'
            cycle += 1
            x_reg += int(command[1])

    ret_str = ''
    for line in screen:
        ret_str+= ''.join(line)
        ret_str+='\n'
    ans = ret_str[:-1]
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
