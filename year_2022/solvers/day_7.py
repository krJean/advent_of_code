from typing import List
from .common import get_input_path

def read_input(input_type: str) -> List[str]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    with open(input_path, 'r') as input_file:
        input = [line.strip() for line in input_file]
    return input

class FileTree:
    def __init__(self):
        self.file_tree = {'/':{'size': 0}}

    def _traverse(self, path: List[str], file_size=0) -> dict:
        temp_tree = self.file_tree[path[0]]
        temp_tree['size'] += file_size
        if len(path) > 1:
            for directory in path[1:]:
                temp_tree = temp_tree[directory]
                temp_tree['size'] += file_size
        return temp_tree

    def insert_dir(self, new_dir: str, path: List[str]) -> None:
        temp_tree = self._traverse(path)
        temp_tree[new_dir] = {'size': 0}

    def insert_file(self, filename: str, size: int, path: List[str]) -> None:
        temp_tree = self._traverse(path, size)
        temp_tree[filename] = {'size': size}

    def print_tree(self):
        print(self.file_tree)

def build_file_tree(input: List[str], ft: FileTree):
    cwd = ['/']
    input.pop(0)

    while len(input) != 0:
        cmd = input.pop(0).split()
        if cmd[1] == 'ls':
            while input and input[0][0] != '$':
                ls_line = input.pop(0).split()
                if ls_line[0] == 'dir':
                    ft.insert_dir(ls_line[1], cwd)
                else:
                    ft.insert_file(ls_line[1], int(ls_line[0]), cwd)
        else:
            if cmd[2] == '..':
                cwd.pop()
            else:
                cwd.append(cmd[2])


def part_1(input: List[str]) -> int:
    ans = 0

    max_size = 100000
    file_tree = FileTree()
    build_file_tree(input, file_tree)

    # i hate to recurse
    def find_small_dir(ft):
        keys = ft.keys()
        local_sum = 0
        if len(keys) != 1:
            for key in ft.keys():
                if key == 'size':
                    if ft[key] <= max_size:
                        local_sum += ft[key]
                else:
                    local_sum += find_small_dir(ft[key])
        return local_sum

    ans = find_small_dir(file_tree.file_tree['/'])
    return ans

def part_2(input: List[str]) -> int:
    ans = 0

    # given
    total_space = 70000000
    total_space_needed = 30000000

    file_tree = FileTree()
    build_file_tree(input, file_tree)

    best_dir_size = float('inf')
    curr_space_available = total_space - file_tree.file_tree['/']['size']
    min_space_to_reallocate = total_space_needed - curr_space_available

    # recursion hates me back
    def find_small_dir(ft):
        nonlocal best_dir_size
        keys = ft.keys()
        local_sum = 0
        if len(keys) != 1:
            for key in ft.keys():
                if key == 'size':
                    if ft[key] >= min_space_to_reallocate and ft[key] < best_dir_size:
                        best_dir_size = ft[key]
                else:
                    find_small_dir(ft[key])
        return local_sum

    find_small_dir(file_tree.file_tree['/'])

    ans = best_dir_size
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
