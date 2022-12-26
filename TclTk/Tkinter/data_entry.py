"""
This interactive application is an example of a form using the Ttk widgets.
The form is used to enter collected data from a fictitious agricultural lab.
The entered data is appended to a CSV file.
"""

import tkinter as tk
from tkinter import ttk

from datetime import datetime
from pathlib import Path
import csv
import sys

from text_with_var import TextWithVar
from label_input import LabelInput

# pylint: disable=too-many-ancestors

class LabeledFrame(ttk.LabelFrame):
    """ Frame with Label and Border """
    def __init__(self, parent, label, columns=3):
        """ Create a new labeled frame """
        super().__init__(parent, text=label)
        self.grid(sticky=tk.W + tk.E)
        for icol in range(columns):
            self.columnconfigure(icol, weight=1)

class RecordInfo(LabeledFrame):
    """ Record Information Box """
    def __init__(self, parent, variables):
        """ Create the record information box """
        super().__init__(parent, 'Record Information')

        LabelInput(self, 'Date', variables['Date']).grid(row=0, column=0)

        LabelInput(
            self,
            'Time',
            variables['Time'],
            input_class=ttk.Combobox,
            input_args={'values': ['8:00', '12:00', '16:00', '20:00']}
        ).grid(row=0, column=1)


        LabelInput(
            self, 'Technician', variables['Technician']
        ).grid(row=0, column=2)

        LabelInput(
            self,
            'Lab',
            variables['Lab'],
            input_class=ttk.Radiobutton,
            input_args={'values': ['A', 'B', 'C']}
        ).grid(row=1, column=0)

        LabelInput(
            self,
            'Plot',
            variables['Plot'],
            input_class=ttk.Combobox,
            input_args={'values': list(range(1, 21))}
        ).grid(row=1, column=1)

        LabelInput(
            self, 'Seed Sample', variables['Seed Sample']
        ).grid(row=1, column=2)

class EnvironmentInfo(LabeledFrame):
    """ Environment Information Box """
    HUMIDITY = "Humidity (g/m\u00B3)"
    LIGHT = 'Light (klx)'
    # pylint: disable=consider-using-f-string
    TEMPERATURE = "Temperature ({}C)".format('\u00B0')
    EQUIPMENT_FAULT = 'Equipment Fault'

    def __init__(self, parent, variables):
        """ Create the environment information box """
        super().__init__(parent, 'Environment Data')

        LabelInput(
            self,
            self.HUMIDITY,
            variables[self.HUMIDITY],
            input_class=ttk.Spinbox,
            input_args={'from_': 0.5, 'to_': 52.0, 'increment': 0.01}
        ).grid(row=0, column=0)

        LabelInput(
            self,
            self.LIGHT,
            variables[self.LIGHT],
            input_class=ttk.Spinbox,
            input_args={'from_': 0.0, 'to_': 100.0, 'increment': 0.01}
        ).grid(row=0, column=1)

        LabelInput(
            self,
            self.TEMPERATURE,
            variables[self.TEMPERATURE],
            input_class=ttk.Spinbox,
            input_args={'from_': 4.0, 'to_': 40.0, 'increment': 0.01}
        ).grid(row=0, column=2)

        LabelInput(
            self,
            self.EQUIPMENT_FAULT,
            variables[self.EQUIPMENT_FAULT],
            input_class=ttk.Checkbutton
        ).grid(row=1, column=0)

class PlantInfo(LabeledFrame):
    """ Plant Information Box """
    MIN_HEIGHT = 'Min Height (cm)'
    MAX_HEIGHT = 'Max Height (cm)'
    MEDIAN_HEIGHT = 'Median Height (cm)'

    def __init__(self, parent, variables):
        """ Create the plant information box """
        super().__init__(parent, 'Plant Data')

        LabelInput(
            self,
            'Plants',
            variables['Plants'],
            input_class=ttk.Spinbox,
            input_args={'from_': 0, 'to_': 20, 'increment': 1}
        ).grid(row=0, column=0)

        LabelInput(
            self,
            'Blossoms',
            variables['Blossoms'],
            input_class=ttk.Spinbox,
            input_args={'from_': 0, 'to_': 1000, 'increment': 1}
        ).grid(row=0, column=1)

        LabelInput(
            self,
            'Fruit',
            variables['Fruit'],
            input_class=ttk.Spinbox,
            input_args={'from_': 0, 'to_': 1000, 'increment': 1}
        ).grid(row=0, column=2)

        LabelInput(
            self,
            self.MIN_HEIGHT,
            variables[self.MIN_HEIGHT],
            input_class=ttk.Spinbox,
            input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
        ).grid(row=1, column=0)

        LabelInput(
            self,
            self.MAX_HEIGHT,
            variables[self.MAX_HEIGHT],
            input_class=ttk.Spinbox,
            input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
        ).grid(row=1, column=1)

        LabelInput(
            self,
            self.MEDIAN_HEIGHT,
            variables[self.MEDIAN_HEIGHT],
            input_class=ttk.Spinbox,
            input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
        ).grid(row=1, column=2)

class ButtonBar(ttk.Frame):
    """ All the Buttons """
    def __init__(self, parent):
        """ Create the button bar """
        super().__init__(parent)

        self.grid(sticky=tk.W + tk.E)

        ttk.Button(
            self, text='Quit', command=self.master.master.quit
        ).pack(side=tk.RIGHT)

        ttk.Button(
            self, text='Save', command=self.master.master.on_save
        ).pack(side=tk.RIGHT)

        ttk.Button(
            self, text='Reset', command=self.master.on_reset
        ).pack(side=tk.RIGHT)

class DataRecordForm(ttk.Frame):
    """ All of the form data """
    def __init__(self, *args, **kwargs):
        """ Construct the form """
        super().__init__(*args, **kwargs)

        self.variables = {
            'Date': tk.StringVar(),
            'Time': tk.StringVar(),
            'Technician': tk.StringVar(),
            'Lab': tk.StringVar(),
            'Plot': tk.IntVar(),
            'Seed Sample': tk.StringVar(),
            EnvironmentInfo.HUMIDITY: tk.DoubleVar(),
            EnvironmentInfo.LIGHT: tk.DoubleVar(),
            EnvironmentInfo.TEMPERATURE: tk.DoubleVar(),
            EnvironmentInfo.EQUIPMENT_FAULT: tk.BooleanVar(),
            'Plants': tk.IntVar(),
            'Blossoms': tk.IntVar(),
            'Fruit': tk.IntVar(),
            PlantInfo.MIN_HEIGHT: tk.DoubleVar(),
            PlantInfo.MAX_HEIGHT: tk.DoubleVar(),
            PlantInfo.MEDIAN_HEIGHT: tk.DoubleVar(),
            'Notes': tk.StringVar()
        }

        RecordInfo(self, self.variables)
        EnvironmentInfo(self, self.variables)
        PlantInfo(self, self.variables)

        LabelInput(
            self,
            'Notes',
            self.variables['Notes'],
            input_class=TextWithVar,
            input_args={'width': 75, 'height': 10}
        ).grid()

        ButtonBar(self)

    def on_reset(self):
        """ Reset all form fields """
        for variable in self.variables.values():
            if isinstance(variable, tk.BooleanVar):
                variable.set(False)
            else:
                variable.set('')

    def get(self):
        """ Get all form data """
        data = {}

        fault = self.variables[EnvironmentInfo.EQUIPMENT_FAULT].get()

        for name, value in self.variables.items():
            if fault and name in [
                    EnvironmentInfo.HUMIDITY,
                    EnvironmentInfo.LIGHT,
                    EnvironmentInfo.TEMPERATURE
            ]:
                data[name] = ''
            else:
                try:
                    data[name] = value.get()
                except tk.TclError as error:
                    message = f"Error in field: {name}. Data was not saved!"
                    raise ValueError(message) from error

        return data

class Application(tk.Tk):
    """ Application Root Window """
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

    def on_save(self):
        """ Save the form values """
        stamp = datetime.today().strftime('%Y-%m-%d')
        filename = Path(f"data_record_{stamp}.csv")
        is_new = not filename.exists()

        try:
            data = self.record_form.get()
        except ValueError as error:
            self.status.configure(foreground='red')
            self.status_value.set(str(error))
            return

        with open(
            filename, 'a', newline='', encoding=sys.getdefaultencoding()
        ) as out:
            writer = csv.DictWriter(out, fieldnames=data.keys())
            if is_new:
                writer.writeheader()
            writer.writerow(data)

        self.records_saved += 1
        self.status.configure(foreground='green')
        self.status_value.set(
            f"{self.records_saved} record(s) saved this session"
        )

        self.record_form.on_reset()

if __name__ == '__main__':
    Application().mainloop()
