import numpy as np
import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Sudoku Solver")

# Initialize the Sudoku grid as a NumPy array
sudoku = np.zeros((9, 9), dtype=int)

# Input values into the Sudoku grid
for i in range(9):
    for j in range(9):
        while True:
            value = input(f"Enter the number for row {i + 1}, column {j + 1}: ")
            if value.isdigit() and 1 <= int(value) <= 9:
                sudoku[i, j] = int(value)
                break
            else:
                print("Please enter a valid number between 1 and 9.")


def is_valid_set(lst):
    return set(lst) == set(range(1, 10))


valid = True

# Check rows
for row in sudoku:
    if not is_valid_set(row):
        valid = False
        break

# Check columns
for col in sudoku.T:
    if not is_valid_set(col):
        valid = False
        break

# Check 3x3 squares
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        subgrid = sudoku[i:i+3, j:j+3]
        if not is_valid_set(subgrid.flatten()):
            valid = False
            break

if valid:
    print("Sudoku solution is valid.")
else:
    print("Sudoku solution is not valid.")
