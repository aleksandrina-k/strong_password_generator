import string
import random
from exception.app_already_has_password_exception import AppAlreadyHasPasswordException
from exception.characters_total_count_too_big import CharactersTotalCountTooBig
from exception.credentials_exception import CredentialsException
from exception.invalid_input_exception import InvalidInputException
from exception.length_required_exception import LengthRequiredException


class Service:
    def __init__(self, repo):
        self.repo = repo

    def generate_password(self, alpha_count, digit_count, special_count, length):

        if alpha_count < 0 or digit_count < 0 or special_count < 0 or length < 0:
            raise InvalidInputException
        if length == 0:
            raise LengthRequiredException

        alphabets = list(string.ascii_letters)
        digits = list(string.digits)
        special_characters = list("!@#$%^&*()")
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        characters_count = alpha_count + digit_count + special_count

        if characters_count > length:
            print("Characters total count is greater than the password length")
            raise CharactersTotalCountTooBig

        password = []

        # getting random alphabets
        for i in range(alpha_count):
            password.append(random.choice(alphabets))

        # getting random digits
        for i in range(digit_count):
            password.append(random.choice(digits))

        # getting random alphabets
        for i in range(special_count):
            password.append(random.choice(special_characters))

        # if the total characters count is less than the password length
        # add random characters to make it equal to the length
        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))

        # shuffle until we get unique password
        while True:
            random.shuffle(password)
            if password not in self.repo.get_passwords():
                break

        result = "".join(password)
        print(f'Generate {result}')
        return result

    def add(self, username, app, password):
        if username == '' or app == '':
            raise CredentialsException('All fields required!')
        if app in self.repo.get_apps():
            raise AppAlreadyHasPasswordException
        self.repo.add(username, app, password)

    def update(self, username, app, password):
        self.repo.add(username, app, password)

    def get_apps(self):
        return self.repo.get_apps()

    def get_password_by_app(self, app):
        return self.repo.get_password_by_app(app)

    def save(self):
        self.repo.save()