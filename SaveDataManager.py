import pickle


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


# Beispielcode:

leben = 3

file_Leben = SaveDataManager("saves/Leben.sv")

file_Leben.save_data(leben)

neue_Leben = file_Leben.load_data()

print(str(neue_Leben))

print("Hallo")
