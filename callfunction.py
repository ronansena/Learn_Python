#Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
#import pyautogui 
import tkinter as tk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry("700x350")

#Define a function for opening the Dialog box
def open_prompt(): 

    win.resizable(False, False)
    win.title("Execution:")
    text = Text(win, height=8)
    text.pack()
    
   # If your shell script has shebang, 
   # you can omit shell=True argument.
    result = subprocess.Popen("python3 /media/EXTRA_NVME_500GB_EXT4/CODE/PYTHON/web_scraping_with_python/Scraping_Prices_Project/produtoRastreado.py".split(), stdout=subprocess.PIPE, bufsize=1, text=True)

    #result = subprocess.Popen(["/scrapping_prices.sh", 
                    #"arguments"],stdout=subprocess.PIPE, bufsize=1, text=True)      
    
    while result.poll() is None:
        msg = result.stdout.readline().strip()  # read a line from the process output
        if msg:
            text.insert(tk.END, msg + "\n")
    

   #print(result)
   #print(result.stdout.strip("\n"))
   #print(result.stderr.strip("\n"))
   #pyautogui.alert(result)
   
    messagebox.showinfo("Message", "Processamento finalizado com Sucesso!")

#Create a Label widget
Label(win, text= "Click to Open the MessageBox").pack(pady=15)

#Create a Button for opening a dialog Box
ttk.Button(win, text="Realizar o Scraper dos preos do produtos", command= open_prompt).pack()

win.mainloop()