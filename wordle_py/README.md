# Wordle Puzzle Solver

My Python [script](./wordle_py/wordle.py) to help you cheat at the New York Times' Wordle Puzzle!

## Usage

$ python wordle.py

### Steps

1. Enter the 5-letter word you have tried.
2. Enter the flags corresponding to the wordle results:
    - 'g' for Green
    - 'y' for Yellow
    - 'x' for Gray
3. The app will give you a list of the 5-letter words that are still in play, and sorted by commonality in English. The app will remember the results from each round and narrow down the possibilities.
4. Use any of the suggested words.
5. If needed, 'r' will reset and clear the memory of prior guesses to start over.
