""" Menu Demonstration """

import tkinter as tk

class Application(tk.Tk):
    """ Main Application """
    def __init__(self):
        super().__init__()
        self.geometry('200x150')
        self.title('Menu Demonstration')

        self.font_bold = tk.BooleanVar(value=False)
        self.font_bold.trace_add('write', self.set_font)
        self.font_size = tk.IntVar(value=10)
        self.font_size.trace_add('write', self.set_font)

        main_text = tk.StringVar(value='Hello')
        self.label = tk.Label(self, textvariable=main_text)
        self.label.pack(side='bottom')

        main_menu = tk.Menu(self)
        main_menu.add('command', label='Quit', command=self.quit)

        text_menu = tk.Menu(main_menu, tearoff=False)
        text_menu.add_command(
            label='Set to "Hello"', command=lambda: main_text.set('Hello')
        )
        text_menu.add_command(
            label='Set to "World"', command=lambda: main_text.set('World')
        )
        main_menu.add_cascade(label='Text', menu=text_menu)

        appearance_menu = tk.Menu(main_menu, tearoff=False)
        appearance_menu.add_checkbutton(label='Bold', variable=self.font_bold)

        size_menu = tk.Menu(appearance_menu, tearoff=False)
        for size in range(8, 24, 2):
            size_menu.add_radiobutton(
                label=f"{size} px", value=size, variable=self.font_size
            )
        appearance_menu.add_cascade(label='Font Size', menu=size_menu)

        main_menu.add_cascade(label='Appearance', menu=appearance_menu)

        self.configure(menu=main_menu)

    def set_font(self, *_):
        size = self.font_size.get()
        weight = 'bold' if self.font_bold.get() else ''
        self.label.configure(font=f"TkDefaultFont {size} {weight}")

if __name__ == '__main__':
    Application().mainloop()
