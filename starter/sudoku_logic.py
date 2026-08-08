import copy
import random

SIZE = 9
EMPTY = 0

def deep_copy(board):
    return copy.deepcopy(board)

def create_empty_board():
    return [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

def is_safe(board, row, col, num):
    # Check row and column
    for x in range(SIZE):
        if board[row][x] == num or board[x][col] == num:
            return False
    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def fill_board(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                possible = list(range(1, SIZE + 1))
                random.shuffle(possible)
                for candidate in possible:
                    if is_safe(board, row, col, candidate):
                        board[row][col] = candidate
                        if fill_board(board):
                            return True
                        board[row][col] = EMPTY
                return False
    return True

def remove_cells(board, clues):
    """Remove cells while keeping exactly one Sudoku solution."""
    cells = [
        (row, col)
        for row in range(SIZE)
        for col in range(SIZE)
    ]

    random.shuffle(cells)

    target_removals = SIZE * SIZE - clues
    removed = 0

    for row, col in cells:
        if removed >= target_removals:
            break

        original = board[row][col]
        board[row][col] = EMPTY

        test_board = deep_copy(board)

        if count_solutions(test_board, limit=2) == 1:
            removed += 1
        else:
            board[row][col] = original

def generate_puzzle(clues=35, difficulty=None):
    """Generate a Sudoku puzzle with a unique solution."""

    difficulty_clues = {
        "easy": 45,
        "medium": 35,
        "hard": 30,
    }

    if difficulty is not None:
        if difficulty not in difficulty_clues:
            raise ValueError(
                "Difficulty must be easy, medium, or hard"
            )

        clues = difficulty_clues[difficulty]

    if clues < 17 or clues > SIZE * SIZE:
        raise ValueError("Clues must be between 17 and 81")

    board = create_empty_board()
    fill_board(board)

    solution = deep_copy(board)

    remove_cells(board, clues)

    puzzle = deep_copy(board)

    return puzzle, solution


def count_solutions(board, limit=2):
    """Count Sudoku solutions, stopping once the limit is reached."""
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                total = 0

                for num in range(1, SIZE + 1):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        total += count_solutions(board, limit)
                        board[row][col] = EMPTY

                        if total >= limit:
                            return total

                return total

    return 1