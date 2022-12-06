from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = []
        for line in input_file:
            elf_1, elf_2 = line.strip().split(',')
            input.append([
                        [int(s) for s in elf_1.split('-')],
                        [int(s) for s in elf_2.split('-')]
                        ])
    return input

def part_1(input: List) -> int:
    ans = 0
    num_contained = 0
    for elf_1, elf_2 in input:
        if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]:
            num_contained += 1
        elif elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]:
            num_contained += 1

    ans = num_contained
    return ans

def part_2(input: List) -> int:
    ans = 0
    num_overlap = 0
    for elf_1, elf_2 in input:
        if elf_1[0] >= elf_2[0] and elf_1[0] <= elf_2[1]:
            num_overlap += 1
        elif elf_2[0] >= elf_1[0] and elf_2[0] <= elf_1[1]:
            num_overlap += 1

    ans = num_overlap
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
