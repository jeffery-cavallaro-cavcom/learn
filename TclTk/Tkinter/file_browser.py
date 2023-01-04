""" File Browser using Treeviw """

import tkinter as tk
from tkinter import ttk
from pathlib import Path

class Application(tk.Tk):
    """ File Browser Application """
    def __init__(self):
        """ Create a file browser """
        super().__init__()
        self.title('File Browser')
        paths = Path('.').glob('**/*')
        self.browser = self.make_browser()
        self.browser.pack()

        for path in paths:
            status = path.stat()
            parent = str(path.parent)
            if parent == '.':
                parent = ''
            self.browser.insert(
                parent,
                'end',
                iid=str(path),
                text=str(path.name),
                values=[status.st_size, status.st_mtime]
            )

    def make_browser(self):
        """ Construct the browser """
        browser = ttk.Treeview(
            self, columns=['size', 'modified'], selectmode='none'
        )

        browser.heading('#0', text='Name')
        browser.heading('size', text='Size', anchor=tk.CENTER)
        browser.heading('modified', text='Modified', anchor=tk.CENTER)

        browser.column('#0', stretch=True)
        browser.column('size', width=200)

        for cid in ['#0', 'size', 'modified']:
            browser.heading(
                cid, command=lambda column=cid: self.sort_column(column)
            )

        return browser

    def sort_column(self, column, parent='', reverse=False):
        """ Sort rows by column """
        if parent == '':
            self.browser.heading(
                column,
                command=lambda col=column: self.sort_column(
                    col, reverse=not reverse
                )
            )

        sort_index = [
            (
                self.browser.set(iid, column) if column != '#0' else iid,
                iid
            )
            for iid in self.browser.get_children(parent)
        ]
        sort_index.sort(key=lambda two: two[0], reverse=reverse)
        for index, (_, iid) in enumerate(sort_index):
            self.browser.move(iid, parent, index)
            self.sort_column(column, parent=iid, reverse=reverse)

if __name__ == '__main__':
    Application().mainloop()
