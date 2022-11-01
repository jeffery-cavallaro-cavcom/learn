"""
This interactive application is a banana survey that demonstrates the use of
the various plain Tk widgets.
"""

import tkinter as tk

root = tk.Tk()
root.title('Going Bananas')
root.resizable(False, False)

row = 0

tk.Label(
    root,
    text='Banana Survey',
    font='Arial 16 bold',
    bg='brown',
    fg='yellow'
).grid(row=row, column=0, columnspan=2, sticky=(tk.W + tk.E))
row += 1

name_value = tk.StringVar()
tk.Label(root, text='Name:').grid(row=row, column=0, pady=10)
tk.Entry(root, textvariable=name_value).grid(
    row=row, column=1, sticky=(tk.W + tk.E), padx=10, pady=10
)
row += 1

eater_value = tk.BooleanVar()
tk.Checkbutton(root, text='Do you eat bananas?', variable=eater_value).grid(
    row=row, column=0, columnspan=2, pady=10
)
row += 1

number_value = tk.IntVar(value=0)
tk.Label(root, text='Number eaten per day:').grid(row=row, column=0)
tk.Spinbox(
    root, from_=0, to=100, increment=1, textvariable=number_value
).grid(row=row, column=1, sticky=tk.W)
row += 1

tk.Label(root, text='Best banana color:').grid(row=row, column=0)
color_choices = [
    'Any',
    'Green',
    'Green-Yellow',
    'Yellow',
    'Brown-Spotted',
    'Black'
]
color_value = tk.StringVar(value=color_choices[0])
tk.OptionMenu(root, color_value, *color_choices).grid(
    row=row, column=1, sticky=tk.W
)
row += 1

plaintain_value = tk.BooleanVar(value=True)
tk.Label(root, text='Do you eat plantains?').grid(row=row, column=0)
plantain_frame = tk.Frame(root)
tk.Radiobutton(
    plantain_frame, text='Yes', variable=plaintain_value, value=True
).pack(side=tk.LEFT, fill=tk.X)
tk.Radiobutton(
    plantain_frame, text='No', variable=plaintain_value, value=False
).pack(side=tk.LEFT, fill=tk.X)
plantain_frame.grid(row=row, column=1, sticky=tk.W, pady=10)
row += 1

tk.Label(root, text='Comments').grid(row=row, column=0, columnspan=2)
row += 1
comments_input = tk.Text(root, height=3)
comments_input.grid(row=row, column=0, columnspan=2)
row += 1

def on_submit():
    message = f"Thanks for taking the survey, {name_value.get()}.\n"
    valid = True
    results.configure(fg='black')

    if eater_value.get():
        color = color_value.get()
        try:
            message += f"Enjoy your {number_value.get()} {color} bananas!\n"
        except tk.TclError:
            message = "Invalid number of bananas"
            valid = False
    else:
        message += 'So sorry that you do not like bananas!\n'

    if valid:
        if plaintain_value.get():
            message += 'Enjoy your plantains!'
        else:
            message += 'Avoid those icky plantains!'
    else:
        results.configure(fg='red')

    comments = comments_input.get('1.0', tk.END)
    results_value.set(value=message)
    print(comments)
 
submit_button = tk.Button(root, text='SUBMIT', command=on_submit)
exit_button = tk.Button(root, text='QUIT', command=root.quit)
submit_button.grid(row=row, column=0, pady=10)
exit_button.grid(row=row, column=1, pady=10)
row += 1

results_value = tk.StringVar()
results = tk.Label(
    root, text='', anchor=tk.W, justify=tk.LEFT, textvariable=results_value
)
results.grid(row=row, column=0, columnspan=2)

root.mainloop()
