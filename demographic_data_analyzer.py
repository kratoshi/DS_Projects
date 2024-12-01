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
nonadvanced_educated = data[-data["Education"].isin(advanced_degree)]
percentage_nonadvanced_educated = (nonadvanced_educated["Salary"] == ">50K").mean() * 100
print(percentage_nonadvanced_educated)

# minimum number of hours a person works per week
min_work_hour = data["Hours-per-week"].min()
print(min_work_hour)

# percentage of min hours worker earning more than 50K
min_hours_worker = data[data["Hours-per-week"] == min_work_hour]
percentage_of_min_worker = (min_hours_worker["Salary"] == ">50K").mean() * 100
print(percentage_of_min_worker)

# country with the highest percentage of people earning more than 50K
more_than_50k_count_per_country = data[data["Salary"] == ">50K"]["Native-Country"].value_counts()
total_per_country = data["Native-Country"].value_counts()
max_percentage = ((more_than_50k_count_per_country / total_per_country) * 100).max()
print(max_percentage)
max_percentage_country = ((more_than_50k_count_per_country / total_per_country) * 100).idxmax()
print(max_percentage_country)

# most popular occupation among those earning more than 50K in India
earning_more_than_50K_india = data[(data["Salary"] == ">50K") & (data["Native-Country"] == "India")]
most_popular_occupation = (earning_more_than_50K_india["Occupation"]).value_counts().idxmax()
print(most_popular_occupation)