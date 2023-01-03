""" Demonstrates a message dialog """

import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    """ Message Dialog Demonstration"""
    def __init__(self):
        """ Create the application """
        super().__init__()
        self.title('Dialog test')
        tk.Button(text='Quit', command=self.on_quit).pack()

    def on_quit(self):
        """ Run the message dialog """
        if messagebox.askyesno(
            title='confirm',
            message='Do you really want to quit?',
            detail='Click No to cancel'
        ):
            self.quit()

if __name__ == '__main__':
    Application().mainloop()
