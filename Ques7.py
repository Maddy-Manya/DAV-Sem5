import pandas as pd

# Create the DataFrame with the given data
data = {
    'Name': ["Mudit Chauhan", "Seema Chopra", "Rani Gupta", "Aditya Narayan", "Sanjeev Sahni",
             "Prakash Kumar", "Ritu Agarwal", "Akshay Goel", "Meeta Kulkarni", "Preeti Ahuja",
             "Sunil Das Gupta", "Sonali Sapre", "Rashmi Talwar", "Ashish Dubey", "Kiran Sharma", "Sameer Bansal"],
    'Birth_Month': ["December", "January", "March", "October", "February", "December", "September", "August",
                    "July", "November", "April", "January", "June", "May", "February", "October"],
    'Gender': ["M", "F", "F", "M", "M", "M", "F", "M", "F", "F", "M", "F", "F", "M", "F", "M"],
    'Pass_Division': ["III", "II", "I", "I", "II", "III", "I", "I", "II", "II", "III", "I", "III", "II", "II", "I"]
}

df = pd.DataFrame(data)

# a: Perform one-hot encoding of the last two columns of categorical data
df_encoded = pd.get_dummies(df, columns=['Birth_Month', 'Gender'])

# b: Sort the data frame on the "Birth Month" column
# First, convert "Birth_Month" to a Categorical type with custom ordering
month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
df_encoded['Birth_Month'] = pd.Categorical(
    df_encoded['Birth_Month'], categories=month_order, ordered=True)
df_encoded = df_encoded.sort_values(by='Birth_Month')

print(df_encoded)
