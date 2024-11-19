import pandas as pd

# path definition of the dataset
file_path = "/home/kratoshi/Documents/DS Projects/data_sets/adult.data.csv"

# read dataset
data = pd.read_csv(file_path, skipinitialspace=True)

print(data.head()) # checking the structure of the dataset

print(data.columns)   # confirm the column names

# calculate the number of people per race
race_count = data["Race"].value_counts()
print(race_count)

