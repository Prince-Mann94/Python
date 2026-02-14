import pandas as pd
summer = pd.read_csv(r"C:\Users\Princ\OneDrive\Documents\summer.csv",index_col = "Athlete")    # Reads the CSV file and sets "Athlete" to index 0 .
# print(summer)
# print(summer.info())   # Displays a summary of the Dataframe including column names , data types , no-null counts
                       # and memory usage  (object means = text / string data / mixed text)

# print(summer.iloc[0])  # Selects the first row (by position) from the dataframe (iloc means integer location)

# print(type(summer.iloc[0]))  # shows the data type of first row using iloc (returns a series)

# print(summer.iloc[1])    # selects the second row using positional indexing

# print(summer.iloc[-1])   # selects the last row of the dataframe using negative indexing

# print(summer.iloc[[1,2,3]])  # selects the rows at positions 1,2,3 and retruns datatype as dataframe

# print(summer.iloc[1:4])   # selects rows from position 1 to 3 (end index excluded)

# print(summer.iloc[:5])    # selects the first 5 rows of the dataframe

# print(summer.iloc[-5:])   # selects the last 5 rows of the dataframe

# print(summer.iloc[:])     # selects all rows and all columns of the dataframe

# print(summer.iloc[[2,45,5467]]) # selects rows at positions at 2,45,5467

# print(summer.head(10))   # displays first 10 rows of the dataframe

# print(summer.iloc[0,4])  # selcts the value at row 0 and column index 4

# print(summer.iloc[0:4,-1])  # takes the values

# print(summer.iloc[0,:3])  # selcts the first row and first three columns

# print(summer.iloc[0, [0,2,5,7]])  # selects the first row and columns at positions 0,2,5 and 7

# print(summer.iloc[34:39, [0,2,5,7]])  # selects rows from position 34 to 38 and columns at position 0,2,5,7

# print(summer.iloc[:,4].equals(summer.Country))   # checks whether column at index 4 is identical to the 'Country'

# print(summer["Country"])   # selects the 'Country' column using label-based indexing

# print(summer.loc["DRIVAS, Dimitrios"])  # selects all records for athlete 'DRIVAS , Dimitrios' using indexing

# print(summer.loc["PHELPS, Michael", "Medal"])  # selects only Medals records of the given athletes

# print(summer.loc["PHELPS, Michael", ["Medal", "Event"]])   # selects 'Medal' and 'Event' columns for athlete

# print(summer.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]]) # selects medal and event 

print(summer.loc[:, ["Medal", "Event"]])  # selects 'Medal' and 'Event' columns for all athletes

print(summer.head(10))  # Displays the first 10 rows again for references

print(summer.loc[:"CHASAPIS, Spiridon"])  # selects all rows from the start up to and including athelete 'CHASAPIS, Spiridon'