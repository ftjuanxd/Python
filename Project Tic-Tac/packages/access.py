from . import design as ds
from . import procces as pr
pointer = ("X","O")#pointer[0] is CPU and pointer[1] is User
board = [[1,2,3],[4,"X",6],[7,8,9]]
size = len(board)

def menu ():
    opc = input("Do you Wish to Begin? S/N: ").lower()
    if opc == "s":
        while not pr.Test(board,pointer,size):
                px = int()
                while True:
                    try:
                        ds.display_board(board)
                        px = int(input("Type Position: "))
                        break
                    except ValueError:
                        print("Type only Integer Numbers.")
                        pr.clean()
                if px <= 0 and px >= 10:
                    raise("The position is wrong.")
                    pr.clean()
                else:
                    pr.play_user(board,px,pointer,size)
                    if not pr.Test(board,pointer,size):
                        print("Turn CPU")
                        pr.play_cpu(board,pointer,size)
                    else:
                        break
    else:
        print("Thanks, Bye.")
