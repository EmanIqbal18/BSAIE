import pickle as pkl
import pandas as pd
class PickleHandler:
    def __init__(self, filepath='people_data.pkl'):
        self.filepath = filepath

    def save_model(self, model):
        with open(self.filepath, 'wb') as file:
            pkl.dump(model, file)
        print(f" Model saved to '{self.filepath}' successfully.")

    def load_model(self):
        with open(self.filepath, 'rb') as file:
            model = pkl.load(file)
        print(f"Model loaded from '{self.filepath}' successfully.")
        return model

