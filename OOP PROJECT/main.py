from phase2.data_loading import dataloader
from phase2.data_preprocessing import DataCleaner
from phase2.data_statistics import DataStatistics
from phase2.univariate_analysis import UnivariateAnalysis
from phase2.univariate_plot import UnivariatePlots
from phase2.bivariate_analysis import BivariateAnalysis
from phase2.bivariate_plot import BivariatePlots
from phase2.data_splitter import DataSplitter
from phase2.model_trainer import ModelTrainer
from phase2.model_evaluator import ModelEvaluator
from phase2.model_predictor import Predictor
from phase2.pickles import PickleHandler

loader = dataloader("people_data.csv")
print(loader.load_data())
print(loader.show_head())
print(loader.show_tail())
print(loader.show_sample())
print(loader.show_description())
print(loader.show_info())

loader = dataloader("people_data.csv")
loader.load_data()
df = loader.df
cleaner = DataCleaner(df)
print(cleaner.check_nulls())
print(cleaner.replace_zeros())
print(cleaner.rename_columns())

# Get the cleaned and updated dataframe
cleaned_df = cleaner.get_clean_data()
print(cleaned_df)
# Assuming 'cleaned_df' is the dataframe after cleaning
stats = DataStatistics(cleaned_df)

print(stats.show_mean())
print(stats.show_median())
print(stats.show_mode())
print(stats.show_max())
print(stats.show_min())
print(stats.show_std())
print(stats.show_variance())
print(stats.show_count())

# Univariate
uni = UnivariateAnalysis(cleaned_df)
print(uni.unique_counts('Age'))
print(uni.value_counts('SBP'))
print(uni.column_summary('HR'))
print(uni.check_skewness('Height'))
print(uni.check_kurtosis('Temp'))

# Bivariate
bi = BivariateAnalysis(cleaned_df)
print(bi.correlation_matrix())
print(bi.covariance_matrix())
print(bi.group_mean_by_target('ID'))
print(bi.group_count_by_target('Age'))
print(bi.crosstab_two_columns('Age', 'DO'))

uni_plot = UnivariatePlots(cleaned_df)

# Histogram with custom color and bins
uni_plot.plot_histogram("Age", bins=20, color="pink", edgecolor="violet", figsize=(10, 5))

# Boxplot horizontal
uni_plot.plot_boxplot("DBP", color="violet", figsize=(8, 4), orient='h')

# KDE Plot with custom shade color
uni_plot.plot_kde("Age", color="purple", shade=True, figsize=(10, 5))

# Countplot for Outcome (categorical)
uni_plot.plot_countplot("DBP", palette="pastel", figsize=(7, 4))

bi_plot = BivariatePlots(cleaned_df)

bi_plot.scatter_plot('DBP', 'SBP', palette='magma', figsize=(10, 6))

bi_plot.correlation_heatmap(cmap='PiYG', figsize=(12, 10))

# Boxplot with custom size and palette
bi_plot.boxplot_by_category("Age", palette="PiYG", figsize=(8, 5))


# Splitting the data
splitter = DataSplitter(cleaned_df, target_column='DO')
X_train, X_test, y_train, y_test = splitter.split_data(test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test

# 2. Train the model
trainer = ModelTrainer()
trainer.train_model(X_train, y_train)

# Evaluating the model
evaluator = ModelEvaluator(trainer.model, X_test, y_test)
print(evaluator)


# Show predictions
predictions = evaluator.show_prediction()
print(predictions)

# Accuracy score
accuracy = evaluator.show_accuracy()
print(accuracy)

    
print(evaluator.show_classification_report())

# Confusion matrix
print(evaluator.show_confusion_matrix())

# 4. Predict on new/test data (Optional)

predictor = Predictor(trainer.model)

new_data = pd.DataFrame({  # type: ignore
    'ID': [101],
    'Age': [45],
    'Weight': [70],
    'Height': [175],
    'SBP': [120],
    'DBP': [80],
    'HR': [75],
    'Temp': [36.5]})

# Prediction (0 = not sick , 1 = sick)
result = predictor.predict(new_data)
print("Predicted DiseaseOutcome:", "sick" if result[0] == 1 else "Not Sick")








