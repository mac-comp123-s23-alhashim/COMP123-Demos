import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def do_something(color):
    if color == 'type color':
        color = simpledialog.askstring("Pick a color", "Type your color: ")
    else:
        msg = "Change background to {}?".format(color)
        yes = messagebox.askyesno('Change Color?', msg)
        if not yes:
            return

    colors_window['bg'] = color


# window
main_window = tk.Tk()
main_window.title("Main Window")

# toplevel widget: another window
colors_window = tk.Toplevel()
colors_window.master = main_window
colors_window.title("Helper Window")

width = 10
pady = 5
colors = ['red', 'green', 'blue', 'type color']
current_row = 0
for color in colors:
    color_button = tk.Button()
    color_button.master = colors_window
    color_button['width'] = width
    color_button['pady'] = pady
    color_button['text'] = color
    color_button['command'] = lambda i=color: do_something(i)
    color_button.pack()
    current_row += 1

# run
main_window.mainloop()
