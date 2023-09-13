"""
Sudoku validator

"""
sudoku = []

for i in range(9):
    row = []
    for j in range(9):
        while True:
            value = input(f"Enter the number for row {i + 1}, column {j + 1}: ")
            if value.isdigit() and 1 <= int(value) <= 9:
                row.append(int(value))
                break
            else:
                print("Please enter a valid number between 1 and 9.")
    sudoku.append(row)


def is_valid_set(lst):
    return set(lst) == set(range(1, 10))


valid = True

# ROWS OPTION:
for rows in sudoku:
    if sum(set(rows)) != 45:
        print(False)
        break

# COLUMNS:
columns = []

for i in sudoku:
    for j in i:
        columns.append(j)

if all(sum(set(columns[i: i + 73: 9])) != 45 for i in range(9)):
    print(False)

# SQUARE OPTION:
one = []
two = []
three = []

for i in sudoku:
    for j in i[:3]:
        one.append(j)

first = one[:9], one[9:18], one[18:27]

for i in sudoku:
    for j in i[3:6]:
        two.append(j)

second = two[:9], two[9:18], two[18:27]

for i in sudoku:
    for j in i[6:9]:
        three.append(j)

third = three[:9], three[9:18], three[18:27]

all_in_one = first + second + third

for i in all_in_one:
    if sum(set(i)) != 45:
        print(False)
        break
