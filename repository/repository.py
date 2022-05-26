# from util.rsa_functions import encrypt, decrypt
from util.rsa import encrypt, decrypt


class Repository:
    def __init__(self):
        self._entities = {}

    def add(self, username, app, password):
        encrypted_password = encrypt(password)
        self._entities[app] = {'username': username, 'password': encrypted_password}

    def update(self, username, app, password):
        encrypted_password = encrypt(password)
        self._entities[app] = {'username': username, 'password': encrypted_password}

    def get_passwords(self):
        passwords = []
        for app, credentials in self._entities.items():
            passwords.append(credentials['password'])
        return passwords

    def get_apps(self):
        return list(self._entities.keys())

    def get_password_by_app(self, app):
        encrypted_str = self._entities[app].get('password')
        password = decrypt(encrypted_str)
        return password

    def find_all(self):
        return self._entities
