import pandas as pd
class BivariateAnalysis:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def correlation_matrix(self):
        print("\nCorrelation matrix:")
        print(self.df.corr())

    def covariance_matrix(self):
        print("\nCovariance matrix:")
        print(self.df.cov())

    def group_mean_by_target(self, target_col):
        print(f"\nMean of each feature grouped by '{target_col}':")
        print(self.df.groupby(target_col).mean())

    def group_count_by_target(self, target_col):
        print(f"\nCount of entries grouped by '{target_col}':")
        print(self.df.groupby(target_col).count())

    def crosstab_two_columns(self, col1, col2):
        print(f"\nCrosstab between '{col1}' and '{col2}':")
        print(pd.crosstab(self.df[col1], self.df[col2]))
