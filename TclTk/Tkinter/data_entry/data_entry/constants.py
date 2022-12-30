"""
Model Contants
"""

from enum import Enum, auto

from widgets.iso_date_entry import ISODateEntry

class FieldType(Enum):
    STRING = auto()
    STRING_LIST = auto()
    SHORT_STRING_LIST = auto()
    ISO_DATE_STRING = auto()
    LONG_STRING = auto()
    DECIMAL = auto()
    INTEGER = auto()
    INTEGER_LIST = auto()
    BOOLEAN = auto()

DATE_FORMAT = ISODateEntry.FORMAT
