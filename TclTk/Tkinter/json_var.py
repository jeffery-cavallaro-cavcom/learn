"""
This class is a subclass of StringVar that stores a JSON string.  Thus, it can
be used for list and dict values.
"""

import json
import tkinter as tk

class JSONVar(tk.StringVar):
    """ A JSON string control variable """
    def __init__(self, *args, **kwargs):
        """ Initialize the value """
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        """ Set JSON value from object """
        super().set(json.dumps(value), *args, **kwargs)

    def get(self, *args, **kwargs):
        """ Get object from JSON value """
        return json.loads(super().get(*args, **kwargs))

if __name__ == '__main__':
    root = tk.Tk()
    var = JSONVar(root, value=[1, 2, 3])
    print(var.get())
    var = JSONVar(root)
    print(var.get())
    var.set({'a': 1, 'b': 2})
    print(var.get())
