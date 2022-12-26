"""
An entry that requires a value
"""

import tkinter as tk
from tkinter import ttk

from validator import Validator

class RequiredEntry(Validator, ttk.Entry):
    """ Required Entry """
    def validate_focusout(self, event):
        """ Strip and check for a non-blank value """
        value = self.get()
        value = value.strip() if value else ''
        self.delete(0, tk.END)
        self.insert(0, value)

        if value:
            valid = True
        else:
            self.error_var.set('A value is required')
            valid = False

        return valid

if __name__ == '__main__':
    root = tk.Tk()
    entry = RequiredEntry(root)
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
