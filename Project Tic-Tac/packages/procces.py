from . import design as ds
import os 
from random import randrange as rm
#Test Winner
def Test(board,pointer,size):
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
#Play User

def play_user(board,px,pointer,size):#esta funcion debe ser llamada desde el menu y llamar a display
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == px:
                board[i][j]= pointer[1]
    ds.display_board(board)

#Play CPU
def play_cpu(board,pointer,size,black_list=None):
    
    if black_list is None:
        black_list = []        
    num_ran = rm(1,10)
    
    while num_ran in black_list:
        num_ran = rm(1,10)
    
    black_list.append(num_ran)
        
    for CPU_i in range(size):
        for CPU_j in range(size):
            if board[CPU_i][CPU_j] == num_ran and isinstance(board[CPU_i][CPU_j], int):
                board[CPU_i][CPU_j]= pointer[0]
                ds.display_board(board)
                return 
    play_cpu(board,pointer,size,black_list)
#Clean Screen
def clean():
    # Para limpiar la consola en Windows
    if os.name == 'nt':
        os.system('cls')
    # Para limpiar la consola en Unix/Linux/Mac
    else:
        os.system('clear')