from typing import List
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> List[List]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    input = []
    with open(input_path, 'r') as input_file:
        for line in input_file:
            unique_signals, output_digits = line.strip().split('|')
            input.append([unique_signals.split(), output_digits.split()])
    return input

def part_1(input: List[List]) -> int:
    ans = 0
    easy_digit_count = 0 # 1, 4, 7, 8
    for _, output_digits in input:
        for digit in output_digits:
            if len(digit) in [2,3,4,7]:
                easy_digit_count += 1
    ans = easy_digit_count
    return ans

def part_2(input: List[List]) -> int:
    ans = 0
    output_sum = 0

    for unique_signals, output_digits in input:
        # map from known wires to unknown wires
        wire_map = {chr(c):'-' for c in range(ord('a'), ord('g')+1)}
        found_digits = [''] * 10
        # unique signals from input with the chars of each digit sorted
        unique_signals = [''.join(sorted(digit)) for digit in unique_signals]
        # output digits from input with the chars of digit sorted
        output_digits = [''.join(sorted(digit)) for digit in output_digits]
        # output number as an int
        output_number = 0

        i = 0
        # boolean to let the loop break when the four easy digits have been found
        initial_sweep = True
        while initial_sweep:
            digit = unique_signals[i]
            hit_match = True
            match len(unique_signals[i]):
                case 2:
                    found_digits[1] = digit
                case 4:
                    found_digits[4] = digit
                case 3:
                    found_digits[7] = digit
                case 7:
                    found_digits[8] = digit
                case _:
                    hit_match = False
            if hit_match:
                unique_signals.pop(i)
            else:
                i+= 1
            initial_sweep = not len(unique_signals) == 6

        def find_number_and_wire(wire_map_key, temp_digit_str):
            nonlocal unique_signals
            nonlocal wire_map
            final_digit_str = ''
            for i, digit in enumerate(unique_signals):
                if len(digit) == len(temp_digit_str)+1:
                    temp_wire = digit.translate(dict.fromkeys(map(ord, temp_digit_str)))
                    if len(temp_wire) == 1:
                        wire_map[wire_map_key] = temp_wire
                        final_digit_str = unique_signals.pop(i)
                        break
            return final_digit_str


        # 'a' is the only wire that seven doesn't share with one
        wire_map['a'] = found_digits[7].translate(dict.fromkeys(map(ord, found_digits[1])))

        # four plus the 'a' wire gets all but the 'g' wire for digit nine
        # get nine and 'g' wire here
        temp_nine = ''.join(sorted(found_digits[4]+wire_map['a']))
        found_digits[9] = find_number_and_wire('g', temp_nine)

        # the only wire nine doesn't use is 'e'
        for c in ['a','b','c','d','e','f','g']:
            if c not in found_digits[9]:
                wire_map['e'] = c

        # seven plus the 'g' wire gets all but the 'd' wire for digit three
        # get three and 'd' wire here
        temp_three = ''.join(sorted(found_digits[7]+wire_map['g']))
        found_digits[3] = find_number_and_wire('d', temp_three)

        # wire_map has all but one wire to make digit two
        # get two and 'c' wire here
        temp_two = ''.join(sorted(wire_map['a']+wire_map['d']+wire_map['e']+wire_map['g']))
        found_digits[2] = find_number_and_wire('c', temp_two)

        wire_map['f'] = found_digits[1].translate(dict.fromkeys(map(ord, wire_map['c'])))
        wire_map['b'] = found_digits[4].translate(dict.fromkeys(map(ord, wire_map['d']+wire_map['c']+wire_map['f'])))

        found_digits[0] = ''.join(sorted([wire_map[c] for c in 'abcefg']))
        found_digits[5] = ''.join(sorted([wire_map[c] for c in 'abdfg']))
        found_digits[6] = ''.join(sorted([wire_map[c] for c in 'abdefg']))

        for output_idx, output_digit in enumerate(output_digits):
            digit_idx = found_digits.index(output_digit)
            output_number += digit_idx*(10**(3-output_idx))

        output_sum += output_number

    ans = output_sum
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
