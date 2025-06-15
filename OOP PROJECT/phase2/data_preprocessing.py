class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def check_nulls(self):
        print("\nChecking for null values:")
        return self.df.isnull().sum()

    def replace_zeros(self):
        print("\nHandling zero values in selected columns...")
        # Columns where zero is not a valid value 
        cols_with_invalid_zeros = ['ID', 'Height', 'Weight', 'SystolicBP', 'Temperature']

        for col in cols_with_invalid_zeros:
            zero_count = (self.df[col] == 0).sum()
            median_value = self.df[self.df[col] != 0][col].median()
            print(f"Column '{col}' with median value: {median_value}")

    def rename_columns(self):
        renamed_columns = {
                'ID': 'ID',
                'Age': 'Age', 
                'Weight': 'Weight',
                'Height': 'Height',
                'SystolicBP': 'SBP',
                'DiastolicBP': 'DBP',
                'HeartRate': 'HR',
                'Temperature': 'Temp',
                'DiseaseOutcome': 'DO'

                }

        self.df.rename(columns=renamed_columns, inplace= True)
        print("Renamed columns successfully.")

    def get_clean_data(self):
        return self.df
        