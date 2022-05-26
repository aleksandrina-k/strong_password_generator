import pyperclip


class CopyToClipboardCommand:
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, item):
        pyperclip.copy(item)
        result = pyperclip.paste()
        print(f'Copy {result}')
