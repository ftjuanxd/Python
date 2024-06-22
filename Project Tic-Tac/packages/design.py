def line():   
    for i in range(25):
        if i == 0 or i == 8 or i == 16 or i == 24:
            print("+", end="")
        else:
            print("-", end="")
    print("\n")

def side(board, row_index):
    counter_x = 0
    for j in range(0, 3):
        for k in range(25):
            if k == 0 or k == 8 or k == 16 or k == 24:
                print("|", end="")
            elif (k == 4 and j == 1) or (k == 12 and j == 1) or (k == 20 and j == 1):
                print(board[row_index][counter_x], end="")
                counter_x += 1
                if counter_x > 2:
                    counter_x = 0
            else:
                print(" ", end="")
        else:
            print("\n")

def display_board(board):
    for i in range(3):
        line()
        side(board, i)  # Pasar el índice de la fila como argumento a la función 'side'
    line()
