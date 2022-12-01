from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List[int]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [[int(d) for d in line.rstrip()] for line in input_file]
    return input

def part_1(input: List[List[int]]) -> int:
    ans = 0
    num_inputs = len(input)
    num_bits = len(input[0])

    # Convert to np array for some fun
    input_np = np.array(input)

    # Count all 1 bits in each position by summing the columns
    bit_1_counts = input_np.sum(axis=0)

    # Count all 0 bits by subtracting the 1 count from the length of a column
    # For example, if there are 12 numbers and 7 of them are 1s, then 5 are 0s.
    bit_0_counts = np.subtract(num_inputs, bit_1_counts)

    # Assign 1 or 0 to each bit position dependent on whatever the prompt says
    # about most or least common bits
    gamma_bits = (bit_1_counts > bit_0_counts).astype('int')
    epsilon_bits = (bit_1_counts < bit_0_counts).astype('int')

    # Fun way to convert list of bits to int
    gamma = gamma_bits.dot(1 << np.arange(num_bits-1,-1,-1))
    epsilon = epsilon_bits.dot(1 << np.arange(num_bits-1,-1,-1))

    ans = gamma*epsilon
    return ans

def part_2(input: List[List[int]]) -> int:
    ans = 0

    num_bits = len(input[0])

    oxy = np.array(input)
    co2 = np.array(input)

    # IDK how to explain the rules this code follows
    # But the list of numbers is getting pared down to one
    for i in range(0, num_bits):
        # Counts of bits as above
        oxy_bit_1_counts = oxy.sum(axis=0)
        oxy_bit_0_counts = np.subtract(len(oxy), oxy_bit_1_counts)
        # Figure out which bit is most common at current position
        oxy_max_bit = int(oxy_bit_1_counts[i] >= oxy_bit_0_counts[i])
        # Keep numbers that have that bit at this position
        oxy = oxy[oxy[:,i] == oxy_max_bit]
        if len(oxy) == 1: break

    for i in range(0, num_bits):
        co2_bit_1_counts = co2.sum(axis=0)
        co2_bit_0_counts = np.subtract(len(co2), co2_bit_1_counts)
        # Same as above but least common
        co2_min_bit = int(co2_bit_1_counts[i] < co2_bit_0_counts[i])
        co2 = co2[co2[:,i] == co2_min_bit]
        if len(co2) == 1: break

    # Turn that list of bits into an int
    oxy_int = oxy.dot(1 << np.arange(num_bits-1,-1,-1))
    co2_int = co2.dot(1 << np.arange(num_bits-1,-1,-1))

    ans = int(oxy_int * co2_int)
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
