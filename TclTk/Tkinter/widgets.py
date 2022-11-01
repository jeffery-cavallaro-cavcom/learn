"""
This interactive application demonstrates the use of the basic Ttk widgets.
"""

import tkinter as tk
from tkinter import ttk
from turtle import bgcolor

root = tk.Tk()
root.title('widgets')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

row = 0
sides = tk.W + tk.E
all = sides + tk.N + tk.S

ttk.Label(
    root,
    text='Widget Examples',
    background='green',
    foreground='yellow',
    anchor=tk.CENTER,
).grid(row=row, column=0, columnspan=2, sticky=sides, ipady=5)

row += 1

ttk.Label(root, text='Entry:', anchor=tk.CENTER).grid(
    row=row, column=0, sticky=sides, pady=5
)
ttk.Entry(root).grid(row=row, column=1, sticky=sides, padx=10, pady=10)

row += 1

ttk.Label(root, text='Count:', anchor=tk.CENTER).grid(
    row=row, column=0, sticky=sides, pady=5
)
counter = tk.IntVar(value=0)
ttk.Spinbox(
    root,
    from_=0,
    to=100,
    increment=10,
    textvariable=counter
).grid(row=row, column=1, sticky=sides, padx=10)

row += 1

ttk.Label(root, text='Direction:', anchor=tk.CENTER).grid(
    row=row, column=0, sticky=sides, pady=5
)
compass = tk.StringVar(value='North')
ttk.Spinbox(
    root,
    textvariable=compass,
    values=['North', 'South', 'East', 'West']
).grid(row=row, column=1, sticky=sides, padx=10)

row += 1

checker = tk.BooleanVar(value=False)
check_label = tk.StringVar(value='off')

def toggle():
    value = checker.get()
    checker.set(value=value)
    check_label.set('on' if value else 'off')

ttk.Checkbutton(
    root,
    textvariable=check_label,
    variable=checker,
    command=toggle
).grid(row=row, column=0, columnspan=2, pady=5)

row += 1

frame = ttk.LabelFrame(text='Selection')
letter = tk.StringVar(value='A')
for iletter in range(ord('A'), ord('D')):
    tletter = chr(iletter)
    ttk.Radiobutton(
        frame, text=tletter, variable=letter, value=tletter
    ).pack()
frame.grid(row=row, column=0, columnspan=2, padx=10, pady=5, sticky=sides)

row += 1

ttk.Label(root, text='Choice:', anchor=tk.CENTER).grid(
    row=row, column=0, sticky=sides
)
choice = tk.StringVar(value='Jeffery')
ttk.Combobox(
    textvariable=choice,
    values = [
        'Jeffery',
        'Leila',
        'April',
        'Peter',
        'Jay',
        'Ruca',
        'Tommie'
    ]
).grid(row=row, column=1, pady=5, sticky=tk.W)

row += 1

ttk.Label(root, text='Comment', anchor=tk.CENTER).grid(
    row=row, column=0, columnspan=2, sticky=sides, pady=10
)
row += 1
tk.Text(
    height=5,
    undo=True,
    maxundo=10,
    wrap=tk.CHAR
).grid(row=row, column=0, columnspan=2, sticky=all, padx=10, pady=10)

row += 1

ttk.Button(
    text='QUIT', command=root.quit, default=tk.ACTIVE
).grid(row=row, column=0, columnspan=2, pady=10)

tk.mainloop()
