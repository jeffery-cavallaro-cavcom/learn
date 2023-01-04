"""
Data Entry Demonstration
"""

from pathlib import Path
import sys

PARENT = Path(__file__).parent
sys.path = [
    str(PARENT / 'data_entry'),
    str(PARENT / 'data_entry' / 'models'),
    str(PARENT / 'data_entry' / 'widgets'),
    *sys.path
]

from data_entry.application import Application

Application().mainloop()
