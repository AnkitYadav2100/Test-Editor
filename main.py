# import tkinter for creaating gui app
import tkinter as tk
from tkinter import filedialog, messagebox

# main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")


# functionality
# create text area
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))

# pura area cover ho
text.pack(expand=True, fill=tk.BOTH)


# main logic
# function 1 - to create a new file
def new_file():
    text.delete(1.0, tk.END)  # delete the current file content to new file open when created


# functionc 2 - to opent a new file
def open_file():
    # open file dialogue - file ka path
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",  # default file extension
        filetypes=[("Text Files", "*.txt")]  # it allow only txt file
    )

    if file_path:
        # open file
        with open(file_path, "r") as file:
            # clear old text
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


# function 3 - save the file
def save_file():
    # loacation jaha save karna hoga
    # open save file dialogue
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # default file extension
        filetypes=[("Text Files", "*.txt")],  # it allow only txt file
    )

    # file ka path jaha save karna hai
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))  # likha hua save ho jaye

    messagebox.showinfo("Info", "File saves successfully.")


# create menu bar
# base menu hai jo root se juda hai
menu = tk.Menu(root)
root.config(menu=menu)  # root se connect hai hum
file_menu = tk.Menu(menu)  # file name dihkega
help_menu = tk.Menu(menu)  # file name dihkega

# new open save exit dekhe
# add filemenu to menu bar
menu.add_cascade(label="File", menu=file_menu)  # label dena like file
menu.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="link")

# file ke andar new open save hoga
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()  # every have distance between them by line - line se separate honge
file_menu.add_command(label="Exit", command=root.quit)


# it starts and keep the window open
root.mainloop()
