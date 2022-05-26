from tkinter import *
from tkinter import ttk, messagebox

from command.copy_to_clipboard_command import CopyToClipboardCommand
from components.password_list_frame import PasswordListFrame


class PasswordsWindow(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        self.title('My Password')
        self.geometry('400x400')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Commands
        self.copy_command = CopyToClipboardCommand(self.controller)

        # Tree
        # self.password_list = PasswordListFrame(self, self.controller.get_apps())
        # self.password_list.grid(row=0, column=0, sticky='n')

        # Listbox
        scrollbar = Scrollbar(self, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox = Listbox(self, width=50, height=20, yscrollcommand=scrollbar.set)

        scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(row=0, column=0, sticky='n')

        # Buttons Frame
        buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky="s")
        self.btn_copy = Button(buttons_frame, text='Copy to clipboard',
                               command=lambda: self.copy_command(
                                   self.get_password_by_app(
                                       self.listbox.get(ANCHOR)
                                   )
                               ),
                               width=15,
                               height=1)
        self.btn_copy.grid(row=0, column=0, padx=40, pady=20)

        self.set_items(self.controller.get_apps())

        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def set_items(self, items):
        self.listbox.delete(0, END)
        for item in items:
            self.listbox.insert(END, item)

    def get_password_by_app(self, app):
        return self.controller.get_password_by_app(app)
