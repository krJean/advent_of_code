from typing import List, Tuple
from .common import get_input_path

def read_input(input_type: str) -> Tuple[List[List], List]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        temp_input = [line.strip('\n') for line in input_file]

    split_idx = temp_input.index('')
    stack_count = int(temp_input[split_idx-1].split()[-1])
    stack_array = [[] for _ in range(stack_count)]

    for line_idx in range(split_idx-2, -1, -1):
        for stack in range(0,stack_count):
            stack_idx = stack*4+1
            crate = temp_input[line_idx][stack_idx]
            if crate != ' ':
                stack_array[stack].append(crate)

    commands = []
    for line_idx in range(split_idx+1, len(temp_input)):
        line_list = temp_input[line_idx].split()
        commands.append(
            (int(line_list[1]),
             int(line_list[3]),
             int(line_list[5])))

    return (stack_array, commands)

def part_1(input: Tuple[List[List], List]) -> str:
    ans = 0
    stack_array, commands = input
    for crate_count, src, dst in commands:
        for _ in range(0,crate_count):
            stack_array[dst-1].append(stack_array[src-1].pop())
    ret_str = ''.join([stack[-1] for stack in stack_array])
    ans = ret_str
    return ans

def part_2(input: Tuple[List[List], List]) -> int:
    ans = 0
    stack_array, commands = input
    for crate_count, src, dst in commands:
        stack_array[dst-1] += stack_array[src-1][-crate_count:]
        stack_array[src-1] = stack_array[src-1][0:-crate_count]
    ret_str = ''.join([stack[-1] if stack else '' for stack in stack_array])
    ans = ret_str
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
