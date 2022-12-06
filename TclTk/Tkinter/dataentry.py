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

EQUIPMENT_FAULT = 'Equipment Fault'
HUMIDITY = "Humidity (g/m\u00B3)"
LIGHT = 'Light (klx)'
# pylint: disable=consider-using-f-string
TEMPERATURE = "Temperature ({}C)".format('\u00B0')
MIN_HEIGHT = 'Min Height (cm)'
MAX_HEIGHT = 'Max Height (cm)'
MEDIAN_HEIGHT = 'Median Height (cm)'

SIDES = tk.W + tk.E

# All of the form widget control variables.
variables = {}

# Number of records saved for this iteration of the application.
# pylint: disable=invalid-name
records_saved = 0

def data_section(parent, title):
    """ Create a labeled box """
    frame = ttk.LabelFrame(parent, text=title)
    frame.grid(sticky=SIDES)
    for icol in range(3):
        frame.columnconfigure(icol, weight=1)
    return frame

def make_rec_info(parent):
    """ Create record information form """
    rec_info = data_section(parent, 'Record Information')

    variables['Date'] = tk.StringVar()
    LabelInput(rec_info, 'Date', variables['Date']).grid(row=0, column=0)

    variables['Time'] = tk.StringVar()
    LabelInput(
        rec_info,
        'Time',
        variables['Time'],
        input_class=ttk.Combobox,
        input_args={'values': ['8:00', '12:00', '16:00', '20:00']}
    ).grid(row=0, column=1)

    variables['Technician'] = tk.StringVar()
    LabelInput(
        rec_info, 'Technician', variables['Technician']
    ).grid(row=0, column=2)

    variables['Lab'] = tk.StringVar()
    LabelInput(
        rec_info,
        'Lab',
        variables['Lab'],
        input_class=ttk.Radiobutton,
        input_args={'values': ['A', 'B', 'C']}
    ).grid(row=1, column=0)

    variables['Plot'] = tk.IntVar()
    LabelInput(
        rec_info,
        'Plot',
        variables['Plot'],
        input_class=ttk.Combobox,
        input_args={'values': list(range(1, 21))}
    ).grid(row=1, column=1)

    variables['Seed Sample'] = tk.StringVar()
    LabelInput(
        rec_info, 'Seed Sample', variables['Seed Sample']
    ).grid(row=1, column=2)

def make_env_info(parent):
    """ Create environment data form """
    env_info = data_section(parent, 'Environment Data')

    variables[HUMIDITY] = tk.DoubleVar()
    LabelInput(
        env_info,
        HUMIDITY,
        variables[HUMIDITY],
        input_class=ttk.Spinbox,
        input_args={'from_': 0.5, 'to_': 52.0, 'increment': 0.01}
    ).grid(row=0, column=0)

    variables[LIGHT] = tk.DoubleVar()
    LabelInput(
        env_info,
        LIGHT,
        variables[LIGHT],
        input_class=ttk.Spinbox,
        input_args={'from_': 0.0, 'to_': 100.0, 'increment': 0.01}
    ).grid(row=0, column=1)

    variables[TEMPERATURE] = tk.DoubleVar()
    LabelInput(
        env_info,
        TEMPERATURE,
        variables[TEMPERATURE],
        input_class=ttk.Spinbox,
        input_args={'from_': 4.0, 'to_': 40.0, 'increment': 0.01}
    ).grid(row=0, column=2)

    variables[EQUIPMENT_FAULT] = tk.BooleanVar()
    LabelInput(
        env_info,
        EQUIPMENT_FAULT,
        variables[EQUIPMENT_FAULT],
        input_class=ttk.Checkbutton
    ).grid(row=1, column=0)
        
def make_plant_info(parent):
    """ Create plant data form """
    plant_info = data_section(parent, 'Plant Data')

    variables['Plants'] = tk.IntVar()
    LabelInput(
        plant_info,
        'Plants',
        variables['Plants'],
        input_class=ttk.Spinbox,
        input_args={'from_': 0, 'to_': 20, 'increment': 1}
    ).grid(row=0, column=0)

    variables['Blossoms'] = tk.IntVar()
    LabelInput(
        plant_info,
        'Blossoms',
        variables['Blossoms'],
        input_class=ttk.Spinbox,
        input_args={'from_': 0, 'to_': 1000, 'increment': 1}
    ).grid(row=0, column=1)

    variables['Fruit'] = tk.IntVar()
    LabelInput(
        plant_info,
        'Fruit',
        variables['Fruit'],
        input_class=ttk.Spinbox,
        input_args={'from_': 0, 'to_': 1000, 'increment': 1}
    ).grid(row=0, column=2)

    variables[MIN_HEIGHT] = tk.DoubleVar()
    LabelInput(
        plant_info,
        MIN_HEIGHT,
        variables[MIN_HEIGHT],
        input_class=ttk.Spinbox,
        input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
    ).grid(row=1, column=0)

    variables[MAX_HEIGHT] = tk.DoubleVar()
    LabelInput(
        plant_info,
        MAX_HEIGHT,
        variables[MAX_HEIGHT],
        input_class=ttk.Spinbox,
        input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
    ).grid(row=1, column=1)

    variables[MEDIAN_HEIGHT] = tk.DoubleVar()
    LabelInput(
        plant_info,
        MEDIAN_HEIGHT,
        variables[MEDIAN_HEIGHT],
        input_class=ttk.Spinbox,
        input_args={'from_': 0.0, 'to_': 1000.0, 'increment': 0.01}
    ).grid(row=1, column=2)

def on_reset():
    """ Reset all form fields """
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')

def on_save():
    """ Save form values """
    # pylint: disable=global-statement
    global records_saved

    stamp = datetime.today().strftime('%Y-%m-%d')
    filename = Path(f"data_record_{stamp}.csv")
    is_new = not filename.exists()

    data = {}
    fault = variables[EQUIPMENT_FAULT].get()
    for name, value in variables.items():
        if fault and name in (HUMIDITY, LIGHT, TEMPERATURE):
            data[name] = ''
        else:
            try:
                data[name] = value.get()
            except tk.TclError:
                status.configure(foreground='red')
                status_value.set(
                    f"Error in field: {name}. Data was not saved!"
                )
                return

    with open(
        filename, 'a', newline='', encoding=sys.getdefaultencoding()
    ) as out:
        writer = csv.DictWriter(out, fieldnames=data.keys())
        if is_new:
            writer.writeheader()
        writer.writerow(data)

    records_saved += 1
    status.configure(foreground='green')
    status_value.set(f"{records_saved} record(s) saved this session")

    on_reset()

def make_buttons(parent):
    """ Make button frame """
    frame = ttk.Frame(parent)
    frame.grid(sticky=SIDES)
    ttk.Button(frame, text='Quit', command=root.quit).pack(side=tk.RIGHT)
    ttk.Button(frame, text='Save', command=on_save).pack(side=tk.RIGHT)
    ttk.Button(frame, text='Reset', command=on_reset).pack(side=tk.RIGHT)

root = tk.Tk()
root.title('Data Entry')
root.columnconfigure(0, weight=1)

ttk.Label(root, text='Lab Data Entry', font=('TkDefaultFont', 16)).grid()

outer = ttk.Frame(root)
outer.grid(padx=10, sticky=SIDES)
outer.columnconfigure(0, weight=1)

make_rec_info(outer)
make_env_info(outer)
make_plant_info(outer)


variables['Notes'] = tk.StringVar()
LabelInput(
    outer,
    'Notes',
    variables['Notes'],
    input_class=TextWithVar,
    input_args={'width': 75, 'height': 10}
).grid()

make_buttons(outer)

status_value = tk.StringVar()
status = ttk.Label(root, textvariable=status_value)
status.grid(sticky=SIDES, padx=10)

on_reset()
tk.mainloop()
