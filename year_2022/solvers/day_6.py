from typing import List, Tuple
from .common import get_input_path

def read_input(input_type: str) -> List[str]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [c for c in input_file.readline().strip()]
    return input

def part_1(input: List[str]) -> str:
    ans = 0
    pkt_idx = 0
    for i in range(0, len(input)-4):
        if len(set(input[i:i+4])) == 4:
            pkt_idx = i+4
            break
    ans = pkt_idx
    return ans

def part_2(input: List[str]) -> int:
    ans = 0
    msg_idx = 0
    for i in range(0, len(input)-14):
        if len(set(input[i:i+14])) == 14:
            msg_idx = i+14
            break
    ans = msg_idx
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
