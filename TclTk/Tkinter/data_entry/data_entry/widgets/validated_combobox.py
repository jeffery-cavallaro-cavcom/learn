"""
A combo box with the following validations:
    1.  A delete action clears the box.
    2.  An partial entry is attempted to be matched to the possible entries.
    3.  Non-matching input is rejected.
"""

import tkinter as tk
from tkinter import ttk

from validator import Validator

# pylint: disable=too-many-ancestors
# pylint: disable=arguments-differ

class ValidatedCombobox(Validator, ttk.Combobox):
    """ A Validated Combobox """
    def validate_key(self, proposed, action, **kwargs):
        valid = True

        if action == '0':
            self.set('')
            return True

        values = self.cget('values')
        matching = [
            candidate for candidate in values
            if candidate.lower().startswith(proposed.lower())
        ]

        if len(matching) == 0:
            valid = False
        elif len(matching) == 1:
            self.set(matching[0])
            self.icursor(tk.END)
            valid = False

        return valid

    def validate_focusout(self, **kwargs):
        valid = True

        value = self.get().lower()
        values = self.cget('values')
        matching = [
            candidate for candidate in values
            if candidate.lower() == value
        ]

        if not matching:
            self.error_var.set('A selected value is required')
            valid = False

        return valid

if __name__ == '__main__':
    root = tk.Tk()
    entry = ValidatedCombobox(
        root, values=['zero', 'one', 'two', 'three', 'four', 'five']
    )
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
