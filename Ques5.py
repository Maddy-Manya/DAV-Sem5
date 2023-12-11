import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import norm
import numpy as np
from scipy import stats

# Load Iris data
iris = load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# a. Load data into pandas' data frame. Use pandas.info () method to look at the info on datatypes in the dataset.
print("a. Data Types Info:")
print(iris_df.info())

# b. Find the number of missing values in each column
print("\nb. Number of Missing Values in Each Column:")
print(iris_df.isnull().sum())

# c. Plot bar chart to show the frequency of each class label in the data.
plt.figure(figsize=(8, 5))
sns.countplot(x='target', data=iris_df)
plt.title('Class Label Frequency')
plt.xlabel('Class Label')
plt.ylabel('Frequency')
plt.show()

# d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='sepal length (cm)', y='petal length (cm)', data=iris_df)
plt.title('Scatter Plot: Petal Length vs Sepal Length with Regression Line')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# e. Plot density distribution for feature Petal width.
plt.figure(figsize=(8, 6))
sns.kdeplot(iris_df['petal width (cm)'], fill=True)
plt.title('Density Distribution: Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.show()

# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
sns.pairplot(iris_df, hue='target')
plt.suptitle('Pairwise Bivariate Distribution in Iris Dataset', y=1.02)
plt.show()

# g. Draw heatmap for any two numeric attributes
plt.figure(figsize=(8, 6))
numeric_attributes = iris_df.select_dtypes(include=['float64'])
sns.heatmap(numeric_attributes.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap for Numeric Attributes')
plt.show()

# h. Compute mean, mode, median, standard deviation, confidence interval, and standard error for each numeric feature
numeric_summary = iris_df.describe().transpose()
mode_result = iris_df.mode().transpose()
confidence_interval_result = stats.t.interval(0.95, len(numeric_attributes) - 1,
                                              loc=numeric_attributes.mean(),
                                              scale=stats.sem(numeric_attributes))
numeric_summary['mode'] = mode_result[0]
numeric_summary['confidence_interval'] = confidence_interval_result[1] - confidence_interval_result[0]
numeric_summary = numeric_summary[['mean', 'mode', '50%', 'std', 'confidence_interval']]
print("\nh. Summary Statistics for Numeric Features:")
print(numeric_summary)

# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = iris_df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Coefficients Heatmap')
plt.show()