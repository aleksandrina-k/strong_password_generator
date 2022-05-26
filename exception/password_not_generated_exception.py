class PasswordNotGeneratedException(Exception):
    def __init__(self):
        self.msg = 'Password not generated!'
