import matplotlib.pyplot as plt
import seaborn as sns 
class UnivariatePlots:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def plot_histogram(self, column, bins=30, color='skyblue', edgecolor='black', figsize=(8, 4)):
        print(f"\nHistogram for '{column}'")
        plt.figure(figsize=figsize)
        plt.hist(self.df[column], bins=bins, color=color, edgecolor=edgecolor)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def plot_boxplot(self, column, color='salmon', figsize=(6, 4), orient='v'):
        print(f"\nBoxplot for '{column}'")
        plt.figure(figsize=figsize)
        if orient == 'v':
            sns.boxplot(y=self.df[column], color=color)
        else:
            sns.boxplot(x=self.df[column], color=color)
        plt.title(f'Boxplot of {column}')
        plt.tight_layout()
        plt.show()

    def plot_kde(self, column, color='purple', shade=True, figsize=(8, 4)):
        print(f"\nKDE Plot for '{column}'")
        plt.figure(figsize=figsize)
        sns.kdeplot(self.df[column], fill=shade, color=color)
        plt.title(f'KDE Plot of {column}')
        plt.xlabel(column)
        plt.tight_layout()
        plt.show()

    def plot_countplot(self, column, palette='Set2', figsize=(6, 4), orient='v'):
        print(f"\nCountplot for '{column}'")
        plt.figure(figsize=figsize)
        if orient == 'v':
            sns.countplot(x=self.df[column], hue=self.df[column], palette=palette, legend=False)
        else:
            sns.countplot(y=self.df[column], hue=self.df[column], palette=palette, legend=False)
        plt.title(f'Countplot of {column}')
        plt.tight_layout()
        plt.show()

