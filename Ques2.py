import numpy as np

# a.
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
upper = int(input("Enter the max range : "))
lower = int(input("Enter the min range : "))

a = np.random.randint(lower, upper, size=(rows, columns))
print(f"2d Array : ")
print(a)
a_mean = np.mean(a, axis=0)
a_sd = np.std(a, axis=0)
a_var = np.var(a, axis=0)
print(f"Mean : {a_mean}")
print(f"Standard Deviation : {a_sd}")
print(f"Variance : {a_var}")


# b.
B = np.array([56, 48, 22, 41, 78, 91, 24, 46, 8, 33])
sorted_array = np.sort(B)
sorted_indices = np.argsort(B)
print(f"Sorted Array Indices : {sorted_indices}")


# c.
m = int(input("Enter the number of rows : "))
n = int(input("Enter the number of columns : "))
upper = int(input("Enter the max range : "))
lower = int(input("Enter the min range : "))

a = np.random.randint(lower, upper, size=(m, n))
print(f"2d Array : ")
print(a)
print(f"Shape of array : {np.shape(a)}")
print(f"Data Type of array : {a.dtype}")
print(f"After Reshaping : ")
print(np.reshape(a, (n, m)))


# d.
S = np.array([0, 28, 39, 1, 0, 273, np.nan, 12, 0, 0, np.nan])
zero_indices = np.where(S == 0)
non_zero_indices = np.where(S != 0)
nan_indices = np.where(np.isnan(S))

print(f"Indices with zero values : {zero_indices}")
print(f"Indices with non-zero values : {non_zero_indices}")
print(f"Indices with Nan values : {nan_indices}")
