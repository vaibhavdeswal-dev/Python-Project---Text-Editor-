# this is my own text editor app like notepad...where we can write story ,letter and many more things

import tkinter as tk  #tkinter is a module in python which is a standard library used to make GUI ( windows,labels,buttons)
from tkinter import filedialog , messagebox  # used for opem save and edit a file 

def new_file(): # this fun is used for when the user wants to open a new file so empty the textbox
    text.delete(1.0,tk.END) # 1.0 means start from the first char of the file

def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt" , filetypes=[("Text Files" ,"*.txt")])
        if file_path:
            with open(file_path ,'r')as file:
                text.delete(1.0 ,tk.END)
                text.insert(tk.END, file.read())

def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt" , filetypes=[("Text Files" ,"*.txt")])
        if file_path:
              with open(file_path , 'w')as file:
                    file.write(text.get(1.0 ,tk.END))
                    messagebox.showinfo("Info" , "File saves successfully!")

root = tk.Tk()
root.title("My Text Editor") 
root.geometry ("800x600")              

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit" , command=root.quit)

text = tk.Text(root , wrap=tk.WORD , font = ("Helvetica" , 24) , fg = "black")
text.pack(expand=tk.YES , fill = tk.BOTH)

root.mainloop() # this shows window on screen


