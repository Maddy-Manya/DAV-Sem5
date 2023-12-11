import pandas as pd
import numpy as np

data = {
    'Column1': np.random.rand(50),
    'Column2': np.random.rand(50),
    'Column3': np.random.rand(50)
}

df = pd.DataFrame(data)

nans = np.random.choice(50, size=int(0.10*50), replace=False)
for col in df.columns:
    df.loc[nans, col] = np.nan

# a: Identify and count missing values
missing_values = df.isnull().sum()

# b: Drop columns with more than 5 null values
df = df.dropna(thresh=45, axis=1)

# c: Identify the row label with the maximum sum and drop that row
row_with_max_sum = df.sum(axis=1).idxmax()
df = df.drop(index=row_with_max_sum)

# d: Sort the DataFrame based on the first column
df = df.sort_values(by='Column1')

# e: Remove duplicates from the first column
df = df.drop_duplicates(subset='Column1')

# f: Find the correlation and covariance
correlation = df['Column1'].corr(df['Column2'])
covariance = df['Column2'].cov(df['Column3'])

# g: Detect and remove outliers
z_scores = (df - df.mean()) / df.std()
outliers = (z_scores.abs() > 3).any(axis=1)
df = df[~outliers]

# h: Discretize the second column into 5 bins
df['Column2_bins'] = pd.cut(df['Column2'], bins=5)

# Print the resulting DataFrame and summary statistics
print(df)
print("Missing Values:\n", missing_values)
print("Correlation between Column1 and Column2:", correlation)
print("Covariance between Column2 and Column3:", covariance)
