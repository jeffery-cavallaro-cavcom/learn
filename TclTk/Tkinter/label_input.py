""" An input widget with an attached label """

import tkinter as tk
from tkinter import ttk

class LabelInput(tk.Frame):
    """ Label plus Input Widget """
    def __init__(
        # pylint: disable=too-many-arguments
        self,
        parent,
        label,
        textvariable,
        input_class=ttk.Entry,
        input_args=None,
        label_args=None,
        **kwargs
    ):
        """ Construct a new label with input widget """
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.value = textvariable

        if input_class in (ttk.Checkbutton, ttk.Button):
            input_args['text'] = label
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=tk.W + tk.E)

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["variable"] = self.value
        else:
            input_args["textvariable"] = self.value

        if input_class == ttk.Radiobutton:
            self.input = tk.Frame(self)
            for value in input_args.pop('values', []):
                button = ttk.Radiobutton(
                    self.input, value=value, text=value, **input_args
                )
                button.pack(
                    side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill=tk.X
                )
        else:
            self.input = input_class(self, **input_args)

        self.input.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.W + tk.E), **kwargs):
        """ Add default sticky argument to grid """
        super().grid(sticky=sticky, **kwargs)
