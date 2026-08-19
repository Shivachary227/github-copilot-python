# 🎮 Sudoku Game

A modern Sudoku game built with **Python Flask, JavaScript, HTML, and CSS**.

This project was developed as a refactoring exercise using GitHub Copilot, with additional features focused on usability, validation, game management, and user experience.

## ✨ Features

- 🎯 Sudoku puzzles with unique solutions
- 🟢 Easy difficulty
- 🟡 Medium difficulty
- 🔴 Hard difficulty
- ⏱️ Game timer
- ⏸️ Pause and Resume
- 💡 Hint system
- 🔢 Hint counter
- ✅ Solution validation
- ❌ Incorrect-cell highlighting
- 👤 Player name support
- 🏆 Top 10 leaderboard
- 🗑️ Clear leaderboard
- 🌙 Dark mode
- 🎉 Completion/result screen
- 📱 Responsive user interface
- 🧪 Automated test suite

## 🛠️ Technologies

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- Pytest
- Git & GitHub


## GitHub Copilot Usage

GitHub Copilot was used as a development assistant throughout the refactoring
process. I used Copilot to explore implementation approaches, review existing
code, improve maintainability, and understand testing and UI requirements.

### Copilot Milestones

#### 1. Testing Framework

Copilot was used to review the pytest testing framework and explain how the
existing tests validate the Sudoku logic.

Evidence:
`screenshots/copilot_testing_framework.png`

#### 2. Unique Sudoku Solution

Copilot was used to review the Sudoku generation algorithm and explain how the
application ensures that generated puzzles have exactly one solution.

Evidence:
`screenshots/copilot_unique_solution_prompt.png`

#### 3. Top-10 Leaderboard

Copilot was used to review the leaderboard implementation, including local
storage, score sorting, player information, difficulty, completion time, and
hints.

Evidence:
`screenshots/copilot_top10_scores.png`

#### 4. Sudoku Grid Styling

Copilot was used to review the CSS responsible for the 9x9 Sudoku grid and
its 3x3 visual sections.

Evidence:
`screenshots/copilot_grid_styling.png`

### Responsible Use of Copilot

I treated GitHub Copilot as an assistant rather than an unquestioned code
generator. I reviewed its suggestions before applying them and compared
suggestions against the project requirements and existing tests.

When a suggestion was unnecessary or could introduce additional complexity,
I rejected or modified the suggestion rather than applying it automatically.

Evidence of reviewing and evaluating a Copilot suggestion:

`screenshots/copilot_suggestion_review.png`

### Verification

After making changes, I manually tested the application and ran the automated
test suite.

The Sudoku logic test suite currently passes all 17 tests.

## 📁 Project Structure

```text
starter/
│
├── app.py
├── sudoku_logic.py
├── requirements.txt
├── instruction.md
├── README.md
│
├── static/
│   ├── main.js
│   └── styles.css
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_sudoku_logic.py

