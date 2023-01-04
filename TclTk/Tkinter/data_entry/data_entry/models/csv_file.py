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
        # pylint: disable=consider-using-f-string
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
    # pylint: disable=too-few-public-methods
    def __init__(self, filename=None):
        """ Initialize output CSV file """
        if not filename:
            stamp = datetime.today().strftime(DATE_FORMAT)
            filename = Path(f"data_record_{stamp}.csv")
        self.filename = Path(filename)

    def open_file(self, clear=False):
        """ Open the output file """
        mode = 'w' if clear else 'a'
        is_new = clear or not self.filename.exists()

        csvfile = open(
            self.filename, mode, newline='', encoding=sys.getdefaultencoding()
        )
        if is_new:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDS.keys())
            writer.writeheader()

        return csvfile

    def get_all_records(self):
        """ Read all file records """
        if not self.filename.exists():
            return []

        with open(self.filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            missing = set(FIELDS.keys()) - set(csvreader.fieldnames)
            if len(missing) > 0:
                missing = ', '.join(missing)
                raise Exception(f"File is missing fields: {missing}")
            records = list(csvreader)

        bool_fields = [
            name for name, spec in FIELDS.items() if spec['type'] == FT.BOOLEAN
        ]
        for record in records:
            for name in bool_fields:
                record[name] = record[name].lower == 'true'

        return records

    def get_record(self, row):
        """ Get record by row number """
        return self.get_all_records()[row]

    def save_record(self, record, row=None):
        """ Save a new data record """
        if row is None:
            with self.open_file() as out:
                writer = csv.DictWriter(out, fieldnames=FIELDS.keys())
                writer.writerow(record)
        else:
            records = self.get_all_records()
            records[row] = record
            with self.open_file(clear=True):
                writer = csv.DictWriter(out, fieldnames=FIELDS.keys())
                writer.writerows(records)
