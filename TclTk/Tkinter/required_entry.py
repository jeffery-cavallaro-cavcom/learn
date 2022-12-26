"""
An entry that requires a value
"""

import tkinter as tk
from tkinter import ttk

from validator import Validator

# pylint: disable=too-many-ancestors

class RequiredEntry(Validator, ttk.Entry):
    """ Required Entry """
    # pylint: disable=arguments-differ

    def validate_focusout(self, **kwargs):
        """ Strip and check for a non-blank value """
        value = self.get()
        value = value.strip() if value else ''
        self.delete(0, tk.END)
        self.insert(0, value)

        if value:
            valid = True
        else:
            self.error_var.set('A non-blank value is required')
            valid = False

        return valid

if __name__ == '__main__':
    root = tk.Tk()
    entry = RequiredEntry(root)
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
