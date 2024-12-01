import pandas as pd

# path definition of the dataset
# file_path = "/home/kratoshi/Documents/DS Projects/data_sets/adult.data.csv"

file_path = "/home/kratoshi/DataThings/DS_Projects/data_sets/adult.data.csv"

# read dataset
data = pd.read_csv(file_path, skipinitialspace=True)

print(data.head()) # checking the structure of the dataset

print(data.columns)   # confirming the column names

# calculate the number of people per race
race_count = data["Race"].value_counts()
print(race_count)

# calculate the average age of men
average_age_men = data[data["Gender"] == "Male"]["Age"].mean()
print(average_age_men)

# calculate percentage of people with Bachelors Degree
percentage_of_bachelors = (data["Education"] == "Bachelors").mean() * 100
print(percentage_of_bachelors)

# percentage of people with advanced education (Bachelors, Masters, or Doctorate) that make more than 50K
advanced_degree = ["Bachelors", "Masters", "Doctorate"]
advanced_educated = data[data["Education"].isin(advanced_degree)]
percentage_advanced_degree = (advanced_educated["Salary"] == ">50K").mean() * 100
print(percentage_advanced_degree)

# percentage of people without advanced education that earn more than 50K
nonadvanced_educated = data[~data["Education"].isin(advanced_degree)]
percentage_nonadvanced_educated = (nonadvanced_educated["Salary"] == ">50K").mean() * 100
print(percentage_nonadvanced_educated)