
from sklearn.model_selection import train_test_split
class DataSplitter:
    def __init__(self, dataframe, target_column):
        self.df = dataframe
        self.target = target_column

    def split_data(self, test_size=0.3, random_state=42):
        X = self.df.drop(self.target, axis=1)
        y = self.df[self.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test