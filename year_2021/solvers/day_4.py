from typing import List, Tuple
from .common import get_input_path
import numpy as np

def read_input(input_type: str) -> Tuple[List,List[List[List]]]:
    input_path = get_input_path(__name__.split('_')[-1], input_type)
    board_list = []
    current_board = []
    with open(input_path, 'r') as input_file:
        for i, line_unstripped in enumerate(input_file):
            line = line_unstripped.rstrip()

            # Handle the first line, which are the called bingo numbers
            if i == 0:
                number_calls = [int(num) for num in line.split(',')]
            else:
                # If we reach an empty line, it's the end of a board, so add that board to the board list
                # (This isn't true for the first empty line, which is handled by chopping off the first element in the board list)
                if line == '':
                    board_list.append(current_board)
                    current_board = []
                # If it's not an empty line and not the called numbers, it's a line on the board. Add it.
                else:
                    current_board.append([int(num) for num in line.split()])
        # No boards left behind
        board_list.append(current_board)

    # Here's where that extra empty array is handled
    input = (number_calls, board_list[1:])
    return input

def print_board(board):
    for line in board:
        print(line)
    print()

def part_1(input: Tuple[List,List[List[List]]]) -> int:
    ans = 0
    num_calls = input[0]
    board_list = np.array(input[1])

    # Create a same sized array of bools to track matches
    track_list = np.full_like(board_list, False)

    # Closure so it can just return when the winning board is found
    # instead of several breaks or conditionals
    def play_bingo() -> Tuple[int,int]:
        nonlocal track_list
        for call in num_calls:
            track_list = np.logical_or(track_list, board_list == call)
            for i, board in enumerate(track_list):
                # Logical and (all) on columns give list of bools, 
                #   where True means all elements in that column were True
                # Logical or (any) on that list of bools gives a bool
                #   where True means at least one of the columns was all True
                col_check = board.all(axis=0).any()
                row_check = board.all(axis=1).any()
                if col_check or row_check:
                    return i, call

    win_idx, last_call = play_bingo()

    # Mask out the called numbers to 0
    not_track = np.logical_not(track_list[win_idx])
    win_leftover = np.where(not_track, board_list[win_idx], 0)

    ans = np.sum(win_leftover) * last_call
    return ans

def part_2(input: List) -> int:
    ans = 0
    num_calls = input[0]
    board_list = np.array(input[1])

    # Array to track how many rounds it takes each board to win
    round_count = [0] * len(board_list)
    # Create a same sized array of bools to track matches
    track_list = np.full_like(board_list, False)

    # For every board, play bingo until it wins
    for board_idx, board in enumerate(board_list):
        track_board = np.full_like(board, False)
        for call_count, call in enumerate(num_calls):
            track_list[board_idx] = np.logical_or(track_list[board_idx], board == call)
            col_check = track_list[board_idx].all(axis=0).any()
            row_check = track_list[board_idx].all(axis=1).any()
            # When the board wins, save the index of the last call
            if col_check or row_check:
                round_count[board_idx] = call_count
                break

    last_win_idx = np.argmax(round_count)

    # Mask out the called numbers to 0
    not_track = np.logical_not(track_list[last_win_idx])
    winning_leftover = np.where(not_track, board_list[last_win_idx], 0)

    ans = np.sum(winning_leftover) * num_calls[round_count[last_win_idx]]
    return ans

def solve(part: int, input_type: str) -> int:
    input=read_input(input_type)
    if part == 1:
        ans = part_1(input)
    else:
        ans = part_2(input)
    return ans
