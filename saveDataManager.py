import pickle
from main import *

class SaveDataManager:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            return None

