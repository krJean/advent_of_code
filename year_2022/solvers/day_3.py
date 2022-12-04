from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [[c for c in line.strip()] for line in input_file]
    return input

def part_1(input: List) -> int:
    ans = 0
    total_priority = 0
    for rucksack in input:
        comp_1 = set(rucksack[:len(rucksack)//2])
        comp_2 = set(rucksack[len(rucksack)//2:])
        common = ord(comp_1.intersection(comp_2).pop())
        if common < 91:
            total_priority += (common - 38) # ascii difference from 'A' to 27
        else:
            total_priority += (common - 96) # ascii difference from 'a' to 1
    ans = total_priority
    return ans

def part_2(input: List) -> int:
    ans = 0
    total_priority = 0
    for i in range(0,len(input), 3):
        elf_1 = set(input[i])
        elf_2 = set(input[i+1])
        elf_3 = set(input[i+2])
        common = ord(elf_1.intersection(elf_2.intersection(elf_3)).pop())
        if common < 91:
            total_priority += (common - 38) # ascii difference from 'A' to 27
        else:
            total_priority += (common - 96) # ascii difference from 'a' to 1
    ans = total_priority
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
