import pickle


class SaveDataManager:
    def __init__(self):
        self.var = 1 + 1

    def save_data(self, data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            return None

