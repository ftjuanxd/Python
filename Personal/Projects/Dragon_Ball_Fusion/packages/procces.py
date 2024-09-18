from . import design as d
import tkinter as tk

outputs = ["\nMenu\n1.Create Character\n2.Merger Character\n3.Show Character.\nChoose",["Name","Speed","Power","Energy"],["Name Character 1:","Name Character 2:"]]

mistake = ["Just Numbers"]

root =tk.Tk()
root.withdraw()

def Main():
    opc = d.Create_Screen(outputs[0])
    if opc == 1:
        #getting character's values
        for values in outputs[1]:
            d.Create_Screen(values)
    elif opc == 2:
        #getting characters' names
        for values in outputs[2]:
            d.Create_Screen(values)
    elif opc == 3:
        #show characters' names
        #values would be a list 
        d.Create_Screen(values)
    else:
        #show the mistake and wait five seconds pa
        d.Create_Screen(mistake[0])
        d.clear_Screen(3)
        Main()
root.mainloop()