""" A Frame with a Label and Border """

import tkinter as tk
from tkinter import ttk

# pylint: disable=too-many-ancestors

class LabeledFrame(ttk.LabelFrame):
    """ Frame with Label and Border """
    def __init__(self, parent, label, columns=3):
        """ Create a new labeled frame """
        super().__init__(parent, text=label)
        self.grid(sticky=tk.W + tk.E)
        for icol in range(columns):
            self.columnconfigure(icol, weight=1)
