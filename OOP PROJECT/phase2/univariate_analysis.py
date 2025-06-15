class UnivariateAnalysis:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def unique_counts(self, column):
        print(f"\nUnique values in '{column}':")
        return self.df[column].nunique()

    def value_counts(self, column):
        print(f"\nValue counts in '{column}':")
        return self.df[column].value_counts()

    def column_summary(self, column):
        print(f"\nSummary statistics for '{column}':")
        return self.df[column].describe()

    def check_skewness(self, column):
        return f"\nSkewness of '{column}': {self.df[column].skew()}"

    def check_kurtosis(self, column):
        return f"\nKurtosis of '{column}': {self.df[column].kurt()}"

