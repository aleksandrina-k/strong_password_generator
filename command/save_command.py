from tkinter import messagebox
from exception.app_already_has_password_exception import AppAlreadyHasPasswordException
from exception.credentials_exception import CredentialsException


class SaveCommand:
    def __init__(self, controller, view):
        self.controller = controller
        self.view = view

    def __call__(self, username, app):
        try:
            self.controller.add(username, app)
            self.view.destroy()
        except CredentialsException as e:
            messagebox.showinfo(message=e.msg)
        except AppAlreadyHasPasswordException:
            res = messagebox.askquestion('askquestion', 'There is password for this app. Do you want to replace it?')
            if res == 'yes':
                self.controller.update(username, app)
                messagebox.showinfo(message='Password replaced successfully!')
                self.view.destroy()
        # except Exception:
        #     messagebox.showwarning(message='Something went wrong!')
