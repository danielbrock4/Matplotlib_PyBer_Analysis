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


## Create a Bubble Chart for Ride-Sharing Data


# Create the Urban city DataFrame
urban_cities_df = pyber_data_df[pyber_data_df["type"] == "Urban"]
urban_cities_df.head()


# Create the Suburban and Rural city DataFrames.
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]
rural_cities_df = pyber_data_df[pyber_data_df["type"] == "Rural"]


#get the Number of Rides for Each City Type
urban_ride_count = urban_cities_df.groupby(["city"]).count()["ride_id"]
urban_ride_count.head()


# Create the suburban and rural ride count.
suburban_ride_count = suburban_cities_df.groupby('city').count()["ride_id"]
rural_ride_count = rural_cities_df.groupby('city').count()["ride_id"]


# Get average fare for each city in the urban cities.
urban_avg_fare = urban_cities_df.groupby(["city"]).mean()["fare"]
urban_avg_fare.head()


# Get average fare for each city in the suburban and rural cities.
suburban_avg_fare = suburban_cities_df.groupby('city').mean()['fare']
rural_avg_fare = rural_cities_df.groupby('city').mean()['fare']


# Get the average number of drivers for each urban city.
urban_driver_count = urban_cities_df.groupby(['city']).mean()['driver_count']
urban_driver_count.head()


# Get the average number of drivers for each city for the suburban and rural cities.
suburban_driver_count = suburban_cities_df.groupby(['city']).mean()['driver_count']
rural_driver_count = rural_cities_df.groupby(['city']).mean()['driver_count']


# Build the scatter plots for urban cities.
plt.scatter(urban_ride_count, urban_avg_fare, s=urban_driver_count*10, label="Urban", alpha=.80, edgecolors='k', linewidths=1, c="coral")
plt.title('PyBer Ride-Sharing Data (2019)')
plt.ylabel('Average Fare ($)')
plt.xlabel('Total Number of Rides (Per City)')
plt.grid()
# add legend
plt.legend()


# Build the scatter plots for suburban cities.
plt.scatter(suburban_ride_count,
      suburban_avg_fare,
      s=10*suburban_driver_count, c="skyblue",
      edgecolor="black", linewidths=1,
      alpha=0.8, label="Suburban")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
# Add the legend.
plt.legend()


# Build the scatter plots for suburban cities.
plt.scatter(rural_ride_count,
      rural_avg_fare,
      s=10*rural_driver_count, c="gold",
      edgecolor="black", linewidths=1,
      alpha=0.8, label="Rural")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
# Add the legend.
plt.legend()





#To create a bubble chart that showcases all the different city types in one chart, we'll combine our three scatter plot code blocks in one Jupyter

# Add the scatter charts for each type of city.
plt.subplots(figsize=(10, 6))
plt.scatter(urban_ride_count,
      urban_avg_fare,
      s=10*urban_driver_count, c="coral",
      edgecolor="black", linewidths=1,
      alpha=0.8, label="Urban")

plt.scatter(suburban_ride_count,
      suburban_avg_fare,
      s=10*suburban_driver_count, c="skyblue",
      edgecolor="black", linewidths=1,
      alpha=0.8, label="Suburban")

plt.scatter(rural_ride_count,
      rural_avg_fare,
      s=10*rural_driver_count, c="gold",
      edgecolor="black", linewidths=1,
      alpha=0.8, label="Rural")

# Incorporate the other graph properties
plt.title("PyBer Ride-Sharing Data (2019)", fontsize=20)
plt.ylabel("Average Fare ($)", fontsize=12)
plt.xlabel("Total Number of Rides (Per City)", fontsize=12)
plt.grid(True)

# Create a legend
# declare a variable for the legend function, lgnd = plt.legend(), and add parameters for font size, legend location, and legend title, along with some other features.
    # legendHandles[]._sizes to set the font size of the marker in the legend to a fixed size
    # expanded the legend horizontally using mode= to fit the area
    # location setting, loc=, for the legend is where it will fit the "best" based on the plotting of the data points.
lgnd = plt.legend(fontsize=12, mode="Expanded", scatterpoints=1, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]
lgnd.get_title().set_fontsize(12)

# Incorporate a text label about circle size
    #plt.text() add text to chart. Inside the function, we add the x and y coordinates for the chart and the text in quotes.
    #The x and y coordinates are based on the chart coordinates. Our x position can be 42, and the y position can be in the middle, 32–35.
plt.text(42, 35, "Note: Circle size correlates with driver count per city.", fontsize="12")

# Save the figure.
    #plt.savefig()= saves chart into a folder
plt.savefig("Analysis/Fig1.png")

# Show the plot
plt.show()



