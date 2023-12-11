import pandas as pd

# Create a DataFrame with the given data
data = {
    'Name': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome (Rs.)': [114000.00, 65000.00, 43150.00, 69500.00, 155000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}

df = pd.DataFrame(data)

# a: Calculate and display familywise gross monthly income
family_gross_income = df.groupby('Name')['MonthlyIncome (Rs.)'].sum()
print("Familywise Gross Monthly Income:")
print(family_gross_income)

# b: Calculate and display the member with the highest monthly income in a family
member_highest_income = df.groupby('Name')['MonthlyIncome (Rs.)'].idxmax()
highest_income_members = df.loc[member_highest_income]
print("\nMember with Highest Monthly Income in Each Family:")
print(highest_income_members)

# c: Calculate and display monthly income of all members with income greater than Rs. 60000.00
income_greater_than_60000 = df[df['MonthlyIncome (Rs.)'] > 60000.00]
print("\nMonthly Income of Members with Income > 60000.00:")
print(income_greater_than_60000)

# d: Calculate and display the average monthly income of the female members in the Shah family
shah_female_avg_income = df[(df['Name'] == 'Shah') & (
    df['Gender'] == 'Female')]['MonthlyIncome (Rs.)'].mean()
print("\nAverage Monthly Income of Female Members in the Shah Family:")
print(shah_female_avg_income)
