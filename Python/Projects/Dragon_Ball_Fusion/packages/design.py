import os
import time
import tkinter as tk
from tkinter import ttk

#Crear Ventana
def Create_Screen(text):
    rest = tk.StringVar()
    #Create New Window Personalize
    window = tk.Toplevel()
    window.title("Dragon Ball Fusion")
    #set up size window
    window.geometry("300x200")
        
    #create label with a Message
    label = ttk.Label(window,text)
    label.pack(pady=10)
    text.pop(0)    
    #create input
    input_text= ttk.Entry(window)
    input_text.pack(pady=10)
       
    #function button sent
    def sent():
        rest.set(input_text.get())
        window.destroy()
    
    button_sent = ttk.Button(window,text="Enviar",command=sent)
    button_sent.pack(pady=10)
    
    window.wait_window()
    
    return rest

def Show_Screen(text):
    #Create New Window Personalize
    window = tk.Toplevel()
    window.title("Dragon Ball Fusion")
    #set up size window
    window.geometry("300x200")
        
    #create label with a Message
    label = ttk.Label(window,text)
    label.pack(pady=10)
    
    button_sent = ttk.Button(window,text="OK")
    button_sent.pack(pady=10)
    
    
def clear_Screen(seconds):
    time.sleep(seconds)
    if os.name == "nt":
        os.system("cls")
    else:#Mac or Linux
        os.system("clear")
    