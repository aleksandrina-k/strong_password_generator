import _tkinter
from tkinter import messagebox

from exception.characters_total_count_too_big import CharactersTotalCountTooBig
from exception.invalid_input_exception import InvalidInputException
from exception.length_required_exception import LengthRequiredException


class GeneratePasswordCommand:
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, alpha_count, digit_count, special_count, length):
        try:
            result = self.controller.generate_password(alpha_count, digit_count, special_count, length)
            self.controller.view.set_password(result)
        except InvalidInputException:
            messagebox.showwarning(message="Negative numbers not allowed!")
        except LengthRequiredException:
            messagebox.showwarning(message="Length must be greater than 0!")
        except CharactersTotalCountTooBig:
            messagebox.showwarning(message="Characters total count is greater than the password length")
