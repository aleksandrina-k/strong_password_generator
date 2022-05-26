from tkinter import *
from tkinter import ttk

from command.save_command import SaveCommand


class SaveWindow(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        self.title('Save password')
        self.geometry('450x300')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        username = StringVar()
        app = StringVar()

        # Entries
        self.entry_username = Entry(self, bd=5, textvariable=username)
        self.entry_app = Entry(self, bd=5, textvariable=app)

        self.entry_username.place(x=170, y=50)
        self.entry_app.place(x=170, y=100)

        # Labels
        self.lbl_username = Label(self, text='Username')
        self.lbl_app = Label(self, text='App')

        self.lbl_username.place(x=90, y=50)
        self.lbl_app.place(x=90, y=100)

        # Commands
        self.save_command = SaveCommand(self.controller, self)

        # Buttons
        self.btn_save = Button(self, text='Save',
                               command=lambda: self.save_command(username.get(), app.get()),
                               width=15, height=1)

        self.btn_save.place(x=140, y=150)

        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()
