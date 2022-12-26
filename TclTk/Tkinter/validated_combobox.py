"""
A combo box with the following validations:
    1.  A delete action clears the box.
"""

from tkinter import ttk

from validator import Validator

# pylint: disable=too-many-ancestors
# pylint: disable=arguments-differ

class ValidateCombobox(Validator, ttk.Combobox):
    """ A Validated Combobox """
    def validate_key(self, proposed, action, **kwargs):
        valid = True

        if action == '0':
            self.set('')
            return True

        return valid
