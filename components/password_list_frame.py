from tkinter import *
from tkinter import ttk


class PasswordListFrame(ttk.Frame):
    def __init__(self, parent, items):
        super().__init__(parent, padding="3 3 12 12")
        self.parent = parent
        self.items = items
        self.grid(row=0, column=0, sticky=NSEW)

        columns = ('application',)
        self.tree = ttk.Treeview(self, columns=columns, selectmode='extended', show='headings')
        self.tree.heading('application', text='Application')
        self.tree.grid(row=0, column=0, sticky=NSEW)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.set_items(self.items)

    def set_items(self, items):
        self.tree.delete(*self.tree.get_children())
        for item in items:
            self.tree.insert('', END, values=item)
