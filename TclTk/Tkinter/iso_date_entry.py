"""
An entry field that accepts valid ISO-type dates (YYYY-MM-DD).
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime

from validator import Validator

# pylint: disable=too-many-ancestors

class ISODateEntry(Validator, ttk.Entry):
    """ A Date Field """
    FORMAT = '%Y-%m-%d'

    # pylint: disable=arguments-differ

    def validate_key(self, action, index, char, **kwargs):
        """ Validate current keystroke """
        valid = True

        if action == '0':
            pass
        elif index in ('0', '1', '2', '3', '5', '6', '8', '9'):
            valid = char.isdigit()
        elif index in ('4', '7'):
            valid = (char == '-')
        else:
            valid = False

        return valid

    def validate_focusout(self, **kwargs):
        valid = True

        value = self.get()
        value = value.strip() if value else None

        if value:
            try:
                datetime.strptime(value, self.FORMAT)
            except ValueError:
                self.error_var.set('Invalid date')
                valid = False
        else:
            self.error_var.set('A date value is required')
            valid = False

        return valid

if __name__ == '__main__':
    root = tk.Tk()
    entry = ISODateEntry(root)
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
