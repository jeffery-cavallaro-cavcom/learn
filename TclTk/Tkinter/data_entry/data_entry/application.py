""" The Data Entry Application """

import tkinter as tk
from tkinter import ttk

from model import CSVModel
from view import DataRecordForm

class Application(tk.Tk):
    """ Main Application Class """
    def __init__(self, *args, **kwargs):
        """ Create the application """
        super().__init__(*args, **kwargs)

        self.title('Data Entry')
        self.columnconfigure(0, weight=1)

        ttk.Label(
            self, text='Lab Data Entry', font=('TkDefaultFont', 16)
        ).grid(row=0)

        self.status_value = tk.StringVar()
        self.record_form = DataRecordForm(self)
        self.record_form.grid(row=1, padx=10, sticky=tk.W + tk.E)

        self.status = ttk.Label(self, textvariable=self.status_value)
        self.status.grid(row=2, padx=10, sticky=tk.W + tk.E)

        self.records_saved = 0
        self.model = CSVModel()

        self.record_form.buttons.bind('<<SaveRecord>>', self.on_save)
        self.record_form.buttons.bind('<<Quit>>', self.on_quit)

    def on_save(self, *_):
        """ Save the form values """
        errors = self.record_form.get_errors()
        if errors:
            self.status.configure(foreground='red')
            self.status_value.set(
                f"Cannot save, error in fields: {', '.join(errors.keys())}"
            )
            return

        try:
            data = self.record_form.get()
            self.model.save_record(data)
        except Exception as error:
            self.status.configure(foreground='red')
            self.status_value.set(str(error))
            return

        self.records_saved += 1
        self.status.configure(foreground='green')
        self.status_value.set(
            f"{self.records_saved} record(s) saved this session"
        )

        self.record_form.on_reset()

    def on_quit(self, *_):
        """ Quit the main loop """
        self.quit()
