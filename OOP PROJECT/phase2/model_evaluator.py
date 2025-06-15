from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
class ModelEvaluator:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.predictions = self.model.predict(self.X_test)

    def show_prediction(self):
        return self.predictions
    
    def show_accuracy(self):
        print("\nAccuracy Score:")
        return accuracy_score(self.y_test, self.predictions)
    
    def show_confusion_matrix(self):
        print("\nConfusion Matrix:")
        return confusion_matrix(self.y_test, self.predictions)
    
    def show_classification_report(self):
        print("\nClassification Report:")
        return classification_report(self.y_test, self.predictions)