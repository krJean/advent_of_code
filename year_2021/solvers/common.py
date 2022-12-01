import os

def get_input_path(day: int, input_type: str) -> str:
    root_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(root_path, f'../inputs/day_{day}_{input_type}.txt')
    return input_path