board = []

for i in range(8):
    row = ['EMPTY' for i in range(8)]
    board.append(row)

for i in range(8):
    for j in range(8):
        if j == 0 and i == 0 or j == 7 and i == 7:
            board.insert(i,j,"Rook")