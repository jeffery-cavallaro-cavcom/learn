"""
An entry that limits the number of allowed characters.
"""

import tkinter as tk
from tkinter import ttk

class LimitedEntry(tk.Entry):
    """ Limited Entry """
    def __init__(
        self, parent, *args, max_chars=10, error_var=None, **kwargs
    ):
        """ Create an entry widget"""
        super().__init__(parent, *args, **kwargs)
        self.max_chars = max_chars
        self.error_var = error_var
        self.configure(
            validate='all',
            validatecommand=(self.register(self.limit_length), '%P'),
            invalidcommand=(self.register(self.set_error), '%P')
        )

    def limit_length(self, proposed):
        """ Check the proposed length """
        if self.error_var:
            self.error_var.set('')
        return len(proposed) <= self.max_chars

    def set_error(self, proposed):
        """ Set error string """
        if self.error_var:
            message = (
                f"'{proposed}' is too long; only {self.max_chars} "
                'characters are allowed'
            )
            self.error_var.set(message)

if __name__ == '__main__':
    root = tk.Tk()
    error_var = tk.StringVar()
    entry = LimitedEntry(root, max_chars=5, error_var=error_var)
    error_label = ttk.Label(root, textvariable=error_var, foreground='red')
    entry.grid(sticky=tk.W+tk.E, padx=10, pady=10)
    error_label.grid(sticky=tk.W+tk.E, padx=10, pady=10)
    root.columnconfigure(0, weight=1)
    root.mainloop()
