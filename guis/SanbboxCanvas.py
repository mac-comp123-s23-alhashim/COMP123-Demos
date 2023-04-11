import tkinter as tk

def mouse_inside_canvas_response(event):
    msg = "({}, {})".format(event.x, event.y)
    mouse_position_tracker['text'] = msg

def mouse_leave_canvas_response(event):
    mouse_position_tracker['text'] = 'mouse outside canvas'

def change_bg_color(event):
    if canvas['bg'] == 'red':
        canvas['bg'] = 'yellow'
    else:
        canvas['bg'] = 'red'

def draw_horizontal_line(event):
    start_x = 0
    start_y = event.y
    end_x = canvas['width']
    end_y = event.y
    canvas.create_line(start_x, start_y,
                       end_x, end_y)


def draw_circel(event):
    start_x = event.x - 5
    start_y = event.y - 5
    end_x = event.x + 5
    end_y = event.y + 5

    shape_ids = canvas.find_overlapping(start_x, start_y, end_x, end_y)
    if len(shape_ids) != 0:
        for shape_id in shape_ids:
            canvas.delete(shape_id)
        print(shape_ids)
        return

    canvas.create_oval(start_x, start_y,
                       end_x, end_y)


def draw_vertical_line(event):
    start_x = event.x
    start_y = 0
    end_x = event.x
    end_y = canvas['height']
    canvas.create_line(start_x, start_y,
                       end_x, end_y)


def draw_vertical_and_horizontal_lines(event):
    draw_vertical_line(event)
    draw_horizontal_line(event)


def type_key(event):
    if event.keysym in ['Control_L', 'Control_R', 'Shift_L', 'Shift_R', 'Caps_Lock']:
        return

    canvas.create_text(event.x, event.y-21, text=event.keysym)


# window (Tk object)
window = tk.Tk()

# label ------------------------------------------------------------------------
mouse_position_tracker = tk.Label()
mouse_position_tracker.master = window
# where to place
mouse_position_tracker.grid(row=0, column=0)


# Canvas -----------------------------------------------------------------------
canvas = tk.Canvas()
canvas.master = window
canvas['bg'] = "red"
canvas['height'] = 500
canvas['width'] = 500
# bind callbacks to some keys
canvas.bind("<Motion>", mouse_inside_canvas_response)
canvas.bind("<Leave>", mouse_leave_canvas_response)
canvas.bind("<Button-3>", change_bg_color)
canvas.bind('<Button-1>', draw_circel)
canvas.bind('<Control-Button-1>', draw_vertical_line)
canvas.bind('<Shift-Button-1>', draw_horizontal_line)
canvas.bind('<Shift-Control-Button-1>', draw_vertical_and_horizontal_lines)
canvas.bind_all('<Key>', type_key)
# where to place
canvas.grid(row=1, column=0)

# run
window.mainloop()
