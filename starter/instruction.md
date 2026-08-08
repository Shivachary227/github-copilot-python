# Sudoku Project Instructions

## Project Overview

This project is a Sudoku game built with Python and Flask.

The goal is to refactor the existing legacy application into a clean, maintainable,
responsive, and accessible Sudoku game while preserving existing functionality.

## Development Principles

- Use Python 3 and Flask.
- Keep the application modular and organized.
- Separate Flask routes, Sudoku game logic, and frontend code where practical.
- Prefer small, reusable functions with clear names.
- Follow PEP 8 style guidelines.
- Add comments only where they improve understanding.
- Use clear variable and function names.
- Handle errors consistently.
- Do not introduce unnecessary dependencies.
- Do not remove working functionality without a clear reason.

## Sudoku Rules

The game uses a standard 9x9 Sudoku board.

Every row must contain the numbers 1-9 without repetition.

Every column must contain the numbers 1-9 without repetition.

Every 3x3 box must contain the numbers 1-9 without repetition.

Every generated puzzle must have exactly one valid solution.

Prefilled cells must be locked and must not be editable by the player.

## Game Features

The final application should support:

- Easy, Medium, and Hard difficulty levels.
- Different numbers of prefilled cells for each difficulty.
- Validation that every generated puzzle has exactly one unique solution.
- Immediate feedback for invalid entries.
- A Check button that identifies incorrect cells.
- A Hint button that fills one correct empty cell and locks it.
- A timer that tracks the player's solving time.
- A congratulatory message when the puzzle is completed correctly.
- A Top 10 leaderboard.
- Player name, solving time, difficulty, and hint count in leaderboard records.
- Persistent Top 10 data using browser local storage.
- Dark and light mode.
- Responsive design for desktop and mobile screens.
- Alternating visual styling for the 3x3 Sudoku boxes.
- Accessible controls and readable text.

## Code Quality

Before making changes to existing functionality:

1. Understand the current implementation.
2. Keep existing behavior working where possible.
3. Use tests to verify behavior.
4. Run the test suite after significant changes.
5. Fix failing tests before continuing.
6. Avoid making unrelated changes.

## Testing

Use pytest for automated tests.

Tests should cover important Sudoku logic and application behavior.

At minimum, tests should verify:

- A Sudoku board has the correct dimensions.
- Sudoku rows, columns, and 3x3 boxes follow the rules.
- Generated puzzles are solvable.
- Generated puzzles have exactly one solution.
- Difficulty levels produce the expected number of clues.
- Invalid Sudoku entries are detected.
- Hint functionality provides a valid value.
- Completed puzzles are recognized correctly.

Run tests before and after major changes.

## GitHub Copilot Guidelines

Use GitHub Copilot as an assistant, not as an automatic decision maker.

Before accepting a Copilot suggestion:

- Read the suggested code.
- Understand what it changes.
- Check whether it follows the project requirements.
- Reject or modify suggestions that are unnecessary or incorrect.

When a change is large, explain the intended change first and implement it in logical steps.

Prefer focused Copilot prompts that address one major task at a time.

Keep Copilot conversations focused on the current problem.

If Copilot produces confusing or incorrect code, stop and investigate the issue before continuing.

## User Interface

The interface should:

- Work in both light and dark modes.
- Be responsive on desktop and mobile devices.
- Keep buttons and text readable.
- Clearly distinguish editable cells from prefilled cells.
- Clearly highlight invalid or conflicting cells.
- Use alternating styles for the 3x3 Sudoku boxes.
- Avoid layout shifts when the game state changes.
- Provide accessible labels and controls.

## Accessibility

Aim for WCAG 2.1 AA practices.

Use:

- Semantic HTML where appropriate.
- Keyboard-accessible controls.
- Sufficient text contrast.
- Clear focus states.
- Meaningful button labels.
- Appropriate labels for interactive controls.

Do not rely only on color to communicate important game information.

## Refactoring Guidelines

The existing project is legacy code.

Refactor carefully instead of rewriting everything blindly.

Prefer:

- Modular functions.
- Clear separation of responsibilities.
- Reusable Sudoku utilities.
- Consistent error handling.
- Testable logic.
- Maintainable frontend JavaScript and CSS.

Do not change multiple unrelated parts of the application at the same time.

## Important Constraint

Do not remove or break existing Sudoku functionality while adding new features.

When adding a feature, first understand how it interacts with the existing application.

Always verify the application after changes.

## Copilot Communication Style

When helping with this project:

1. Explain what the proposed change does.
2. Identify which files will be changed.
3. Make the smallest reasonable change.
4. Explain important code decisions.
5. Suggest how to test the change.
6. Do not assume a suggestion is correct just because it compiles.

The final project should be understandable to a beginner who is learning Python, Flask,
testing, web development, and GitHub Copilot.