"""
A sandbox to play with Tkinter based on the document written by Susan Fox
https://docs.google.com/document/d/1S6xWzzMEF30FI0WBbxxZTI4m335kiA_wEVvuLztkNfE/preview

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""

import tkinter as tk


class BasicGui:
    def __init__(self):
        # window object
        self.root_win1 = tk.Tk()
        self.root_win1.title("Window 1")
        self.root_win1.config(bg="blue")

        # bind the whole window to key presses
        # binding levels: https://tkdocs.com/shipman/binding-levels.html
        self.root_win1.bind_all('<KeyPress-Caps_Lock>',
                                self.canvas_response)

        # label ----------------------------------------------------------------
        # setting attributes using the constructor (initializer) approach
        self.label1 = \
            tk.Label(self.root_win1,
                     text="18",
                     font="Arial 18 bold",
                     bg="red",
                     relief=tk.GROOVE,
                     justify=tk.CENTER,
                     padx=10,
                     pady=10)
        # specify where to place the widget (layout) using the grid approach
        self.label1.grid(row=0, column=0)

        # label ----------------------------------------------------------------
        # setting attributes using the dictionary approach
        label2 = tk.Label(self.root_win1)
        label2['text'] = "COMP 123"
        label2['font'] = "Arial 18 bold"
        label2['bg'] = "yellow"
        label2['relief'] = tk.GROOVE
        label2['justify'] = tk.CENTER
        label2['padx'] = 10
        label2['pady'] = 10
        # specify where to place the widget (layout) using the grid approach
        label2.grid(row=1, column=0)

        # button ---------------------------------------------------------------
        # setting attributes using the config method
        button1 = tk.Button(self.root_win1)
        button1.config(
            text="Print Something to Council",
            command=self.button1_response)
        # specify where to place the widget (layout) using the grid approach
        button1.grid(row=1, column=1)

        # button ---------------------------------------------------------------
        # setting attributes using the constructor (initializer) approach
        quit_button = \
            tk.Button(self.root_win1,
                      text="Quit App",
                      command=self.quit_button_response)
        # specify where to place the widget (layout) using the grid approach
        quit_button.grid(row=0, column=1)

        # button ---------------------------------------------------------------
        # setting attributes using the dictionary approach
        enlarge_button = tk.Button(self.root_win1)
        enlarge_button['text'] = "+"
        enlarge_button['width'] = 30
        enlarge_button['command'] = self.enlarge_button_response
        # specify where to place the widget (layout) using the grid approach
        enlarge_button.grid(row=4, column=0)

        # button ---------------------------------------------------------------
        # setting attributes using the config method
        shrink_button = tk.Button(self.root_win1)
        shrink_button.config(
            text="-",
            width=30,
            command=self.shrink_button_response)
        # specify where to place the widget (layout) using the grid approach
        shrink_button.grid(row=4, column=1)

        # Frame ----------------------------------------------------------------
        # setting attributes using the dictionary approach
        left_frame = tk.Frame(self.root_win1)
        left_frame['pady'] = 20
        left_frame['width'] = 100
        # specify where to place the widget (layout) using the grid approach
        left_frame.grid(row=5, column=0)

        # Label ----------------------------------------------------------------
        # setting attributes using the dictionary approach
        instruction_label = tk.Label(left_frame)
        instruction_label['text'] = 'type something and hit Enter or Tab to ' \
                                    'reverse'
        # specify where to place the widget (layout) using the grid approach
        instruction_label.grid(row=0, column=0)

        # Entry ----------------------------------------------------------------
        # setting attributes using the constructor (initializer) approach
        self.name_entry = \
            tk.Entry(left_frame,
                     justify=tk.CENTER,
                     width=30)
        # binding callbacks to key presses
        self.name_entry.bind('<Return>', self.name_entry_response)
        self.name_entry.bind('<Tab>', self.name_entry_response)
        # specify where to place the widget (layout) using the grid approach
        self.name_entry.grid(row=1, column=0)

        # button ---------------------------------------------------------------
        # setting attributes using the config method
        count_button = tk.Button(self.root_win1)
        count_button.config(
            text="find length of input",
            width=30,
            command=self.find_input_length)
        # specify where to place the widget (layout) using the grid approach
        count_button.grid(row=5, column=1)



        # another window
        self.root_win2 = tk.Tk()
        self.root_win2.title("Window 2")
        self.root_win2.config(bg="yellow")

    def run(self):
        self.root_win1.mainloop()
        # self.root_win2.mainloop()

    def button1_response(self):
        print("Button was pressed")

    def canvas_response(self, event):
        print(event)

    def quit_button_response(self):
        self.root_win1.destroy()

    def enlarge_button_response(self):
        current_val = int(self.label1['text']) + 1
        self.label1['text'] = current_val
        self.label1['font'] = 'Arial ' + str(current_val) + ' bold'

    def shrink_button_response(self):
        current_val = int(self.label1['text']) - 1
        self.label1['text'] = current_val
        self.label1['font'] = 'Arial ' + str(current_val) + ' bold'

    def find_input_length(self):
        self.label1['text'] = len(self.name_entry.get())
        self.name_entry.delete(0, tk.END)

    def name_entry_response(self, event):
        if event.keysym == 'Return':
            print("Return pressed")
        elif event.keysym == 'Tab':
            print("Tab pressed")

        txt = self.name_entry.get()
        rev_txt = txt[::-1]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, rev_txt)


if __name__ == '__main__':
    myBasicGui = BasicGui()  # create object of BasicGui class
    myBasicGui.run()         # call the run method of the class
