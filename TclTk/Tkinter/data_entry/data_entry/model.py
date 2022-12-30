""" Data Model """

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys

from constants import FieldType as FT
from constants import DATE_FORMAT

@dataclass
class Field:
    """ A single field definition """
    type : FT
    label: str = None
    required : bool = True
    values : list = None
    min_value : float = None
    max_value : float = None
    inc_value : float = None

FIELDS = {
    'Date': Field(
        type=FT.ISO_DATE_STRING
    ),
    'Time': Field(
        type=FT.STRING_LIST,
        values=['8:00', '12:00', '16:00', '20:00']
    ),
    'Technician': Field(
        type=FT.STRING
    ),
    'Lab': Field(
        type=FT.SHORT_STRING_LIST,
        values=['A', 'B', 'C']
    ),
    'Plot': Field(
        type=FT.INTEGER_LIST,
        values=range(1, 20)
    ),
    'Seed Sample': Field(
        type=FT.STRING
    ),
    'Humidity': Field(
        type=FT.DECIMAL,
        label="Humidity (g/m\u00B3)",
        min_value=0.5,
        max_value=52.0,
        inc_value=0.01
    ),
    'Light': Field(
        type=FT.DECIMAL,
        label='Light (klx)',
        min_value=0.0,
        max_value=100.0,
        inc_value=0.01
    ),
    'Temperature': Field(
        type=FT.DECIMAL,
        label="Temperature ({}C)".format('\u00B0'),
        min_value=4.0,
        max_value=40.0,
        inc_value=0.01
    ),
    'Equipment Fault': Field(
        type=FT.BOOLEAN,
        required=False
    ),
    'Plants': Field(
        type=FT.INTEGER,
        min_value=0,
        max_value=20
    ),
    'Blossoms': Field(
        type=FT.INTEGER,
        min_value=0,
        max_value=1000
    ),
    'Fruit': Field(
        type=FT.INTEGER,
        min_value=0,
        max_value=1000
    ),
    'Min Height': Field(
        type=FT.DECIMAL,
        label='Min height (cm)',
        min_value=0.0,
        max_value=1000.0,
        inc_value=0.01
    ),
    'Max Height': Field(
        type=FT.DECIMAL,
        label='Max height (cm)',
        min_value=0.0,
        max_value=1000.0,
        inc_value=0.01
    ),
    'Med Height': Field(
        type=FT.DECIMAL,
        label='Med height (cm)',
        min_value=0.0,
        max_value=1000.0,
        inc_value=0.01
    ),
    'Notes': Field(
        type=FT.LONG_STRING,
        required=False
    )
}

class CSVModel:
    """ CSV Output File Model """
    def __init__(self, filename=None):
        """ Initialize output CSV file """
        if not filename:
            stamp = datetime.today().strftime(DATE_FORMAT)
            filename = Path(f"data_record_{stamp}.csv")
        self.filename = Path(filename)
        is_new = not self.filename.exists()

        with open(
            self.filename, 'a', newline='', encoding=sys.getdefaultencoding()
        ) as out:
            writer = csv.DictWriter(out, fieldnames=FIELDS.keys())
            if is_new:
                writer.writeheader()

    def save_record(self, record):
        """ Save a new data record """
        with open(
            self.filename, 'a', newline='', encoding=sys.getdefaultencoding()
        ) as out:
            writer = csv.DictWriter(out, fieldnames=FIELDS.keys())
            writer.writerow(record)
