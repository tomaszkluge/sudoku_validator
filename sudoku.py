'''
Sudoku validator

'''

sudoku1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
]

# ROWS OPTION:
for rows in sudoku1:
    if sum(set(rows)) != 45:
        print(False)
        break

# COLUMNS:
columns = []

for i in sudoku1:
    for j in i:
        columns.append(j)

if all(sum(set(columns[i : i + 73 : 9])) != 45 for i in range(9)):
    print(False)

# SQUARE OPTION:
one = []
two= []
three = []

for i in sudoku1:
    for j in i[:3]:
        one.append(j)

first = one[:9], one[9:18], one[18:27]


for i in sudoku1:
    for j in i[3:6]:
        two.append(j)

second = two[:9], two[9:18], two[18:27]


for i in sudoku1:
    for j in i[6:9]:
        three.append(j)

third = three[:9], three[9:18], three[18:27]

all_in_one = first + second + third

for i in all_in_one:
    if sum(set(i)) != 45:
        print(False)
        break
