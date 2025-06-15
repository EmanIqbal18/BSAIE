import pandas as pd
class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, new_data):
        prediction = self.model.predict(new_data)
        return prediction