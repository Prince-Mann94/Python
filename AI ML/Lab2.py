# import numpy as np

# # Create the array
# arr = np.array([10,5,7,20,15,-9,33])

# # Print the array
# print("Array : ",arr)

# # Find max and min values
# max_value = np.max(arr)
# min_value = np.min(arr)

# # Print the max and min values
# print("Maximum value : ",max_value)
# print("Minimum values : ",min_value)


# # Method 2 without using functions
# max_value = arr[0]
# for element in arr:
#     if element > max_value:
#         max_value = element

# print("Maximum value : ",max_value)

# min_value = arr[0]
# for element in arr:
#     if element < min_value:
#         min_value = element

# print("Minimum value : ",min_value)


# # 2. Add and subtract the matrices

# # Define the matrices
# matrix1 = np.array([[1,2],[3,4]])
# matrix2 = np.array([[2,4],[6,8]])

# # Print the array
# print("Matrix 1 : ",matrix1)
# print("MAtrix 2 : ",matrix2)

# # Find the sum of matrices
# sum_result = matrix1 + matrix2
# print("Sum of the matrices : ",sum_result)

# # Find the subtraction of matrices
# sub_result = matrix1 - matrix2
# print("Sub of matrices : ",sub_result)

# # 3. Create the random matrix and insert new row and then add rows

# # Generate a random matrix of size 5x6
# random_matrix = np.random.rand(5,6)
# print("Random matrix : ",random_matrix) 

# # Add another row with random elements
# new_row = np.random.rand(1,6)
# random_matrix = np.vstack([random_matrix,new_row])
# print("\nMatrix with added row : ",random_matrix)

# # Find the sum of each row
# row_sums = np.sum(random_matrix,axis=1)
# print("Sum of rows : ",row_sums)

# # 4. Create the random matrix and insert new column and then add column

# # Generate a random matrix of size 5x6
# random_matrix = np.random.randint(0,10,size=(5,6))
# print("Random matrix : ",random_matrix)

# # Add another column with random elements
# new_column = np.random.randint(0,10,size=(5,6))
# print("Random matrix : ",new_column)

# # 5. Find the sin of each element of matrix
# random_matrix = np.random.randint(0,10,size=(5,6))
# sin_matrix = np.sin(random_matrix)

# print("Sin of each element : ",sin_matrix)


# # 6. Create the random matrix of 5x6 and then extract specified rows and colums (3rd , 4th row) (2nd , 3rd , 4th column)

# # Generate a random matrix of 5x6
# random_matrix = np.random.randint(0,10,size=(5,6))
# print("Random matrix : ",random_matrix)

# # now extarct specified rows and columns
# resultant_matrix = random_matrix[2:4,1:4]
# print("\nResultant matrix : ",resultant_matrix) 


import pandas as pd
titanic = pd.read_csv("c:\\Users\\Princ\\OneDrive\\Documents\\titanic.csv")
print(titanic)
print(titanic.head(2)) # Displays the fisrt 2 rows of titanic Dataframe
print(titanic.tail(3)) # Displays the last 2 rows of titanic Dataframe

# Provides a concise summary of the Dataframes including column names , non-null counts , data type
print(titanic.info) 

# Provides descriptive stats (count , mean , std deviation , min , max , etc.) . This is only for numerical Dataframe
print(titanic.describe())

# Returns a tuple representing the dimensions of Dataframe (number of rows and columns)
print(titanic.shape)

# Returns the total number of elements in the Dataframe (rows x columns)
print(titanic.size)

# Displays the index (row labels) of the Dataframe
print(titanic.index)

# Displays the columns name of the Dataframe
print(titanic.columns)

# Selects teh 'age' column and returns it as a Series
print(type(titanic[["age"]]))

# Fetches the value
print(titanic["age"])

# Selects the 'sex' and 'age' columns (order matters)
print(titanic[["age","sex"]])
print(titanic[["sex","age"]])

# Selects the 'sex' , 'age' and 'fare' columns
print(titanic[["sex","age","fare"]])

# Access the 'age' colum using attribute-style notation
print(titanic.age)

# Checks whether the 'age' column accessed via dot notation is exactly same as accessing it using bracket notation
print(titanic.age.equals(titanic["age"]))

# Shows how many missing (NaN) values are present ine ach column
print(titanic.isnull().sum())

# Filters only numerical colums like age, fare, sibsp, parch, etc.
print(titanic.select_dtypes(include="number"))

# Computes the total sum for each nuemerical column
print(titanic.select_dtypes(include="number").sum())

# Computes max, min value of fare column.
print(titanic["fare"].max())
print(titanic["fare"].min())

# Computes the sum of null value of fare column
print(titanic["fare"].isnull().sum())