import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import StringVar
import re
import time

root  = tk.Tk()
root.title("(t)ext")
root.geometry("1920x1080")

style  = ttk.Style()
style.theme_use('clam')

text_editor  = scrolledtext.ScrolledText(root, width=1920, height=1080, undo=True)
text_editor.config(insertbackground='white')
text_editor.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: text_editor.delete(1.0, tk.END))
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

options_menu = tk.Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Switch to Dark Mode", command=lambda: switch_to_dark_mode())
menu_bar.add_cascade(label="Options", menu=options_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "(t)ext 1.0.2 (testing)\nDeveloped by Teslaboi_3000"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

def open_file():
    file_path  = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, file.read())
            highlight_python_code()

def save_file():
    file_path  = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))
        highlight_python_code()

def switch_to_dark_mode():
    if text_editor.cget('bg') == 'black':
        text_editor.configure(bg='white', fg='black')
    else:
        text_editor.configure(bg='black', fg='white')

def highlight_python_code():
    text = text_editor.get(1.0, tk.END)
    lines = text.splitlines()
    line_count = 0
    column = 0
    for line in lines:
        line_words = line.split()
        for word in line_words:
            line_count += 1
            start_index = f'{line_count}.{column}'
            end_index = f'{line_count}.{column + len(word)}'
            text_editor.tag_add('python', start_index, end_index)
            if word.lower() in ['print', 'def', 'class', 'if', 'else', 'for', 'while', 'try', 'except', 'finally', 'import']:
                text_editor.tag_add('python', start_index, end_index)
            elif word.lower() in ['true', 'false', 'none']:
                text_editor.tag_add('boolean', start_index, end_index)
            elif word.lower() in ['str', 'int', 'float', 'list', 'dict']:
                text_editor.tag_add('type', start_index, end_index)
            column += len(word) + 1
    text_editor.tag_config('python', foreground='blue')
    text_editor.tag_config('boolean', foreground='green')
    text_editor.tag_config('type', foreground='purple')

def update_highlight():
    highlight_python_code()
    root.after(1, update_highlight) 

update_highlight()

root.mainloop()