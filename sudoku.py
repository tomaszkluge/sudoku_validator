import numpy as np
import tkinter as tk


def is_valid_set(lst):
    return set(lst) == set(range(1, 10))


def check_sudoku_validity(sudoku):
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

    return valid


# Create a Tkinter window
window = tk.Tk()
window.title("Sudoku Validator")
window.geometry("350x350")


# Initialize the Sudoku grid as a NumPy array
sudoku = np.zeros((9, 9), dtype=int)

# Create a 2D list to hold the Entry widgets for Sudoku input
entry_grid = []

# Create Entry widgets for Sudoku input and populate the grid
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(window, width=3, font=("Arial", 14))
        entry.grid(row=i, column=j)
        entry.insert(0, "")
        row_entries.append(entry)
    entry_grid.append(row_entries)


def on_entry_change(i, j):
    value = entry_grid[i][j].get()
    if value.isdigit() and 1 <= int(value) <= 9:
        sudoku[i, j] = int(value)
    else:
        entry_grid[i][j].delete(0, tk.END)
        entry_grid[i][j].insert(0, "")


def validate_sudoku():
    validity = check_sudoku_validity(sudoku)
    if validity:
        result_label.config(text="Sudoku solution is valid.", fg="green")
    else:
        result_label.config(text="Sudoku solution is not valid.", fg="red")


# Button to validate Sudoku
validate_button = tk.Button(window, text="Validate Sudoku", command=validate_sudoku)
validate_button.grid(row=10, columnspan=9, pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.grid(row=11, columnspan=9, pady=10)

# Start the main tkinter loop
window.mainloop()

