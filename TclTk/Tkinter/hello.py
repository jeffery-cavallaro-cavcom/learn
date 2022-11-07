""" A hello world form """

import tkinter as tk

root = tk.Tk()
root.title('Hello')
root.geometry('300x150')
root.resizable(False, False)

text = tk.StringVar(value='enter something here')

widgets = [
    tk.Label(root, text='Hello, World !!!', bg='green', fg='yellow'),
    tk.Entry(root, textvariable=text),
    tk.Button(root, text='QUIT', command=root.quit)
]
for widget in widgets:
    widget.pack(padx=10, pady=10)

root.mainloop()
print(f"text=\"{text.get()}\"")
