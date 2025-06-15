class DataStatistics:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
    
    def show_mean(self):
        print("\nMean of each column:")
        return self.df.mean()
    def show_median(self):
        print("\nMedian of each column:")
        return self.df.median()
    def show_mode(self):
        print("\nMode of each column:")
        return self.df.mode()
    def show_max(self):
        print("\nMaximum value in each column:")
        return self.df.max()
    def show_min(self):
        print("\nMinimum value in each column:")
        return self.df.min()
    def show_std(self):
        print("\nStandard Deviation of each column:")
        return self.df.std()
    def show_variance(self):
        print("\nVariance of each column:")
        return self.df.var()
    def show_count(self):
        print("\nCount of non-null values in each column:")
        return self.df.count()