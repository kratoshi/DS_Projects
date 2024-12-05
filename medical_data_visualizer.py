import pandas as pd
import seaborn
import matplotlib.pyplot
import numpy

file_path = "/home/kratoshi/DataThings/DS_Projects/data_sets/medical_examination.csv"

df = pd.read_csv(file_path, skipinitialspace=True)

print(df.head())