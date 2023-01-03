"""
A spin box with the following validations:
    1. Valid characters limited to digits, '-', and '.'.
    2. Minus sign only allowed in first position and only when the minimum
       allowed value is negative.
    3. Decimal point allowed only once and only when precision is less than 1.
    4. Final value in range and correct precision.
    5. Updatable minimum and maximum values.
"""

from decimal import Decimal, InvalidOperation
import tkinter as tk
from tkinter import ttk

from validator import Validator

# pylint: disable=too-many-ancestors

class ValidatedSpinbox(Validator, ttk.Spinbox):
    """ A Validated Spinbox """
    def __init__(
        self,
        *args,
        min_var=None,
        max_var=None,
        update_var=None,
        from_value='-Infinity',
        to_value='Infinity',
        **kwargs
    ):
        super().__init__(*args, from_=from_value, to=to_value, **kwargs)
        increment = Decimal(str(kwargs.get('increment', '1.0')))
        self.precision = increment.normalize().as_tuple().exponent

        self.variable = kwargs.get('textvariable')
        if not self.variable:
            self.variable = tk.DoubleVar()
            self.configure(textvariable=self.variable)

        if min_var:
            self.min_var = min_var
            self.min_var.trace_add('write', self.set_minimum)

        if max_var:
            self.max_var = max_var
            self.max_var.trace_add('write', self.set_maximum)

        self.update_var = update_var
        self.bind('<FocusOut>', self.on_focusout)

    # pylint: disable=arguments-differ
    # pylint: disable=too-many-arguments

    def validate_key(self, char, index, current, proposed, action, **kwargs):
        """ Validate keystrokes """
        if action == '0':
            return True

        min_value = self.cget('from')
        max_value = self.cget('to')
        no_negative = (min_value >= 0)
        no_decimal = (self.precision >= 0)

        if any(
            [
                (char not in '-1234567890.'),
                ((char == '-') and (no_negative or (index != 0))),
                ((char == '.') and (no_decimal or ('.' in current)))
            ]
        ):
            return False

        if proposed in '-.':
            return True

        proposed = Decimal(proposed)
        precision = proposed.as_tuple().exponent

        if any(
            [
                (proposed > max_value),
                (precision < self.precision)
            ]
        ):
            return False

        return True

    def validate_focusout(self, **kwargs):
        """ Validate focusout event """
        value = self.get()
        if not value:
            self.error_var.set('A numeric value is required')
            return False

        min_value = self.cget('from')
        max_value = self.cget('to')

        try:
            dvalue = Decimal(value)
        except InvalidOperation:
            self.error_var.set(f"Invalid number string: {value}")
            return False

        if dvalue < min_value:
            self.error_var.set(f"Value is too low (min: {min_value})")
            return False

        if dvalue > max_value:
            self.error_var.set(f"Value is too high (max: {max_value})")
            return False

        return True

    def on_focusout(self, *_):
        """ Focusout event handler """
        value = self.get()
        if self.update_var and not self.error_var.get():
            self.update_var.set(value)

    def set_minimum(self, *_):
        """ Set the minimum allowed value """
        current = self.get()

        try:
            new_min = self.min_var.get()
            self.config(from_=new_min)
        except (tk.TclError, ValueError):
            pass

        if current:
            self.variable.set(current)
        else:
            self.delete(0, tk.END)

        self.trigger_validate_focusout()

    def set_maximum(self, *_):
        """ Set the maximum allowed value """
        current = self.get()

        try:
            new_max = self.max_var.get()
            self.config(to=new_max)
        except (tk.TclError, ValueError):
            pass

        if current:
            self.variable.set(current)
        else:
            self.delete(0, tk.END)

        self.trigger_validate_focusout()

if __name__ == '__main__':
    root = tk.Tk()
    entry = ValidatedSpinbox(root, from_value=1.0, to_value=10.0, increment=0.1)
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
