import tkinter as tk

root = tk.Tk()
root.title('Going Bananas')
root.resizable(False, False)

row = 0

title = tk.Label(
    root,
    text='Banana Survey',
    font='Arial 16 bold',
    bg='brown',
    fg='yellow'
)
title.grid(row=row, column=0, columnspan=2, sticky=(tk.W + tk.E))
row += 1

name_label = tk.Label(root, text='Name:')
name_input = tk.Entry(root)
name_label.grid(row=row, column=0, pady=10)
name_input.grid(row=row, column=1, sticky=(tk.W + tk.E), padx=10, pady=10)
row += 1

eater_check = tk.Checkbutton(root, text='Do you eat bananas?')
eater_check.grid(row=row, column=0, columnspan=2, pady=10)
row += 1

number_label = tk.Label(root, text='Number eaten per day:')
number_input = tk.Spinbox(root, from_=0, to=100, increment=1)
number_label.grid(row=row, column=0)
number_input.grid(row=row, column=1, sticky=tk.W)
row += 1

color_label = tk.Label(root, text='Best banana color:')
color_choices = [
    'Any',
    'Green',
    'Green-Yellow',
    'Yellow',
    'Brown-Spotted',
    'Black'
]
color_input = tk.Listbox(root, height=1)
for color in color_choices:
    color_input.insert(tk.END, color)
color_label.grid(row=row, column=0)
color_input.grid(row=row, column=1, sticky=tk.W)
row += 1

plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
yesno = tk.BooleanVar(value=True)
plantain_yes = tk.Radiobutton(
    plantain_frame,
    text='Yes',
    variable=yesno,
    value=True
)
plantain_no = tk.Radiobutton(
    plantain_frame,
    text='No',
    variable=yesno,
    value=False
)
plantain_yes.pack(side=tk.LEFT, fill=tk.X)
plantain_no.pack(side=tk.LEFT, fill=tk.X)
plantain_label.grid(row=row, column=0)
plantain_frame.grid(row=row, column=1, sticky=tk.W, pady=10)
row += 1

comments_label = tk.Label(root, text='Comments')
comments_input = tk.Text(root, height=3)
comments_label.grid(row=row, column=0, columnspan=2)
row += 1
comments_input.grid(row=row, column=0, columnspan=2)
row += 1

submit_button = tk.Button(root, text='SUBMIT')
exit_button = tk.Button(root, text='QUIT', command=root.quit)
submit_button.grid(row=row, column=0, pady=10)
exit_button.grid(row=row, column=1, pady=10)

results = tk.Label(root, text='', anchor=tk.W, justify=tk.LEFT)

root.mainloop()
