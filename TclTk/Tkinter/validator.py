"""
Mixin for data entry validation
"""

import tkinter as tk

# pylint: disable=no-member

class Validator:
    """ Validating Mixin """
    ARGS = ('%P', '%s', '%S', '%V', '%i', '%d')

    def __init__(self, *args, error_var=None, **kwargs):
        """ Register validattion methods """
        super().__init__(*args, **kwargs)
        self.error_var = error_var or tk.StringVar()
        self.configure(
            validate='all',
            validatecommand=(self.register(self.validate), *self.ARGS),
            invalidcommand=(self.register(self.invalid), *self.ARGS)
        )

    def set_error(self, state=False):
        """ Set error state """
        self.configure(foreground='red' if state else 'black')

    # pylint: disable=too-many-arguments
    def validate(self, proposed, current, char, event, index, action):
        """ Validate event """
        self.error_var.set('')
        self.set_error()
        valid = True

        state = str(self.configure('state')[-1])
        if state == tk.DISABLED:
            return valid

        if event == 'focusout':
            valid = self.validate_focusout(event=event)
        elif event == 'key':
            valid = self.validate_key(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )

        return valid

    # pylint: disable=unused-argument
    # pylint: disable=no-self-use

    def validate_focusout(self, **kwargs):
        """ Validate focus-out event """
        return True

    def validate_key(self, **kwargs):
        """ Validate key events"""
        return True

    def invalid(self, proposed, current, char, event, index, action):
        """ Handle invalid values """
        if event == 'focusout':
            self.invalid_focusout(event=event)
        elif event == 'key':
            self.invalid_key(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )

    def invalid_focusout(self, **kwargs):
        """ Handle invalid value"""
        self.set_error(state=True)

    def invalid_key(self, **kwargs):
        """ Handle invalid keystroke """

    def trigger_validate_focusout(self):
        """ Simulate focusout validation """
        valid = self.validate('', '', '', 'focusout', '', '')
        if not valid:
            self.invalid_focusout(event='focusout')
        return valid
