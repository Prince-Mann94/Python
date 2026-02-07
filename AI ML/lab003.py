# Q1 Write a python command to load the dataset and print first 10 rows
import pandas as pd
summer = pd.read_csv(r"C:\Users\Princ\OneDrive\Documents\summer.csv")
print(summer.head(10))

# Q2 Write a python command to find the total number of rows and columns in the dataset
print(summer.shape)

# Q3 Using python, command compute the minimum and maximum olympic year present in the datatset
print(summer["Year"].min())
print(summer["Year"].max())

# Q4 Write the python command to calculate the number of medals won by each gender and display the result in descending order
print(summer.groupby("Gender")["Medal"].count().sort_values(ascending = False))

# Q5 Using python, command determine the top 5 countries with the highest number of medals
print(summer.groupby("Country")["Medal"].count().sort_values(ascending = False).head(5))

# Q6 Using python, command calculate the distribution of medals type (Gold,silver,bronze) and determine which medal type occurs frequently
dis = summer["Medal"].value_counts()
print(dis)
print(dis.idxmax())

# Q7 Write python code to find out which sports appears only in one olympic year in dataset
count = summer.groupby("Sport")["Year"].nunique()
min = count[count == 1]
print(min)

# Q8 Check whether an athlete has won multiple medal types(Gold,silver,bronze) . Display the athlete name along with medal type
ath = summer.groupby("Athlete")["Medal"].nunique()
mul = ath[ath.apply(len) > 1]
print(mul)

# Q9 Using pandas, compute the total medal score per country and display top 10 countries
print(summer.groupby("Country")["Medal"].count().sort_values(ascending = False).head(10))

# Q10 Write python code to display the structure of dataset including columns names , datatype and non-null counts

print(summer.info())
