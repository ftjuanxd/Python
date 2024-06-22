import os 
from random import randomrange as rm
import packages.design as ds
board = [[1,2,3],[4,"X",6],[7,8,9]]

def play(board,px):#esta funcion debe ser llamada desde el menu y llamar a display
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == px:
                board[i][j]= "O"
    for CPU_i in range(len(board)):
        for CPU_j in range(len(board)):
            if board[CPU_i][CPU_j] == rm(1,10):
                board[CPU_i][CPU_j]= "X"
    ds.display_board(board)
def clean():
    # Para limpiar la consola en Windows
    if os.name == 'nt':
        os.system('cls')
    # Para limpiar la consola en Unix/Linux/Mac
    else:
        os.system('clear')
def menu ():
    opc = input("Do you Wish to Begin? S/N: ").lower()
    if opc == "s":
        px = int()
        while True:
            try:
                ds.display_board(board)
                px = int(input("Type Position: "))
                break
            except ValueError:
                print("Type only Integer Numbers.")
                clean()
        if px < 0 and px > 10:
            raise("The position is wrong.")
        else:
            play(board,px)
    else:
        print("Thanks, Bye.")
menu()