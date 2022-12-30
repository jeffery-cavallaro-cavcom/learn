"""
Ensures that at least one radio button is selected.
"""

import tkinter as tk
from tkinter import ttk

# pylint: disable=too-many-ancestors

class ValidatedRadioGroup(ttk.Frame):
    """ A Validate Radio Button Group """
    def __init__(
        self,
        *args,
        variable=None,
        error_var=None,
        values=None,
        button_args=None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.variable = variable or tk.StringVar()
        self.error_var = error_var or tk.StringVar()
        self.values = values or []
        self.button_args = button_args or {}

        for value in self.values:
            ttk.Radiobutton(
                self,
                value=value,
                text=value,
                variable=self.variable,
                **self.button_args
            ).pack(
                side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill=tk.X
            )

        self.bind('<FocusOut>', self.on_focusout)

    def on_focusout(self, *_):
        """ Enforce a selection """
        self.error_var.set('')
        if not self.variable.get():
            self.error_var.set('An option must be selected')

if __name__ == '__main__':
    root = tk.Tk()
    entry = ValidatedRadioGroup(
        root, values=['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    )
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
