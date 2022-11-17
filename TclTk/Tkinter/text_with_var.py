""" Text Widget with a String Control Variable """

import tkinter as tk

class TextWithVar(tk.Text):
    """ Text with Variable """
    def __init__(self, *args, **kwargs):
        """ Initialize the widget combination """
        super().__init__(*args, **kwargs)
        self.value = tk.StringVar(self)
        self.value.trace_add('write', self.on_set_value)
        self.value.trace_add('read', self.on_get_value)

    def on_set_value(self, *_):
        """ Update text widget """
        self.delete('1.0', tk.END)
        self.insert('1.0', self.value.get())

    def on_get_value(self, *_):
        """ Update control variable """
        self.value.set(self.get('1.0', 'end-1chars'))
