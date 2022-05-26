from controller.controller import Controller
from repository.json_repository import JsonRepository
from service.service import Service
from components.view import View


class App:
    def __init__(self, root):
        self.root = root
        self.repo = JsonRepository()
        self.service = Service(self.repo)
        self.controller = Controller(self.service)
        view = View(self.root, self.controller)
        self.controller.set_view(view)
