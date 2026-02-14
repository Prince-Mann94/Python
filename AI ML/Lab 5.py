import matplotlib.pyplot as plt
# Data
# cities = ['New York','Los Angeles','Chicago','Houston','Phoenix']
# populations = [8419000,3980000,2716000,2328000,1690000]

# # Colors for each bar
# colors = ['blue','green','red','purple','orange']

# # Plotting the bar graph
# plt.bar(cities,populations,color=colors)

# # Adding title and labels
# plt.title('population of five cities')
# plt.xlabel('cities')
# plt.ylabel('population')

# # Displaying the plot
# plt.show()

# # Data
# brands = ['Apple','Samsung','Huawei','Xiaomi','Oppo']
# market_share = [27.5,21.3,15.8,10.5,8.3]

# # Determine the index of the highest market share
# max_index = market_share.index(max(market_share))

# # Create an explode list, with a 0.1 offset for the highest market share
# explode = [0.1 if i==max_index else 0 for i in range(len(market_share))]

# # Plotting the pie chart
# plt.pie(market_share,labels=brands, autopct='%1.1f%%',explode=explode, shadow = True, startangle = 140)
# # Explode:- 0 -> slice stays in place 0.1 -> slice moves outward , higher value -> more separation
# # Adding title
# plt.title('Market Share of Smartphone Brands')

# # Displaying the plot
# plt.show()

# Data
# x = [5,15,25,35,45,55,65,75,85,95]
# y = [10,30,20,40,60,80,70,90,50,100]

# # Plotting the scatter plot
# plt.scatter(x,y,s=100)    # s Controls the size of the markers (dots)

# # Adding title and labels
# plt.title('Scatter Plot', fontsize=14)
# plt.xlabel('X values', fontsize=12)
# plt.ylabel('Y Values', fontsize=12)

# # Displaying the plot
# plt.show()

# Data
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [10,20,25,30,35,40,45,50,55,60]
# colors = ['red','blue','green','purple','orange','brown','pink','gray','olive','cyan']
# sizes = [50,100,150,200,250,300,350,400,450,500]

# # Plotting the scatter plot with custom markers
# plt.scatter(x,y,c=colors,s=sizes,marker='*')

# # Adding title and labels
# plt.title('Custom Marker Scatter Plot')
# plt.xlabel('x')
# plt.ylabel('y')

# # Displaying the plot
# plt.show()

# Data

# exams = [1,2,3,4,5]
# student1_scores = [80,85,88,90,92]
# student2_scores = [78,82,85,87,89]
# student3_scores = [75,80,82,85,88]

# # Plotting
# plt.plot(exams, student1_scores, marker='o', color='blue', label='Student 1')
# plt.plot(exams, student2_scores, marker='s', color='green', label='Student 2')
# plt.plot(exams, student3_scores, marker='^', color='red', label='Student 3')

# # Adding labels and legend
# plt.title('Performance of Students')
# plt.xlabel('Exams')
# plt.ylabel('Scores')
# plt.legend()

# # Displaying the plot
# plt.show()

# Data

quaters = ['Q1','Q2','Q3','Q4']
product1_sales = [150,200,250,300]
product2_sales = [100,150,200,250]
product3_sales = [50,100,150,200]

# Plotting 
plt.bar(quaters, product1_sales, color='red',label='Product 1')
plt.bar(quaters, product2_sales, bottom=product1_sales, color='green', label='Product 2')
plt.bar(quaters, product3_sales, bottom=[i+j for i,j in zip(product1_sales,product2_sales)], color='blue', label='Product 3')

# Adding labels and legend
plt.title('Sales of Products by Quater')
plt.xlabel('Quaters')
plt.ylabel('Sales')
plt.legend()

# Displaying the plot
plt.show()