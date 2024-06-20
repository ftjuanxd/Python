board = [[1,2,3],[4,"X",6],[7,8,9]]
def line():   
    for i in range(25):
        if i == 0 or i == 8 or i == 16 or i == 24:
            print("+",end="")
        else:
            print("-",end="")
    print("\n")
def side(board):
    for j in range(3):
        for i in range(25):
            if i == 0 or i == 8 or i == 16 or i == 24:
                print("|",end="")
            elif i == 4 and j == 1 or i == 12 and j == 1 or i == 20 and j == 1: 
                print(board[0][0],end="")
                board[0].remove(board[0][0])
            else:
                print(" ",end="")
        print("\n")

def display_board(board):
    for i in range(3):
        line()
        side(board)
        del board[0]
    line()
def play(board,px=-1,py=-1):
    if px > 0 and py < 4 and py > 0 and py < 4:
        if board[px][py].isdigit():
            board[px][py]= "O"
            return board
        else:
            return False
    elif px ==-1 and py == -1:
        side(board)
    else:
        return True
def menu ():
    opc = input("Do you Wish to Begin? S/N: ").lower()
    if opc == "s":