""" Data Entry Settings """

import json
from pathlib import Path
import sys

class SettingsModel:
    """ Data Model for Saved Settings """
    def __init__(self):
        """ Setup settings file """
        self.fields = {
            'autofill date': {'type': 'bool', 'value': True},
            'autofill sheet data': {'type': 'bool', 'value': True},
        }
        self.filename = Path.home() / 'data_entry_settings.json'
        self.load()

    def load(self):
        """ Load settings """
        # pylint: disable=bare-except
        try:
            with open(
                self.filename, 'r', encoding=sys.getdefaultencoding()
            ) as settings_file:
                raw_values = json.load(settings_file)
        except:
            return

        for name, values in self.fields.items():
            if name in raw_values and 'value' in raw_values[name]:
                values['value'] = raw_values[name]['value']

    def save(self):
        """ Save settings """
        # pylint: disable=bare-except
        try:
            with open(
                self.filename, 'w', encoding=sys.getdefaultencoding()
            ) as settings_file:
                json.dump(self.fields, settings_file)
        except:
            pass

    def set(self, name, value):
        """ Alter setting value """
        if (
            name in self.fields and
            type(value).__name__ == self.fields[name]['type']
        ):
            self.fields[name]['value'] = value
