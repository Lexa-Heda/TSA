import pickle


def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        return None

