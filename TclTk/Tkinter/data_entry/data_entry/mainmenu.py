""" Application Main Menu """

import tkinter as tk
from tkinter import messagebox

class MainMenu(tk.Menu):
    """ Main Menu """
    def __init__(self, parent, settings, **kwargs):
        """ Create the main menu """
        super().__init__(parent, **kwargs)

        self.settings = settings

        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(
            label='Select File', command=self.event('<<FileSelect>>')
        )
        file_menu.add_separator()
        file_menu.add_command(
            label='Quit', command=self.event('<<FileQuit>>')
        )
        self.add_cascade(label='File', menu=file_menu)

        options_menu = tk.Menu(self, tearoff=False)
        options_menu.add_checkbutton(
            label='Autofill Date', variable=self.settings['autofill date']
        )
        options_menu.add_checkbutton(
            label='Autofill Sheet Data',
            variable=settings['autofill sheet data']
        )
        self.add_cascade(label='Options', menu=options_menu)

        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(label='About', command=self.on_about)
        self.add_cascade(label='Help', menu=help_menu)

    @staticmethod
    def on_about(*_):
        """ Run about dialog """
        about_message = 'Data Entry Demonstration'
        about_detail = 'Version 1.0\njeffery@cavcom.com'
        messagebox.showinfo(
            title='About', message=about_message, detail=about_detail
        )

    def event(self, sequence):
        """ Define event handler """
        def callback(*_):
            root = self.master.winfo_toplevel()
            root.event_generate(sequence)
        return callback
