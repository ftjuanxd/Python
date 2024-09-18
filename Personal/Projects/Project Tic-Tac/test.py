pointer = ("X", "O")  # pointer[0] es CPU y pointer[1] es User
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def Test(board):
    size = len(board)  # Tamaño de la matriz
    
    # Test Winner en filas
    for k in pointer:
        for i in range(size):
            cont = 0
            for elem in board[i]:
                if elem == k:
                    cont += 1
            if cont == size:
                if k == 'X':
                    print("CPU Winner")
                else:
                    print("User Winner")
                return True

    # Test Winner en columnas
    for k in pointer:
        for j in range(len(board[0])):
            cont = 0
            for i in range(size):
                if board[i][j] == k:
                    cont += 1
            if cont == size:
                if k == 'X':
                    print("CPU Winner")
                else:
                    print("User Winner")
                return True

    # Test Winner en la diagonal principal
    for k in pointer:
        count = 0
        for i in range(size):
            if board[i][i] == k:
                count += 1
        if count == size:
            if k == "X":
                print("CPU Winner")
            else:
                print("User Winner")
            return True

    # Test Winner en la diagonal secundaria
    for k in pointer:
        count = 0
        for i in range(size):
            if board[i][size - 1 - i] == k:
                count += 1
        if count == size:
            if k == "X":
                print("CPU Winner")
            else:
                print("User Winner")
            return True

    # Si no hay ganador
    return False
