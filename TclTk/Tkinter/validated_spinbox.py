"""
A spin box with the following validations:
    1. Valid characters limited to digits, '-', and '.'.
    2. Minus sign only allowed in first position and only when the minimum
       allowed value is negative.
    3. Decimal point allowed only once and only when precision is less than 1.
    4. Final value in range and correct precision.
"""

from decimal import Decimal, InvalidOperation
import tkinter as tk
from tkinter import ttk

from validator import Validator

# pylint: disable=too-many-ancestors

class ValidatedSpinbox(Validator, ttk.Spinbox):
    """ A Validated Spinbox """
    def __init__(
        self, *args, from_value='-Infinity', to_value='Infinity', **kwargs
    ):
        super().__init__(*args, from_=from_value, to=to_value, **kwargs)
        increment = Decimal(str(kwargs.get('increment', '1.0')))
        self.precision = increment.normalize().as_tuple().exponent

    # pylint: disable=arguments-differ
    # pylint: disable=too-many-arguments

    def validate_key(self, char, index, current, proposed, action, **kwargs):
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

if __name__ == '__main__':
    root = tk.Tk()
    entry = ValidatedSpinbox(root, from_value=1.0, to_value=10.0, increment=0.1)
    entry.pack()
    ttk.Label(textvariable=entry.error_var).pack()
    ttk.Entry(root).pack()
    root.mainloop()
