# Load the titanic.csv dataset using pandas and plot the 'fare' column with a line plot . customize the plot to have a green line with  
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv(r"c:\Users\Princ\OneDrive\Documents\titanic.csv")
# plt.figure(figsize=(12,8))
# plt.plot(titanic['fare'], linestyle='-',marker='^', color='g')
# plt.title("Fare plot", fontsize=15)
# plt.xlabel("passegener No", fontsize=15)
# plt.ylabel("Fare",fontsize=13)
# plt.show()

# Create a bar chart of the 'pclass' column in Titanic dataset , showing the count of each class . set the color of the bars to blue .
# pclass_counts = titanic['pclass'].value_counts()
# plt.figure (figsize=(12,8))
# plt.bar(pclass_counts.index,pclass_counts.values,color='blue')
# plt.title("Passenger class distribution",fontsize=20)
# plt.xlabel("class",fontsize=13)
# plt.ylabel("Count",fontsize=13)
# plt.show()

# Create a piechat for the 'sex' column in the titainic dataset . set the colors to ['lightblue','pink'] and add a title "Gender Distribution" .

# sex_counts = titanic['sex'].value_counts()
# plt.figure(figsize=(12,8))
# plt.pie(sex_counts,labels=sex_counts.index,colors=['lightblue','pink'], autopct='%1.1f%%')
# plt.title("Gender Distribution", fontsize=15)
# plt.ylabel('')  # hides the y-label
# plt.show()

# Using the titanic dataset , plot a scatter plot of 'age' vs 'fare' and color the points by 'survived' . Set the colormap to 'coolwarm' .
# plt.figure(figsize=(15,8))
# plt.scatter(titanic['age'], titanic['fare'], c=titanic['survived'], cmap='viridis', s=20)
# plt.title("Age vs Fare (colored by Survived)", fontsize=15)
# plt.xlabel("Age", fontsize=13)
# plt.ylabel("Fare", fontsize=13)

# plt.colorbar(label="survived")
# plt.show()
# Using the titanic dataset plot a customized scatter plot of 'age' vs 'fare' with the size of the points dteermined by 'sibsp' (number of siblings/spouse abroad)
# plt.figure(figsize=(15,8))
# plt.scatter(titanic['age'], titanic['fare'], s=titanic['sibsp']*20, alpha=0.5)
# plt.title("Age vs Fare (Point size by siblings/spouses abroad)", fontsize=15)
# plt.xlabel("Age", fontsize=13)
# plt.ylabel("Fare", fontsize=13)
# plt.show()

# Plot a histogram of the 'age' column from the titanic dataset . Customize the histogram to have 50 bins , a title "Age Distribution", and a red color for the bars.
# plt.figure(figsize=(12,8))
# plt.hist(titanic['age'].dropna(), bins=50, color='r')
# plt.title("Age Distribution", fontsize=15)
# plt.xlabel("Age", fontsize=13)
# plt.ylabel("Frequency",fontsize=13)
# plt.show()

#using the titanic dataset , create a line plot of tge 'age' column and customise the x-axis and y-axis ticks to show every 100 passengers and every 10 years of age , respectively

# age_data = titanic['age'].dropna().reset_index(drop=True)

# plt.figure(figsize=(15,6))

# plt.plot(age_data)

# plt.title("Line Plot of Passenger Age", fontsize=15)
# plt.xlabel("Passenger Number", fontsize=13)
# plt.ylabel("Age (Years)", fontsize=13)

# plt.xticks(pd.arange(0, len(age_data), 100)) 
# plt.yticks(pd.arange(0, 90, 10))               

# plt.grid(True)
# plt.show()

# create a cummulative histogram of the 'fare' column from the titanic dataset with 50 bins and a blue color
# plt.figure(figsize=(12,8))
# plt.hist(titanic['age'].dropna(), bins=50,cumulative=True, color='b')
# plt.title("Cumulative frequency", fontsize=15)
# plt.xlabel("Fare", fontsize=13)
# plt.ylabel("Cumulative Frequency",fontsize=13)
# plt.show()

# create a histogram of the 'age' column from the titanic dataset, setting the y-axis label to 'density' and enabling density normalization
# plt.figure(figsize=(12,8))
# plt.hist(titanic['age'].dropna(), bins=50,density=True, color='c')
# plt.title("Age distribution with density", fontsize=15)
# plt.xlabel("age", fontsize=13)
# plt.ylabel("Density",fontsize=13)
# plt.show()

# Using the titanic dataset create a line plot of the 'age' column . Customise the plot with a dashes line style , magenta color , and then add a grid
plt.figure(figsize=(12,8))
titanic['age'].plot(linestyle='--',color='m')
plt.title("Age plot with customizations", fontsize=15)
plt.xlabel("Passenger no.", fontsize=13)
plt.ylabel("age",fontsize=13)
plt.grid(True)
plt.show()