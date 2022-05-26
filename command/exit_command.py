from tkinter import Tk, messagebox


class ExitCommand:
    def __init__(self, root):
        self.root = root

    def __call__(self, *args, **kwargs):
        res = messagebox.askquestion('Ask Question', 'Are you sure?')
        if res == 'yes':
            self.root.destroy()
