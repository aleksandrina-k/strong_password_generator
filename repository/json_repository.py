import json
import os

from repository.repository import Repository


class JsonRepository(Repository):
    def __init__(self):
        super().__init__()
        self.db_filename = 'credentials.json'
        self.load()

    def save(self):
        with open(self.db_filename, mode='wt', encoding='utf-8') as f:
            json.dump(self.find_all(), f, indent=4, default=dumper)
            print('Saved in json!')

    def load(self):
        self._entities.clear()
        with open(self.db_filename, mode='rt', encoding='utf-8') as f:
            if os.path.getsize(self.db_filename) != 0:
                self._entities = json.load(f)
                print(f'Data loaded:\n{self._entities}')


# Helpers
def dumper(obj):
    if hasattr(obj, 'from_json'):
        return obj.to_json()
    return obj.__dict__
