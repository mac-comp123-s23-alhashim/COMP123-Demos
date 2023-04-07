import tkinter as tk


class BasicGui:
    def __init__(self):
        self.root_win1 = tk.Tk()
        self.root_win1.title("Window 1")
        self.root_win1.config(bg="blue")

        self.lablel1 = \
            tk.Label(self.root_win1,
                     text="Hello World",
                     font="Arial 18 bold",
                     bg="red",
                     relief=tk.GROOVE,
                     justify=tk.CENTER,
                     padx=10,
                     pady=10)
        self.lablel1.grid(row=0, column=0)

        lablel2 = \
            tk.Label(self.root_win1,
                     text="COMP 123",
                     font="Arial 18 bold",
                     bg="yellow",
                     relief=tk.GROOVE,
                     justify=tk.CENTER,
                     padx=10,
                     pady=10)
        lablel2.grid(row=1, column=0)

        botton1 = \
            tk.Button(self.root_win1,
                      text="Click Me",
                      command=self.botton1_response)
        botton1.grid(row=2, column=1)

        quit_button = \
            tk.Button(self.root_win1,
                      text="Quit",
                      command=self.quit_button_response)
        quit_button.grid(row=3, column=1)

        enlarge_button = \
            tk.Button(self.root_win1,
                      text="+",
                      command=self.enlarge_button_response)
        enlarge_button.grid(row=4, column=0)

        shrink_button = \
            tk.Button(self.root_win1,
                      text="-",
                      command=self.shrink_button_response)
        shrink_button.grid(row=4, column=1)


        # self.root_win2 = tk.Tk()
        # self.root_win2.title("Window 2")
        # self.root_win2.config(bg="yellow")

    def run(self):
        self.root_win1.mainloop()
        # self.root_win2.mainloop()

    def botton1_response(self):
        print("Button was pressed")

    def quit_button_response(self):
        self.root_win1.destroy()

    def enlarge_button_response(self):
        self.lablel1["font"] = "Arial 20 bold"
    def shrink_button_response(self):
        self.lablel1["font"] = "Arial 10 bold"

myBasicGui = BasicGui()
myBasicGui.run()
