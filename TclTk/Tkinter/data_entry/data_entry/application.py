""" The Data Entry Application """

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from model import CSVModel
from view import DataRecordForm, LoginDialog
from mainmenu import MainMenu

class Application(tk.Tk):
    """ Main Application Class """
    def __init__(self, *args, **kwargs):
        """ Create the application """
        super().__init__(*args, **kwargs)

        self.withdraw()
        if not self.show_login():
            self.destroy()
            return
        self.deiconify()

        self.title('Data Entry')
        self.columnconfigure(0, weight=1)

        event_callbacks = {
            '<<FileSelect>>': self.on_file_select,
            '<<FileQuit>>': lambda _: self.quit()
        }
        for sequence, callback in event_callbacks.items():
            self.bind(sequence, callback)

        self.settings = {
            'autofill date': tk.BooleanVar(value=True),
            'autofill sheet data': tk.BooleanVar(value=True)
        }

        menu = MainMenu(self, self.settings)
        self.configure(menu=menu)

        ttk.Label(
            self, text='Lab Data Entry', font=('TkDefaultFont', 16)
        ).grid(row=0)

        self.status_value = tk.StringVar()
        self.record_form = DataRecordForm(self, self.settings)
        self.record_form.grid(row=1, padx=10, sticky=tk.W + tk.E)

        self.status = ttk.Label(self, textvariable=self.status_value)
        self.status.grid(row=2, padx=10, sticky=tk.W + tk.E)

        self.records_saved = 0
        self.model = CSVModel()

        self.record_form.buttons.bind('<<SaveRecord>>', self.on_save)
        self.record_form.buttons.bind('<<Quit>>', self.on_quit)

    def on_file_select(self, *_):
        """ Select an output CSV file """
        filename = filedialog.asksaveasfilename(
            title='Select the target file for saving records',
            defaultextension='.csv',
            filetypes=[('CSV', '*.csv *.CSV')]
        )
        if filename:
            self.model = CSVModel(filename)

    def on_save(self, *_):
        """ Save the form values """
        errors = self.record_form.get_errors()
        if errors:
            self.status.configure(foreground='red')
            self.status_value.set(
                f"Cannot save, error in fields: {', '.join(errors.keys())}"
            )

            message = 'Cannot save record'
            detail = (
                'The following fields have errors:'
                "\n  * {}".format('\n  * '.join(errors.keys()))
            )
            messagebox.showerror(title='Error', message=message, detail=detail)

            return

        # pylint: disable=broad-except
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

    def show_login(self):
        """ Run the login dialog """
        error = ''
        title = 'Data Entry Login'

        while True:
            login = LoginDialog(self, title, error)
            if not login.result:
                return False
            username, password = login.result
            if self.simple_login(username, password):
                return True
            error = 'Login Failed'

    @staticmethod
    def simple_login(username, password):
        """ Overly simple authentication """
        return (username == 'admin') and (password == 'data')
