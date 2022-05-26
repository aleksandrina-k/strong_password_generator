from tkinter import *
from tkinter import ttk

from command.copy_to_clipboard_command import CopyToClipboardCommand
from command.exit_command import ExitCommand
from command.generate_password_command import GeneratePasswordCommand
from command.open_commands.open_passwords_window_command import OpenPasswordsWindowCommand
from command.open_commands.open_save_window_command import OpenSaveWindowCommand


class View(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.controller = controller

        self.root.title('Strong Password Generator')
        self.root.geometry('900x600')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # self.bg = PhotoImage(file='lock1.png')
        # self.label_bg = Label(self.root, image=self.bg)
        # self.label_bg.place(x=0, y=0)

        # Commands
        self.generate_password_command = GeneratePasswordCommand(self.controller)
        self.copy_to_clipboard_command = CopyToClipboardCommand(self.controller)
        self.open_save_window_command = OpenSaveWindowCommand(self.controller)
        self.open_passwords_window_command = OpenPasswordsWindowCommand(self.controller)
        self.exit_command = ExitCommand(self.root)

        # Entries
        self.entry_password = Entry(self.root, bd=5, state=DISABLED, width=47)
        self.entry_password.place(x=325, y=425)

        # Labels
        self.lbl_alpha_count = Label(self.root, text='Alphabets count')
        self.lbl_digit_count = Label(self.root, text='Digits count')
        self.lbl_special_count = Label(self.root, text='Special symbols count')
        self.lbl_length = Label(self.root, text='Length')

        self.lbl_alpha_count.place(x=325, y=150)
        self.lbl_digit_count.place(x=325, y=200)
        self.lbl_special_count.place(x=325, y=250)
        self.lbl_length.place(x=325, y=300)

        # Sliders
        self.scale_alpha_count = Scale(self.root, from_=0, to=20, orient=HORIZONTAL, length=150)
        self.scale_digit_count = Scale(self.root, from_=0, to=20, orient=HORIZONTAL, length=150)
        self.scale_special_count = Scale(self.root, from_=0, to=20, orient=HORIZONTAL, length=150)
        self.scale_length = Scale(self.root, from_=12, to=40, orient=HORIZONTAL, length=150)

        self.scale_alpha_count.place(x=475, y=130)
        self.scale_digit_count.place(x=475, y=180)
        self.scale_special_count.place(x=475, y=230)
        self.scale_length.place(x=475, y=280)

        # Buttons
        self.btn_generate = Button(root, text='Generate',
                                   command=lambda: self.generate_password_command(
                                       self.scale_alpha_count.get(),
                                       self.scale_digit_count.get(),
                                       self.scale_special_count.get(),
                                       self.scale_length.get()
                                   ),
                                   width=15, height=1)

        self.btn_copy = Button(root, text='Copy to clipboard',
                               command=lambda: self.copy_to_clipboard_command(self.get_password()), width=15,
                               height=1)
        self.btn_refresh = Button(root, text='Refresh', command=self.reset, width=15, height=1)
        self.btn_save = Button(root, text='Save', command=self.open_save_window_command, width=15, height=1)
        self.btn_my_passwords = Button(root, text='My Passwords', command=self.open_passwords_window_command, width=15,
                                       height=1)
        self.btn_exit = Button(root, text='Exit', command=self.exit_command, width=15, height=1)

        self.btn_generate.place(x=325, y=375)
        self.btn_copy.place(x=495, y=375)
        self.btn_refresh.place(x=0, y=0)
        self.btn_save.place(x=0, y=25)
        self.btn_my_passwords.place(x=0, y=50)
        self.btn_exit.place(x=0, y=75)

    def set_password(self, password):
        self.entry_password.config(state='normal')
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password)
        self.entry_password.config(state='disabled')

    def get_password(self):
        return self.entry_password.get()

    def reset(self):
        self.set_password('')
        self.scale_alpha_count.set(0)
        self.scale_digit_count.set(0)
        self.scale_special_count.set(0)
        self.scale_length.set(0)
