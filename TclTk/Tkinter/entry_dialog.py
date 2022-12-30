""" Entry Dialog Demonstration """

import tkinter as tk
from tkinter import simpledialog

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bird is the Word')

        self.word = tk.StringVar()
        tk.Label(textvariable=self.word).pack()

        tk.Button(text='Enter Word', command=self.on_enter).pack()

    def on_enter(self, *_):
        word = simpledialog.askstring('Word', 'What is the word?')
        if word:
            self.word.set(word)
            if word.lower() == 'bird':
                self.quit()

if __name__ == '__main__':
    Application().mainloop()
