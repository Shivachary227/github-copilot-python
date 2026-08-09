// Client-side rendering and interaction for the Flask-backed Sudoku

const SIZE = 9;
let puzzle = [];

let timerInterval = null;
let elapsedSeconds = 0;


function updateTimer() {
    elapsedSeconds++;

    const minutes = Math.floor(elapsedSeconds / 60);
    const seconds = elapsedSeconds % 60;

    const timeText =
        String(minutes).padStart(2, '0') +
        ':' +
        String(seconds).padStart(2, '0');

    document.getElementById('timer').innerText = `Time: ${timeText}`;
}


function startTimer() {
    stopTimer();

    elapsedSeconds = 0;
    document.getElementById('timer').innerText = 'Time: 00:00';

    timerInterval = setInterval(updateTimer, 1000);
}


function stopTimer() {
    if (timerInterval !== null) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
}


function createBoardElement() {
    const boardDiv = document.getElementById('sudoku-board');

    boardDiv.innerHTML = '';

    for (let i = 0; i < SIZE; i++) {

        const rowDiv = document.createElement('div');
        rowDiv.className = 'sudoku-row';

        for (let j = 0; j < SIZE; j++) {

            const input = document.createElement('input');

            input.type = 'text';
            input.maxLength = 1;
            input.className = 'sudoku-cell';

            input.dataset.row = i;
            input.dataset.col = j;

            // Allow only numbers 1-9
            input.addEventListener('input', (e) => {

                const val = e.target.value.replace(/[^1-9]/g, '');

                e.target.value = val;

                // Remove previous result highlighting
                e.target.classList.remove('incorrect');
                e.target.classList.remove('correct');

                // Clear message when user changes an answer
                document.getElementById('message').innerText = '';
            });

            rowDiv.appendChild(input);
        }

        boardDiv.appendChild(rowDiv);
    }
}


function renderPuzzle(puz) {

    puzzle = puz;

    createBoardElement();

    const boardDiv = document.getElementById('sudoku-board');

    const inputs = boardDiv.getElementsByTagName('input');

    for (let i = 0; i < SIZE; i++) {

        for (let j = 0; j < SIZE; j++) {

            const idx = i * SIZE + j;

            const val = puzzle[i][j];

            const inp = inputs[idx];

            // Remove all previous classes
            inp.className = 'sudoku-cell';

            if (val !== 0) {

                // Given Sudoku number
                inp.value = val;

                inp.disabled = true;

                inp.classList.add('prefilled');

            } else {

                // Empty cell
                inp.value = '';

                inp.disabled = false;
            }
        }
    }
}


async function newGame() {

    try {

        const difficulty =
            document.getElementById('difficulty').value;

        const res = await fetch(
            `/new?difficulty=${difficulty}`
        );

        const data = await res.json();

        if (data.error) {
            document.getElementById('message').innerText =
                data.error;
            return;
        }

        renderPuzzle(data.puzzle);

        const msg = document.getElementById('message');

        msg.innerText = '';
        msg.style.color = '#d32f2f';

        // Start timer for the new game
        startTimer();

    } catch (error) {

        console.error(error);

        document.getElementById('message').innerText =
            'Unable to start a new game.';
    }
}

async function checkSolution() {

    const boardDiv = document.getElementById('sudoku-board');

    const inputs = boardDiv.getElementsByTagName('input');

    const board = [];

    // Build current board
    for (let i = 0; i < SIZE; i++) {

        board[i] = [];

        for (let j = 0; j < SIZE; j++) {

            const idx = i * SIZE + j;

            const val = inputs[idx].value;

            board[i][j] = val ? parseInt(val, 10) : 0;
        }
    }


    try {

        const res = await fetch('/check', {

            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                board: board
            })
        });


        const data = await res.json();

        const msg = document.getElementById('message');


        if (data.error) {

            msg.style.color = '#d32f2f';

            msg.innerText = data.error;

            return;
        }


        // Remove previous highlighting
        for (let idx = 0; idx < inputs.length; idx++) {

            inputs[idx].classList.remove('incorrect');
            inputs[idx].classList.remove('correct');
        }


        // Convert incorrect positions into a Set
        const incorrect = new Set(
            data.incorrect.map(
                x => x[0] * SIZE + x[1]
            )
        );


        let emptyCells = 0;


        // Check each editable cell
        for (let idx = 0; idx < inputs.length; idx++) {

            const inp = inputs[idx];

            // Do not modify original puzzle numbers
            if (inp.disabled) {
                continue;
            }


            const value = inp.value;

            // Empty cell
            if (value === '') {

                emptyCells++;

                continue;
            }


            // Wrong number
            if (incorrect.has(idx)) {

                inp.classList.add('incorrect');

            } else {

                // Correct number
                inp.classList.add('correct');
            }
        }


        // Results
        if (incorrect.size > 0) {

            msg.style.color = '#d32f2f';

            msg.innerText = 'Some cells are incorrect.';

        } else if (emptyCells > 0) {

            msg.style.color = '#f57c00';

            msg.innerText =
                'Good progress! Fill in all remaining cells.';

        } else {

            // Puzzle completely solved
            stopTimer();

            msg.style.color = '#388e3c';

            msg.innerText =
                'Congratulations! You solved it! 🎉';
        }


    } catch (error) {

        console.error(error);

        document.getElementById('message').innerText =
            'Unable to check the solution.';
    }
}


// Wire buttons
window.addEventListener('load', () => {

    document
        .getElementById('new-game')
        .addEventListener('click', newGame);

    document
        .getElementById('check-solution')
        .addEventListener('click', checkSolution);

    document
        .getElementById('difficulty')
        .addEventListener('change', newGame);

    // Start the first game
    newGame();
});