import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.simpledialog
from tkinter import scrolledtext

root = tk.Tk()
root.title("(t)ext")
root.geometry("1920x1080")

text_editor = scrolledtext.ScrolledText(root, width=1920, height=1080, undo=True)
text_editor.pack()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "(t)ext 1.0\nDeveloped by Teslaboi_3000"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

def new_file():
    text_editor.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))

root.mainloop()