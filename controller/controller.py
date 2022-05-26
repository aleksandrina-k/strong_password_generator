from components.passwords_window import PasswordsWindow
from exception.password_not_generated_exception import PasswordNotGeneratedException
from components.save_window import SaveWindow


class Controller:
    def __init__(self, service, view=None):
        self.service = service
        self.view = view

    def set_view(self, view):
        self.view = view

    def generate_password(self, alpha_count, digit_count, special_count, length):
        return self.service.generate_password(alpha_count, digit_count, special_count, length)

    def open_save_window(self):
        if self.view.get_password() == '':
            raise PasswordNotGeneratedException
        SaveWindow(self.view, self)

    def open_passwords_window(self):
        PasswordsWindow(self.view, self)

    def add(self, username, app):
        self.service.add(username, app, self.view.get_password())
        self.save()

    def update(self, username, app):
        self.service.update(username, app, self.view.get_password())
        self.save()

    def get_apps(self):
        return self.service.get_apps()

    def get_password_by_app(self, app):
        return self.service.get_password_by_app(app)

    def save(self):
        self.service.save()


