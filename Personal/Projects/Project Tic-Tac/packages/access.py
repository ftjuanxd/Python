from . import design as ds
from . import procces as pr
pointer = ("X","O")#pointer[0] is CPU and pointer[1] is User
board = [[1,2,3],[4,"X",6],[7,8,9]]
size = len(board)

def menu ():
    opc = input("Do you Wish to Begin? S/N: ").lower()
    if opc == "s":
        while not pr.Test(board,pointer,size):
            
                pr.play_user(board,pr.Template(board),pointer,size)
            
                if pr.Test(board,pointer,size):
                        return "End Game"
            
                print("Turn CPU")
                pr.play_cpu(board,pointer,size)
                
                if pr.Test(board,pointer,size):
                        return "End Game"
    else:
        print("Thanks, Bye.")