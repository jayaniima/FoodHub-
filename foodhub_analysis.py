# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Command to tell Python to actually display the graphs
%matplotlib inline

# -------------------------

# read the data (Importing data)
df = pd.read_csv('/data/foodhub_order.csv')
# returns the first 5 rows
df.head()

# -------------------------

df.shape # Checking the shape of data

# -------------------------

# Use info() to print a concise summary of the DataFrame
df.info()

# -------------------------

# Changing the data types of columns order_id and cumtomer_id
df['order_id'] = df['order_id'].astype(object)
df['customer_id'] = df['customer_id'].astype(object)

df.info()

# -------------------------


df.isnull().sum() # Checking the count of missing values in all the columns

# -------------------------


df.describe().T # Transpose of statistical summary of all numerical variables

# -------------------------

df.describe(include='all').T # Transpose of statistical summary of all the variables

# -------------------------


df['rating'].value_counts() # counting the unique values in the column 'rating'

# -------------------------


# Column 1: order_id: Unique ID of the order (non numeric)
df['order_id'].nunique()

# -------------------------

# Column 2: customer_id: ID of the customer who ordered the food (non numeric)
df['customer_id'].nunique()

# -------------------------

# Column 3: restaurant_name: Name of the restaurant (Nominal)
df['restaurant_name'].nunique()

# -------------------------

df['restaurant_name'].value_counts()

# -------------------------

# code for creating bar chart for column resaurant_name
#plt.figure(figsize = (20, 5))
#sns.countplot(x='restaurant_name', data = df)
#plt.xlabel('restaurant name')
#plt.ylabel('count')
#plt.xticks(rotation=90);



# -------------------------

# Column 4: cuisine_type: Cuisine ordered by the customer (Nominal)
df['cuisine_type'].value_counts() # Counting the popularity of all cuisines

# -------------------------

a1= df[df['cuisine_type'] == 'American'] # Identifying restaurants offering most popular cuisine
a1['restaurant_name'].value_counts()

# -------------------------

#creating bar chart for cusine_type
#plt.figure(figsize = (15,5)) #  size of the plot can be increased using this method
sns.countplot(data = df, x = 'cuisine_type') # Ploting the bar graph using countplot() function of seaborn
plt.xlabel('Cuisine Type') # labeling x axis
plt.ylabel('Count') # labeling y axis
plt.xticks(rotation= 90); # rotate the tick marks  on the x axis to make it look better and to avoid overlapping

# -------------------------

# Column 5: cost: Cost of the order (Continuous variable)
sns.histplot(data=df,x='cost_of_the_order',kde=True) # Histogram for the cost of order
plt.show()


# -------------------------

sns.boxplot(data=df,x='cost_of_the_order') # Boxplot for the cost of order
plt.show()


# -------------------------

# Column 6: day_of_the_week: Indicates whether the order is placed on a weekday or weekend (Categorical)
df['day_of_the_week'].value_counts() # checking number of occurences of unique values in the column day_of_the week


# -------------------------

ax = sns.countplot(x = 'day_of_the_week', data = df ) # Creating bar chart to visualize weekend and weekday order counts
ax.bar_label(ax.containers[0], fmt=lambda x: f'{(x/total)*100:0.1f}%') # annotate the bars with fmt from matplotlib
ax.margins(y=0.1) #add space at the end of the bar for the labels
ax.set(xlabel='Day of the week', ylabel='Order Count', title='Orders by day of the week') # Setting x, y axis labels and chart title
plt.show()

# -------------------------

# Column 7: rating: Rating given by the customer out of 5 (Categorical)
df['rating'].value_counts() # Getting counts of each unique rating value in the data set

# -------------------------

ax = sns.countplot(data=df, x = 'rating', order=['3' , '4' , '5','Not given']) # Creating a bar chart to plot count of ratings in acsending order
total = df['rating'].count() # total count of rating column
ax.bar_label(ax.containers[0], fmt=lambda x: f'{(x/total)*100:0.1f}%') # annotate the bars with fmt from matplotlib
ax.margins(y=0.1) #add space at the end of the bar for the labels
ax.set(xlabel='Rating', ylabel='Count', title='Overall Customer Ratings') # Setting x, y axis labels and chart title
plt.show()




# -------------------------

# Column 8: food_preparation_time: Time (in minutes) (Continuous variable)
sns.boxplot(data = df, x = 'food_preparation_time') # Box-plot for food preperation time
plt.xlabel('Food Preparation Time');


# -------------------------

sns.histplot(data = df, x = 'food_preparation_time', bins =10) # Histogram for food preperation time
plt.xlabel('Food Preparation Time')
plt.ylabel('Count');

# -------------------------

# Column 9: delivery_time: Time (in minutes) (Continuous variable)
sns.histplot(data = df, x= 'delivery_time')
plt.xlabel('Delivery Time')
plt.ylabel('Count');

# -------------------------

sns.boxplot(data = df, x ='delivery_time')
plt.xlabel('Delivery Time');

# -------------------------


df['restaurant_name'].value_counts()

# -------------------------


pd.crosstab(df['cuisine_type'],df['day_of_the_week']) #Method 1


# -------------------------

df_weekend = df[df['day_of_the_week'] == 'Weekend'] #Method 2
df_weekend['cuisine_type'].value_counts()

# -------------------------


sub_set = df[df['cost_of_the_order']>20] # data set having order cost greater than $20
total_set = df.shape[0] # df.shape[0] returns number of rows in df

print('Percentage of the orders cost more than $20 = ',round((sub_set.shape[0]/total_set)*100,2), '%')

# -------------------------


mean_order_delivery_time = df['delivery_time'].mean()

print('Mean order delivery time in minutes = ',round(mean_order_delivery_time,2))

# -------------------------


top_three = df['customer_id'].value_counts() # getting number of occurences of each customer id
top_three[0:3] # retreiving only first three rows

# -------------------------

import plotly.express as px

# -------------------------

#Relationship between rating  and delivery time using box plot
sns.boxplot(df, x = 'rating', y = 'delivery_time', order = ['3','4','5','Not given'])


# -------------------------

#Relationship between rating  and delivery time using scatter plot
sns.pointplot(data = df, x = 'rating', y = 'delivery_time',order = ['3','4','5','Not given'])
plt.show

# -------------------------

#POint plot of relationship between rating   and cost of order
#plt.figure(figsize = (20, 7))
sns.pointplot(df, x='rating', y ='cost_of_the_order', order = ['3','4','5','Not given']);


# -------------------------

#Box plot for the relationship in between rating and food preperation time
sns.boxplot(data=df, x='rating', y='food_preparation_time',order = ['3','4','5','Not given'])

# -------------------------

# Violin plot for the relationship in between rating and food preperation time
sns.violinplot(data=df, x='rating', y='food_preparation_time',order = ['3','4','5','Not given'])

# -------------------------

#Relationship between rating and cuisine type
rating = df[df['rating']!= 'Not given'].copy() # Creating a subset of df having records rating given
rating['rating'] = rating['rating'].astype(int) # converting the column data type to integer
rating.groupby('cuisine_type')['rating'].mean().sort_values(ascending=False) # Calculating the average rating for each cuisine type


# -------------------------

# Box Plot for relationship between cuisine type and cost of order
sns.boxplot(data=df, x='cuisine_type', y='cost_of_the_order')
plt.xticks(rotation = 75);

# -------------------------

#Box plot for relationship between cuisine type and food preparation time
sns.boxplot(df, x='cuisine_type', y='food_preparation_time')
plt.ylabel('Food Preparation Time')
plt.xlabel('Cuisine Type')
plt.xticks(rotation = 90);

# -------------------------

#Violin plot for relationship between day of the week and delivery time
sns.violinplot(data=df, x='day_of_the_week', y='delivery_time', orient='v');

# -------------------------


# Correlation among variables
sns.heatmap(data = df[['cost_of_the_order', 'food_preparation_time', 'delivery_time']].corr(), annot=True, cmap='coolwarm');

# -------------------------



rating_set = df[df['rating']!= 'Not given'].copy() # creating a subset of data without rating = 'Not given'
rating_set['rating']= rating_set['rating'].astype('int') # converting the data type of rating column to integer for future arithmatic operations

new_df1 = rating_set.groupby('restaurant_name')['rating'].count().sort_values(ascending = False)  # getting rating count grouped by resaurant name

new_df2 = rating_set.groupby('restaurant_name')['rating'].mean().sort_values(ascending = False) # getting rating mean values grouped by restaurant name

new_df3 = pd.merge(new_df1,new_df2,how='inner',on='restaurant_name') # merging two data sets to construct a new data view with restaurant name, rating count and average rating

new_df4 = new_df3[(new_df3['rating_x']>50) & (new_df3['rating_y']>4)] # Filter only restaurant names which are having rating count>50 and average rating >4
new_df4 # view result


# -------------------------


net_revenue = 0
for each in df['cost_of_the_order']:

  if each>20:
    commision = each*0.25
  elif each>5:
    commision = each*0.15
  else:
    commision = each*0

  net_revenue += commision

print("Net Revenue = ", round(net_revenue,2), 'dollars')

# -------------------------


df['total_time'] = df['food_preparation_time'] + df['delivery_time'] # calculating the total time and add that as a new column to the data set

total_greater_than_60 = df[df['total_time']>60].shape[0] # number of rows in the dataset having total time greater than 60 minutes
total_data = df.shape[0] # total number of rows in the data set
print('Percentage of orders take more than 60 minutes = ',round((total_greater_than_60/total_data )*100,2),'%')
#df.describe()

# -------------------------


df.groupby('day_of_the_week')['delivery_time'].mean()
