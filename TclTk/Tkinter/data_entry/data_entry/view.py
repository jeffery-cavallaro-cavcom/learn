""" Data Entry View """

from datetime import datetime
import tkinter as tk
from tkinter import ttk

from model import FIELDS
from constants import FieldType as FT
from constants import DATE_FORMAT

from widgets.iso_date_entry import ISODateEntry
from widgets.labeled_frame import LabeledFrame
from widgets.label_input import LabelInput
from widgets.required_entry import RequiredEntry
from widgets.text_with_var import TextWithVar
from widgets.validated_combobox import ValidatedCombobox
from widgets.validated_radio_group import ValidatedRadioGroup
from widgets.validated_spinbox import ValidatedSpinbox

FIELD_TYPES = {
    FT.STRING: (RequiredEntry, tk.StringVar),
    FT.STRING_LIST: (ValidatedCombobox, tk.StringVar),
    FT.SHORT_STRING_LIST: (ValidatedRadioGroup, tk.StringVar),
    FT.ISO_DATE_STRING: (ISODateEntry, tk.StringVar),
    FT.LONG_STRING: (TextWithVar, tk.StringVar),
    FT.DECIMAL: (ValidatedSpinbox, tk.DoubleVar),
    FT.INTEGER: (ValidatedSpinbox, tk.IntVar),
    FT.INTEGER_LIST: (ValidatedCombobox, tk.IntVar),
    FT.BOOLEAN: (ttk.Checkbutton, tk.BooleanVar)
}

class FormField(LabelInput):
    """ Match Form Field to Labeled Widget """
    def __init__(self, parent, name, model, variables, **kwargs):
        """ Construct a labeled input widget """
        kwargs = kwargs.copy()

        field_spec = model[name]
        input_class = FIELD_TYPES[field_spec.type][0]
        if 'input_class' not in kwargs:
            kwargs['input_class'] = input_class

        variable = variables[name]
        name = field_spec.label or name

        input_args = kwargs.get('input_args')
        if not input_args:
            input_args = {}
            kwargs['input_args'] = input_args

        if 'from_value' not in input_args and field_spec.min_value is not None:
            input_args['from_value'] = field_spec.min_value
        if 'to_value' not in input_args and field_spec.max_value is not None:
            input_args['to_value'] = field_spec.max_value
        if 'increment' not in input_args and field_spec.inc_value is not None:
            input_args['increment'] = field_spec.inc_value
        if 'values' not in input_args and field_spec.values:
            input_args['values'] = [str(value) for value in field_spec.values]

        super().__init__(parent, name, variable, **kwargs)

class RecordInfo(LabeledFrame):
    """ Record Information Box """
    def __init__(self, parent, variables):
        """ Create the record information box """
        super().__init__(parent, 'Record Information')

        FormField(self, 'Date', FIELDS, variables).grid(row=0, column=0)
        FormField(self, 'Time', FIELDS, variables).grid(row=0, column=1)
        FormField(self, 'Technician', FIELDS, variables).grid(row=0, column=2)

        FormField(self, 'Lab', FIELDS, variables).grid(row=1, column=0)
        FormField(self, 'Plot', FIELDS, variables).grid(row=1, column=1)
        FormField(self, 'Seed Sample', FIELDS, variables).grid(row=1, column=2)

class EnvironmentInfo(LabeledFrame):
    """ Environment Information Box """
    def __init__(self, parent, variables):
        """ Create the environment information box """
        super().__init__(parent, 'Environment Data')

        FormField(
            self,
            'Humidity',
            FIELDS,
            variables,
            disable_var=variables['Equipment Fault']
        ).grid(row=0, column=0)

        FormField(
            self,
            'Light',
            FIELDS,
            variables,
            disable_var=variables['Equipment Fault']
        ).grid(row=0, column=1)

        FormField(
            self,
            'Temperature',
            FIELDS,
            variables,
            disable_var=variables['Equipment Fault']
        ).grid(row=0, column=2)

        FormField(
            self, 'Equipment Fault', FIELDS, variables
        ).grid(row=1, column=0)

class PlantInfo(LabeledFrame):
    """ Plant Information Box """
    def __init__(self, parent, variables):
        """ Create the plant information box """
        super().__init__(parent, 'Plant Data')

        FormField(self, 'Plants', FIELDS, variables).grid(row=0, column=0)
        FormField(self, 'Blossoms', FIELDS, variables).grid(row=0, column=1)
        FormField(self, 'Fruit', FIELDS, variables).grid(row=0, column=2)

        min_height_var = tk.DoubleVar(value='-infinity')
        max_height_var = tk.DoubleVar(value='infinity')

        FormField(
            self,
            'Min Height',
            FIELDS,
            variables,
            input_args={
                'max_var': max_height_var,
                'update_var': min_height_var
            }
        ).grid(row=1, column=0)

        FormField(
            self,
            'Max Height',
            FIELDS,
            variables,
            input_args={
                'min_var': min_height_var,
                'update_var': max_height_var
            }
        ).grid(row=1, column=1)

        FormField(
            self,
            'Med Height',
            FIELDS,
            variables,
            input_args={
                'min_var': min_height_var,
                'max_var': max_height_var
            }
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
            name: FIELD_TYPES[spec.type][1]()
            for name, spec in FIELDS.items()
        }

        RecordInfo(self, self.variables)
        EnvironmentInfo(self, self.variables)
        PlantInfo(self, self.variables)

        FormField(
            self,
            'Notes',
            FIELDS,
            self.variables,
            input_args={'width': 75, 'height': 10}
        ).grid()

        ButtonBar(self)

    def on_reset(self):
        """ Reset all form fields """
        lab = self.variables['Lab'].get()
        time = self.variables['Time'].get()
        technician = self.variables['Technician'].get()

        try:
            plot = self.variables['Plot'].get()
        except tk.TclError:
            plot = ''

        plot_values = self.variables['Plot'].label_widget.input.cget('values')

        for variable in self.variables.values():
            if isinstance(variable, tk.BooleanVar):
                variable.set(False)
            else:
                variable.set('')

        self.variables['Date'].set(datetime.today().strftime(DATE_FORMAT))
        self.variables['Time'].label_widget.input.focus()

        if plot not in ('', 0, plot_values[-1]):
            self.variables['Lab'].set(lab)
            self.variables['Time'].set(time)
            self.variables['Technician'].set(technician)

            next_plot_index = plot_values.index(str(plot)) + 1
            self.variables['Plot'].set(plot_values[next_plot_index])

            self.variables['Seed Sample'].label_widget.input.focus()

    def get(self):
        """ Get all form data """
        data = {}

        fault = self.variables['Equipment Fault'].get()

        for name, value in self.variables.items():
            if fault and name in ['Humidity', 'Light', 'Temperature']:
                data[name] = ''
            else:
                try:
                    data[name] = value.get()
                except tk.TclError as error:
                    message = f"Error in field: {name}. Data was not saved!"
                    raise ValueError(message) from error

        return data

    def get_errors(self):
        errors = {}
        for name, variable in self.variables.items():
            input = variable.label_widget.input
            error_var = variable.label_widget.error_var
            if hasattr(input, 'trigger_validate_focusout'):
                input.trigger_validate_focusout()
            message = error_var.get()
            if message:
                errors[name] = message
        return errors
