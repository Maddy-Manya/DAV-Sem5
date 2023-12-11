import pandas as pd  # importing pandas library
import numpy as np

# seq = pd.Series([2, 1, 29, 202])
# print(seq)
# seq_index = seq.index
# print(seq_index)


# series = pd.Series([2, 4, 8, 10], index=['a', 'b', 'c', 'd'])
# series_index = series.index
# print(series_index)

# # allows duplicates
# series = pd.Series([2, 4, 8, 10], index=['a', 'b', 'c', 'b'])
# series_index = series.index
# print(series_index)


# series_two = pd.Series(
#     range(10), index=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# series_two_index = series_two.index
# print(series_two_index[2:5])

# series_two = pd.Series(
#     range(10), index=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# series_two_index = series_two.index
# series_two_index[2] = 200
# print(series_two_index)


# error in cases when immutable and when insufficient index labels are given

# indirectly assigning labels
# indices = pd.Index(np.random.randint(1, 5, size=4))
# series_three = pd.Series(range(4), indices)
# series_three_index = series_three.index
# print(series_three.index is indices)

# index objects on dataframes
# data = {
#     'Sports': ['Football', 'Cricket', 'Badminton', 'Chess', 'Hockey', 'Golf'],
#     'Medals': ['10', '22', '8', '5', '17', '11']
# }
# dataframe = pd.DataFrame(
#     data, index=['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth'])
# print(dataframe)
# print(dataframe.columns)
# print('Seventh' in dataframe.index)

# Some methods -
a_labels = pd.Index(['a', 'b', 'c', 'd'])
b_labels = a_labels.append(pd.Index(['e']))  # a. append
Seq = pd.Series([100, 150, 200, 250, 300], b_labels)
print(f"append method : {Seq.index}")

c_labels = pd.Index(['a', 'n', 'o', 'd'])
print(f"difference method : {a_labels.difference(c_labels)}")  # b.difference

print(f"union method : {a_labels.union(c_labels)}")  # c.union

# d.intersection
print(f"intersection method : {a_labels.intersection(c_labels)}")

print(f"isin method : {a_labels.isin(c_labels)}")  # e. isin

d_labels = ['b', 'd']
print(f"delete method : {b_labels.drop(d_labels)}")  # f.drop

series = pd.Series([12, 123, 10, 1, 32], index=[
                   0, 1, 3, 5, 10])  # e.is_monotonic
print(f"is_monotonic method : {series.index.is_monotonic_increasing}")

print(f"is_unique method : {Seq.index.is_unique}")  # f.is_unique

print(f"unique method : {Seq.index.unique}")  # g.unique
