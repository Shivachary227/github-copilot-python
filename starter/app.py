from flask import Flask, render_template, jsonify, request
import sudoku_logic

app = Flask(__name__)

# Keep a simple in-memory store for current puzzle and solution
CURRENT = {
    'puzzle': None,
    'solution': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new_game():
    difficulty = request.args.get('difficulty')

    if difficulty:
        try:
            puzzle, solution = sudoku_logic.generate_puzzle(
                difficulty=difficulty
            )
        except ValueError as error:
            return jsonify({'error': str(error)}), 400
    else:
        clues = int(request.args.get('clues', 35))
        puzzle, solution = sudoku_logic.generate_puzzle(clues=clues)

    CURRENT['puzzle'] = puzzle
    CURRENT['solution'] = solution
    CURRENT['difficulty'] = difficulty or 'custom'

    return jsonify({
        'puzzle': puzzle,
        'difficulty': difficulty or 'custom'
    })

@app.route('/check', methods=['POST'])
def check_solution():
    data = request.json
    board = data.get('board')
    solution = CURRENT.get('solution')

    if solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    incorrect = []

    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):

            # Ignore empty cells.
            # Empty cells are represented by 0.
            if board[i][j] == 0:
                continue

            # Check only numbers entered by the player.
            if board[i][j] != solution[i][j]:
                incorrect.append([i, j])

    return jsonify({'incorrect': incorrect})


@app.route('/hint', methods=['POST'])


def get_hint():
    puzzle = CURRENT.get('puzzle')
    solution = CURRENT.get('solution')

    if puzzle is None or solution is None:
        return jsonify({'error': 'No game in progress'}), 400

    data = request.json or {}
    board = data.get('board')

    if board is None:
        return jsonify({'error': 'Board is required'}), 400

    empty_cells = []

    for i in range(sudoku_logic.SIZE):
        for j in range(sudoku_logic.SIZE):

            if puzzle[i][j] == sudoku_logic.EMPTY:
                if board[i][j] == 0:
                    empty_cells.append((i, j))

    if not empty_cells:
        return jsonify({
            'error': 'No empty cells available for a hint'
        }), 400

    row, col = empty_cells[0]

    return jsonify({
        'row': row,
        'col': col,
        'value': solution[row][col]
    })

if __name__ == '__main__':
    app.run(debug=True)

