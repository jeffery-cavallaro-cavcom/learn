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

EQUIPMENT_FAULT = 'Equipment Fault'
HUMIDITY = "Humidity (g/m\u00B3)"
LIGHT = 'Light (klx)'
TEMPERATURE = "Temperature ({}C)".format('\u00B0')
NOTES = 'Notes'

sides = tk.W + tk.E

# All of the form widget control variables.
variables = dict()

# Number of records saved for this iteration of the application.
records_saved = 0

def data_section(outer, title):
    frame = ttk.LabelFrame(outer, text=title)
    frame.grid(sticky=sides)
    for icol in range(3):
        frame.columnconfigure(icol, weight=1)
    return frame

def form_entry(outer, row, column, name, type=tk.StringVar):
    variables[name] = type()
    ttk.Label(outer, text=name).grid(row=row, column=column)
    ttk.Entry(outer, textvariable=variables[name]).grid(
        row=(row + 1), column=column, sticky=sides
    )

def form_combo(outer, row, column, values, name, type=tk.StringVar):
    variables[name] = type()
    ttk.Label(outer, text=name).grid(row=row, column=column)
    ttk.Combobox(outer, textvariable=variables[name], values=values).grid(
        row=(row + 1), column=column, sticky=sides
    )

def form_spinner(outer, row, column, from_, to, inc, name, type=tk.DoubleVar):
    variables[name] = type()
    ttk.Label(outer, text=name).grid(row=row, column=column)
    ttk.Spinbox(
        outer,
        textvariable=variables[name],
        from_=from_,
        to=to,
        increment=inc
    ).grid(row=(row + 1), column=column, sticky=sides)

def make_rec_info(outer):
    rec_info = data_section(outer, 'Record Information')

    form_entry(rec_info, 0, 0, 'Date')
    
    times = ['8:00', '12:00', '16:00', '20:00']
    form_combo(rec_info, 0, 1, times, 'Time')

    form_entry(rec_info, 0, 2, 'Technician')

    variables['Lab'] = tk.StringVar()
    ttk.Label(rec_info, text='Lab').grid(row=2, column=0)
    lab_frame = ttk.Frame(rec_info)
    for lab in ('A', 'B', 'C'):
        ttk.Radiobutton(
            lab_frame, value=lab, text=lab, variable=variables['Lab']
        ).pack(side=tk.LEFT, expand=True)
    lab_frame.grid(row=3, column=0, sticky=sides)

    plots = list(range(1, 21))
    form_combo(rec_info, 2, 1, plots, 'Plot')

    form_entry(rec_info, 2, 2, 'Seed Sample')

def make_env_info(outer):
    env_info = data_section(outer, 'Environment Data')

    form_spinner(env_info, 0, 0, 0.5, 52.0, 0.01, HUMIDITY)
    form_spinner(env_info, 0, 1, 0.0, 100.0, 0.01, LIGHT)
    form_spinner(env_info, 0, 2, 4.0, 40.0, 0.01, TEMPERATURE)

    name = EQUIPMENT_FAULT
    variables[name] = tk.BooleanVar()
    ttk.Checkbutton(outer, variable=variables[name], text=name).grid(
        row=2, column=0, sticky=tk.W, pady=5
    )

def make_plant_info(outer):
    plant_info = data_section(outer, 'Plant Data')

    form_spinner(plant_info, 0, 0, 0, 20, 1, 'Plants', type=tk.IntVar)
    form_spinner(plant_info, 0, 1, 0, 1000, 1, 'Blossoms', type=tk.IntVar)
    form_spinner(plant_info, 0, 2, 0, 1000, 1, 'Fruit', type=tk.IntVar)

    form_spinner(plant_info, 2, 0, 0.0, 1000.0, 0.01, 'Min Height (cm)')
    form_spinner(plant_info, 2, 1, 0.0, 1000.0, 0.01, 'Max Height (cm)')
    form_spinner(plant_info, 2, 2, 0.0, 1000.0, 0.01, 'Median Height (cm)')

def on_reset():
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')
    notes_input.delete('1.0', tk.END)

def on_save():
    global records_saved

    stamp = datetime.today().strftime('%Y-%m-%d')
    filename = Path(f"data_record_{stamp}.csv")
    is_new = not filename.exists()

    data = dict()
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
    data[NOTES] = notes_input.get('1.0', tk.END)

    with open(filename, 'a', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=data.keys())
        if is_new:
            writer.writeheader()
        writer.writerow(data)

    records_saved += 1
    status.configure(foreground='green')
    status_value.set(f"{records_saved} record(s) saved this session")

    on_reset()

def make_buttons(outer):
    frame = ttk.Frame(outer)
    frame.grid(sticky=sides)
    ttk.Button(frame, text='Quit', command=root.quit).pack(side=tk.RIGHT)
    ttk.Button(frame, text='Save', command=on_save).pack(side=tk.RIGHT)
    ttk.Button(frame, text='Reset', command=on_reset).pack(side=tk.RIGHT)

root = tk.Tk()
root.title('Data Entry')
root.columnconfigure(0, weight=1)

ttk.Label(root, text='Lab Data Entry', font=('TkDefaultFont', 16)).grid()

outer = ttk.Frame(root)
outer.grid(padx=10, sticky=sides)
outer.columnconfigure(0, weight=1)

make_rec_info(outer)
make_env_info(outer)
make_plant_info(outer)

ttk.Label(outer, text='Notes').grid()
notes_input = tk.Text(outer, width=75, height=10)
notes_input.grid(sticky=sides)

make_buttons(outer)

status_value = tk.StringVar()
status = ttk.Label(root, textvariable=status_value)
status.grid(sticky=sides, padx=10)

on_reset()
tk.mainloop()
