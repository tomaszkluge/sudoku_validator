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
    if len(set(rows)) != 9:
        print("Sudoku1 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku1:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fifth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku1 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fifthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku1[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku1[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku1[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku1[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku1[3:6]:
        fiv = row[3:6]
        fifthh += fiv

    for row in sudoku1[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku1[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku1[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku1[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fifthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku1 has incorrect number in square")
        break

sudoku2 = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]

# ROWS OPTION:
for rows in sudoku2:
    if len(set(rows)) != 9:
        print("Sudoku2 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku2:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku2 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku2[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku2[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku2[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku2[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku2[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku2[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku2[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku2[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku2[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku2 has incorrect number in square")
        break

sudoku3 = [
    [4, 3, 2, 2, 6, 9, 7, 8, 1],
    [6, 8, 5, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]

# ROWS OPTION:
for rows in sudoku3:
    if len(set(rows)) != 9:
        print("Sudoku3 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku3:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku3 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku3[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku3[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku3[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku3[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku3[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku3[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku3[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku3[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku3[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku3 has incorrect number in square")
            break

sudoku4 = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [1, 5, 9, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]

# ROWS OPTION:
for rows in sudoku4:
    if len(set(rows)) != 9:
        print("Sudoku4 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku4:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku4 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku4[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku4[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku4[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku4[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku4[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku4[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku4[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku4[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku4[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku4 has incorrect number in square")
            break

sudoku5 = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [8, 9, 7, 1, 3, 4, 5, 6, 2],
    [1, 2, 6, 8, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9],
]

# ROWS OPTION:
for rows in sudoku5:
    if len(set(rows)) != 9:
        print("Sudoku5 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku5:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku5 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku5[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku5[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku5[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku5[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku5[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku5[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku5[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku5[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku5[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku5 has incorrect number in square")
            break

sudoku6 = [
    [5, 9, 6, 1, 4, 2, 5, 3, 7],
    [6, 1, 4, 3, 5, 8, 2, 4, 8],
    [5, 6, 9, 4, 1, 2, 5, 3, 6],
    [1, 9, 5, 3, 6, 8, 4, 1, 6],
    [5, 9, 3, 6, 3, 4, 8, 2, 1],
    [5, 9, 5, 3, 2, 1, 4, 5, 6],
    [1, 3, 6, 4, 8, 6, 5, 2, 5],
    [4, 1, 2, 3, 6, 8, 4, 9, 2],
    [3, 6, 8, 7, 4, 1, 5, 6, 3],
]

# ROWS OPTION:
for rows in sudoku6:
    if len(set(rows)) != 9:
        print("Sudoku6 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku6:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku6 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku6[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku6[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku6[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku6[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku6[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku6[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku6[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku6[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku6[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku6 has incorrect number in square")
            break

sudoku7 = [
    [1, 3, 3, 4, 5, 6, 7, 7, 9],
    [4, 5, 6, 7, 7, 9, 1, 3, 3],
    [7, 7, 9, 1, 3, 3, 4, 5, 6],
    [9, 1, 3, 3, 4, 5, 6, 7, 7],
    [3, 4, 5, 6, 7, 7, 9, 1, 3],
    [6, 7, 7, 9, 1, 3, 3, 4, 5],
    [7, 9, 1, 3, 3, 4, 5, 6, 7],
    [3, 3, 4, 5, 6, 7, 7, 9, 1],
    [5, 6, 7, 7, 9, 1, 3, 3, 4],
]

# ROWS OPTION:
for rows in sudoku7:
    if len(set(rows)) != 9:
        print("Sudoku7 has incorrect number in row")
        break

# COLUMNS OPTION:
first = []
second = []
third = []
fourth = []
fivth = []
sixth = []
seventh = []
eighth = []
ninth = []

for row in sudoku7:
    first.append(row[0])
    second.append(row[1])
    third.append(row[2])
    fourth.append(row[3])
    fivth.append(row[4])
    sixth.append(row[5])
    seventh.append(row[6])
    eighth.append(row[7])
    ninth.append(row[8])

new_rows = [first, second, third, fourth, fivth, sixth, seventh, eighth, ninth]
for rows in new_rows:
    if len(set(rows)) != 9:
        print("Sudoku7 has incorrect number in column")
        break

    # SQUARE OPTION:
    firstt = []
    secondd = []
    thirdd = []
    fourthh = []
    fivthh = []
    sixthh = []
    seventhh = []
    eighthh = []
    ninthh = []
    for row in sudoku7[:3]:
        one = row[:3]
        firstt += one

    for row in sudoku7[3:6]:
        sec = row[:3]
        secondd += sec

    for row in sudoku7[6:9]:
        thr = row[:3]
        thirdd += thr

    for row in sudoku7[:3]:
        four = row[3:6]
        fourthh += four

    for row in sudoku7[3:6]:
        fiv = row[3:6]
        fivthh += fiv

    for row in sudoku7[6:9]:
        six = row[3:6]
        sixthh += six

    for row in sudoku7[:3]:
        one = row[6:9]
        seventhh += one

    for row in sudoku7[3:6]:
        one = row[6:9]
        eighthh += one

    for row in sudoku7[6:9]:
        one = row[6:9]
        ninthh += one
    new_rows = [
        firstt,
        secondd,
        thirdd,
        fourthh,
        fivthh,
        sixthh,
        seventhh,
        eighthh,
        ninthh,
    ]
    for i in new_rows:
        if len(set(i)) != 9:
            print("Sudoku7 has incorrect number in square")
            break
