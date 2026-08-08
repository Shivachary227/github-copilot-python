import pytest
from sudoku_logic import (
    EMPTY,
    SIZE,
    create_empty_board,
    fill_board,
    generate_puzzle,
    is_safe,
)


def board_is_valid(board):
    for row in board:
        if set(row) != set(range(1, SIZE + 1)):
            return False

    for col in range(SIZE):
        column_values = [board[row][col] for row in range(SIZE)]
        if set(column_values) != set(range(1, SIZE + 1)):
            return False

    for start_row in range(0, SIZE, 3):
        for start_col in range(0, SIZE, 3):
            box_values = []
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    box_values.append(board[row][col])
            if set(box_values) != set(range(1, SIZE + 1)):
                return False

    return True


def test_size_is_nine():
    assert SIZE == 9


def test_empty_is_zero():
    assert EMPTY == 0


def test_create_empty_board_is_9x9():
    board = create_empty_board()
    assert len(board) == 9
    assert all(len(row) == 9 for row in board)


def test_new_board_has_only_empty_cells():
    board = create_empty_board()
    for row in board:
        for cell in row:
            assert cell == EMPTY


def test_is_safe_accepts_valid_number():
    board = create_empty_board()
    assert is_safe(board, 0, 0, 5) is True


def test_is_safe_rejects_duplicate_in_same_row():
    board = create_empty_board()
    board[0][0] = 7
    assert is_safe(board, 0, 1, 7) is False


def test_is_safe_rejects_duplicate_in_same_column():
    board = create_empty_board()
    board[0][0] = 4
    assert is_safe(board, 1, 0, 4) is False


def test_is_safe_rejects_duplicate_in_same_box():
    board = create_empty_board()
    board[0][0] = 2
    assert is_safe(board, 0, 2, 2) is False


def test_fill_board_produces_completed_valid_board():
    board = create_empty_board()
    assert fill_board(board) is True
    assert all(cell != EMPTY for row in board for cell in row)
    assert board_is_valid(board) is True


def test_generate_puzzle_returns_puzzle_and_solution():
    puzzle, solution = generate_puzzle()
    assert puzzle is not None
    assert solution is not None


def test_puzzle_and_solution_are_9x9():
    puzzle, solution = generate_puzzle()
    assert len(puzzle) == 9
    assert len(solution) == 9
    assert all(len(row) == 9 for row in puzzle)
    assert all(len(row) == 9 for row in solution)

def test_generated_puzzle_has_one_unique_solution():
    puzzle, solution = generate_puzzle(35)

    assert puzzle != solution
    assert solution is not None

def count_solutions(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                total = 0

                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        total += count_solutions(board)
                        board[row][col] = 0

                        if total > 1:
                            return total

                return total

    return 1


def test_generate_puzzle_has_exactly_one_solution():
    puzzle, solution = generate_puzzle()

    puzzle_copy = [row[:] for row in puzzle]

    assert count_solutions(puzzle_copy) == 1
    assert puzzle != solution

import pytest


@pytest.mark.parametrize(
    "difficulty, expected_clues",
    [
        ("easy", 45),
        ("medium", 35),
        ("hard", 30),
    ],
)
def test_generate_puzzle_difficulty_clue_counts(
    difficulty, expected_clues
):
    puzzle, solution = generate_puzzle(difficulty=difficulty)

    clue_count = sum(
        cell != EMPTY
        for row in puzzle
        for cell in row
    )

    assert clue_count == expected_clues
    assert puzzle != solution

def test_generate_puzzle_rejects_invalid_difficulty():
    import pytest

    with pytest.raises(ValueError):
        generate_puzzle(difficulty="extreme")

