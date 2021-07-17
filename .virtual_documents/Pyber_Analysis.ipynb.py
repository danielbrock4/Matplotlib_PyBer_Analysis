# Add Matplotlib inline magic command
get_ipython().run_line_magic("matplotlib", " inline")
# Dependencies and Setup
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd


# files to load
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"


# Read the city data file and store it in a pandas DataFrame.
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(5)


# Read the ride data file and store it in a pandas DataFrame.
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)


# Get the columns and the rows that are not null.
city_data_df.count()


# Get the columns and the rows that are not null.
city_data_df.isnull().sum()


# Get the data types of each column.
city_data_df.dtypes


# Get the unique values of the type of city.
city_data_df["type"].unique()


# Get the unique values of the type of a city.
sum(city_data_df['type'] == "Urban")


# Get the unique values of the type for all cities.
city_data_df['type'].value_counts()


# Get the columns and the rows that are not null.
ride_data_df.count()


# Get the columns and the rows that are not null.
ride_data_df.isnull().sum()


# Get the columns and the rows that are not null.
ride_data_df.dtypes


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=['city', 'city'])

# Display the DataFrame
pyber_data_df.head()



