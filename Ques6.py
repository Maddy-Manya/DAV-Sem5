import pandas as pd

# Sample DataFrame
data = {
    'sales': [10, 15, 20, 25, 30, 35],
    'group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-08']),
    'year_month': ['2023-01', '2023-02', '2023-01', '2023-02', '2023-01', '2023-02'],
    'group1': ['X', 'X', 'Y', 'Y', 'X', 'Y'],
    'group2': ['P', 'P', 'Q', 'Q', 'P', 'Q'],
    'value': [5, 8, 12, 18, 22, 30]
}

df = pd.DataFrame(data)

# a. Compute mean of a series grouped by another series
mean_sales_by_group = df.groupby('group')['sales'].mean()
print("Mean Sales by Group:\n", mean_sales_by_group, "\n")

# b. Fill an intermittent time series
df = df.set_index('date')
df = df.resample('D').ffill()
print("Interpolated Time Series:\n", df, "\n")

# c. Perform appropriate year-month string to dates conversion
df['year_month'] = pd.to_datetime(df['year_month'], format='%Y-%m')
print("Converted Year-Month to Dates:\n", df, "\n")

# d. Split a dataset to group by two columns and then sort the aggregated results within the groups
sorted_aggregated_result = df.groupby(['group1', 'group2']).agg({'value': 'sum'}).sort_values(['group1', 'group2', 'value'])
print("Sorted Aggregated Result:\n", sorted_aggregated_result, "\n")

# e. Split a given dataframe into groups with bin counts
bins = [0, 10, 20, 30, 40]  # Define your bin edges
labels = ['bin1', 'bin2', 'bin3', 'bin4']  # Define labels for each bin
df['bin'] = pd.cut(df['value'], bins=bins, labels=labels)
grouped_by_bin = df.groupby('bin')
for name, group in grouped_by_bin:
    print(f"Bin {name}:\n{group}\n")