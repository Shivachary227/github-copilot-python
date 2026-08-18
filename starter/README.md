# 🎮 Sudoku Game

A web-based Sudoku game built using Python, Flask, HTML, CSS, and JavaScript.

The application generates Sudoku puzzles with different difficulty levels and provides an interactive interface for solving and checking puzzles.

## 🚀 Features

- 🎮 Interactive Sudoku game
- 👤 Player name
- 🎯 Three difficulty levels:
  - Easy
  - Medium
  - Hard
- ⏱️ Game timer
- ⏸️ Pause and Resume
- 💡 Hint system
- 🔍 Solution checking
- ❌ Incorrect-cell highlighting
- 🎉 Completion/result screen
- 🏆 Top 10 leaderboard
- 💾 Leaderboard persistence using browser localStorage
- 🧹 Clear leaderboard
- 🌙 Dark mode
- 📱 Responsive user interface

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Testing
- pytest

### Data Storage
- Browser LocalStorage for leaderboard data

## 📂 Project Structure

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