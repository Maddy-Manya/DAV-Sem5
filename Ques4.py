import pandas as pd

# Load data from the two Excel files into dataframes
file1 = 'workshop_day1.xlsx'
file2 = 'workshop_day2.xlsx'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# a: Perform merging to find the names of students who attended both days
both_days_attendance = pd.merge(df1, df2, on='Name', how='inner')
print("Students who attended both days:")
print(both_days_attendance)

# b: Find names of all students who attended the workshop on either of the days
either_day_attendance = pd.merge(df1, df2, on='Name', how='outer')
print("Students who attended either day:")
print(either_day_attendance)

# c: Merge two data frames row-wise and find the total number of records
total_records = pd.concat([df1, df2], ignore_index=True)
print("Total number of records:")
print(total_records)

# d: Merge two data frames and use 'names' and 'duration' as multi-row indexes, then generate descriptive statistics
merged_df = pd.merge(df1, df2, on=['Name', 'duration'], how='outer')
print("Merged DataFrame with multi-row indexes:")
print(merged_df)

# Generate descriptive statistics for the multi-index dataframe
statistics = merged_df.groupby(['Name', 'duration']).describe()
print("Descriptive statistics for the multi-index:")
print(statistics)
