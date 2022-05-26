from tkinter import messagebox

from exception.password_not_generated_exception import PasswordNotGeneratedException


class OpenSaveWindowCommand:
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        try:
            self.controller.open_save_window()
        except PasswordNotGeneratedException as e:
            messagebox.showwarning(message=e.msg)
