import tkinter as tk
from tkinter import ttk
import math

def mile_changed(event):
    km_value.set(round(mile_value.get() * 1.61, 2))
    # km_value.set(mile_value.get() * 1.61)


def km_changed(event):
    mile_value.set(round(km_value.get() / 1.61, 2))
    # mile_value.set(km_value.get() / 1.61)


# window
window = tk.Tk()
window.title("Mile-KM Converter App")
window.geometry("300x100")

# mile frame -------------------------------------------------------------------
mile_frame = ttk.Frame(master=window)
mile_frame.pack()

mile_label = ttk.Label(master=mile_frame, text="Mile: ")
mile_label.pack(side='left')

mile_value = tk.DoubleVar()
mile_input = ttk.Entry(master=mile_frame, textvariable=mile_value)
mile_input.bind('<KeyRelease>', mile_changed)
mile_input.pack(side='left')

# mile frame -------------------------------------------------------------------
km_frame = ttk.Frame(master=window)
km_frame.pack()

km_label = ttk.Label(master=km_frame, text="KM: ")
km_label.pack(side='left')

km_value = tk.DoubleVar()
km_input = ttk.Entry(master=km_frame, textvariable=km_value)
km_input.bind('<KeyRelease>', km_changed)
km_input.pack(side='left')

# run --------------------------------------------------------------------------
window.mainloop()
