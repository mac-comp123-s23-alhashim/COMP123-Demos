import tkinter as tk

def do_something(color):
    main_window['bg'] = color

# window
main_window = tk.Tk()
main_window.title("Main Window")
main_window['width'] = 500

# toplevel widget: another window
colors_window = tk.Toplevel()
colors_window.master = main_window
colors_window.title("Helper Window")
colors_window['width'] = 500

width = 10
pady = 5
colors = ['red', 'green', 'blue']
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
