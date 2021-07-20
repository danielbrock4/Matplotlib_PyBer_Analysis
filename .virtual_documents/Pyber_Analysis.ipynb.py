# Add Matplotlib inline magic command
get_ipython().run_line_magic("matplotlib", " inline")
# Dependencies and Setup
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd

# Import mpl to change the plot configurations using rcParams.
 #Matpltolib has a way to change the default parameters for charts by using the rcParams, which accesses the run and configure settings for the Matplotlib parameters.
import matplotlib as mpl
    
# Import NumPy and the stats module from SciPy.
import scipy.stats as sts


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


# measures of central tendency = refer to the tendency of data to be toward gthe middle of the dataset. The three key measures of central tednency are the mean, median, and mode.


# describe() function is a convenient tool to get a high-level summary statistics on a DataFrame or Series.
# After running the function, the output will show the count, mean, standard deviation, minimum value, 25get_ipython().run_line_magic(",", " 50%, and 75% percentiles, and maximum value from a DataFrame column that has numeric values.")

# Get summary statistics.
urban_ride_count.describe()


suburban_ride_count.describe()


rural_ride_count.describe()


# Calculate the mean of the ride count for each city type.
round(urban_ride_count.mean(),2), round(suburban_ride_count.mean(),2), round(rural_ride_count.mean(),2)


# Calculate the medium of the ride count for each city type.
round(urban_ride_count.median(),2), round(suburban_ride_count.median(),2), round(rural_ride_count.median(),2)


# Calculate the mode of the ride count for each city type.
urban_ride_count.mode(), suburban_ride_count.mode(), rural_ride_count.mode()


# Import NumPy and the stats module from SciPy.
# import numpy as np
# import scipy.stats as sts


# Calculate the measures of central tendency for the ride count for the urban cities.
mean_urban_ride_count = np.mean(urban_ride_count)
print(f"The mean for the ride counts for urban trips is {mean_urban_ride_count:.2f}.")

median_urban_ride_count = np.median(urban_ride_count)
print(f"The median for the ride counts for urban trips is {median_urban_ride_count}.")

mode_urban_ride_count = sts.mode(urban_ride_count)
print(f"The mode for the ride counts for urban trips is {mode_urban_ride_count}.")


# Calculate the measures of central tendency for the ride count for the suburban cities.
mean_suburban_ride_count = np.mean(suburban_ride_count)
print(f"The mean fo the rides counts for suburban trips is {mean_suburban_ride_count:.2f}.")

median_suburban_ride_count = np.median(suburban_ride_count)
print(f"The median for the ride counts for suburban trips is {median_suburban_ride_count}.")

mode_suburban_ride_count = sts.mode(suburban_ride_count)
print(f"The mode for the ride counts for suburban trips is {mode_suburban_ride_count}.")


# Calculate the measures of central tendency for the ride count for the rural cities.
mean_rural_ride_count = np.mean(rural_ride_count)
print(f"The mean for the ride counts for rural trips {mean_rural_ride_count:.2f}.")

median_rural_ride_count = np.median(rural_ride_count)
print(f"The median for the ride counts for rural trips is {median_rural_ride_count}.")

mode_rural_ride_count = sts.mode(rural_ride_count)
print(f"The mode for the ride counts for rural trips is {mode_rural_ride_count}.")


# Get the fares for the urban cities.
urban_fares = urban_cities_df["fare"]
urban_fares.head()


# Calculate the measures of central tendency for the average fare for the urban cities.
mean_urban_fares = np.mean(urban_fares)
median_urban_fares = np.median(urban_fares)
mode_urban_fares = sts.mode(urban_fares)


# Get the fares for the suburban cities
suburban_fares = suburban_cities_df["fare"]


# Calculate the measures of central tendency for the average fare for the suburban cities.
mean_suburban_fares = np.mean(suburban_fares)
median_suburban_fares = np.median(suburban_fares)
mode_suburban_fares = sts.mode(suburban_fares)


# Get the fares for the rural cities
rural_fares = rural_cities_df["fare"]


# Calculate the measures of central tendency for the average fare for the rural cities.
mean_rural_fares = np.mean(rural_fares)
median_rural_fares = np.median(rural_fares)
mode_rural_fares = sts.mode(rural_fares)


print("URBAN")
print(f"The mean fare price for urban trips is ${mean_urban_fares:.2f}.")
print(f"The median fare price for urban trips is ${median_urban_fares:.2f}.")
print(f"The mode fare price for urban trips is {mode_urban_fares}.")
print("SUBURBAN")
print(f"The mean fare price for suburban trips is ${mean_suburban_fares:2f}.")
print(f"The median fare price for suburban trips is ${median_suburban_fares:.2f}.")
print(f"The mode fare price for suburban trips is {mode_suburban_fares}.")
print("RURAL")
print(f"The mean fare price for rural trips is ${mean_rural_fares:.2f}.")
print(f"The median fare price for rural trips is ${median_rural_fares:.2f}.")
print(f"The mode fare price for rural trips is {mode_rural_fares}.")


# Get the driver count data from the urban cities.
urban_drivers = urban_cities_df["driver_count"]


# Calculate the measures of central tendency for the average fare for the urban cities.
mean_urban_drivers= np.mean(urban_drivers)
median_urban_drivers = np.median(urban_drivers)
mode_urban_drivers = sts.mode(urban_drivers)


# Get the driver count data from the suburban cities.
suburban_drivers = suburban_cities_df["driver_count"]


# Calculate the measures of central tendency for the average fare for the suburban cities.
mean_suburban_drivers= np.mean(suburban_drivers)
median_suburban_drivers = np.median(suburban_drivers)
mode_suburban_drivers = sts.mode(suburban_drivers)


# Get the driver count data from the rural cities.
rural_drivers = rural_cities_df["driver_count"]


# Calculate the measures of central tendency for the average fare for the rurual cities.
mean_rural_drivers= np.mean(rural_drivers)
median_rural_drivers = np.median(rural_drivers)
mode_rural_drivers = sts.mode(rural_drivers)


print("URBAN")
print(f"The mean drive count for urban trips {mean_urban_drivers:.1f}.")
print(f"The median drive count for urban trips is {median_urban_drivers}.")
print(f"The mode drive count for urban trips is {mode_urban_drivers}.")
print("SUBURBAN")
print(f"The mean drive count for suburban trips is {mean_suburban_drivers:1f}.")
print(f"The median drive count for suburban trips is {median_suburban_drivers}.")
print(f"The mode drive count for suburban trips is {mode_suburban_drivers}.")
print("RURAL")
print(f"The mean drive count for rural trips is {mean_rural_drivers:.2f}.")
print(f"The median drive count for rural trips is {median_rural_drivers}.")
print(f"The mode drive count for rural trips is {mode_rural_drivers}.")


# ax.boxplot() function takes an array inside the parentheses.

# Create a box-and-whisker plot for the urban cities ride count.x_labels = ["Urban"]
x_labels = ["Urban", "Suburban", "Rural"]
ride_count_data = [urban_ride_count, suburban_ride_count, rural_ride_count]
fig = plt.figure()
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(ride_count_data, labels=x_labels)

# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)', fontsize=20)
ax.set_ylabel('Number of Rides', fontsize=14)
ax.set_xlabel("City Types", fontsize=14)
ax.set_yticks(np.arange(0, 45, step=3.0))
ax.grid()
# Save the figure.
plt.savefig("analysis/Fig2.png")
plt.show()


# Get the city that matches 39.
urban_city_outlier = urban_ride_count[urban_ride_count==39].index[0]
print(f"{urban_city_outlier} has the highest rider count.")


# Create a box-and-whisker plot for the fare data.
x_labels = ["Urban", "Suburban", "Rural"]
fares_data = [urban_fares, suburban_fares, rural_fares]
fig = plt.figure()
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(fares_data, labels=x_labels)

# Add the title, y-axis label and grid.
ax.set_title('Ride Fare Data (2019)', fontsize=20)
ax.set_ylabel('Fare($USD)', fontsize=14)
ax.set_xlabel("City Types", fontsize=14)
ax.set_yticks(np.arange(0, 55, step=5.0))
ax.grid()

plt.savefig("analysis/Fig3")
plt.show()


# Create a box-and-whisker plot for the driver count data.
x_labels = ["Urban", "Suburban", "Rural"]
driver_count_data = [urban_driver_count, suburban_driver_count, rural_driver_count]
fig = plt.figure()
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(driver_count_data, labels=x_labels)

# Add the title, y-axis label and grid.
ax.set_title('Driver Count Data (2019)', fontsize=20)
ax.set_ylabel('Number of Drivers', fontsize=14)
ax.set_xlabel("City Types", fontsize=14)
ax.set_yticks(np.arange(0, 90, step=5.0))
ax.grid()

plt.savefig("analysis/Fig4")
plt.show()


# Get the sum of the fares for each city type.
sum_fares_by_type = pyber_data_df.groupby(["type"]).sum()["fare"]
sum_fares_by_type


# Get the sum of all the fares.
total_fares = pyber_data_df["fare"].sum()
total_fares


# Calculate the percentage of fare for each city type.
type_percents = 100 * sum_fares_by_type / total_fares
type_percents


# Calculate the percentage of fare for each city type in one cell.
type_percents = 100 * pyber_data_df.groupby(["type"]).sum()['fare'] / pyber_data_df['fare'].sum()
type_percents


# Import mpl to change the plot configurations using rcParams.
    #There is no parameter for fontsize in pie charts like there is for scatter plots. However, Matpltolib has a way to change the default parameters for charts by using the rcParams

# Build the percentage of fares by city type pie chart.
plt.subplots(figsize=(10, 6))
plt.pie(type_percents, labels=["Rural", "Suburban", "Urban"], colors=["gold", "lightskyblue", "lightcoral"], explode=[0, 0, 0.1], autopct="get_ipython().run_line_magic("1.1f%%",", " shadow=True, startangle=150)")
plt.title("% of Total Fares by City Type")
# Change the default font size from 10 to 14 using mpl.rcParams["font.size"] = .
mpl.rcParams['font.size'] = 14
# Show Figure
plt.savefig("analysis/fig5")
plt.show()


# Calculate the percentage of rides for each city type.
ride_percents = 100 * pyber_data_df.groupby(["type"]).sum()["ride_id"] / pyber_data_df['ride_id'].sum()
ride_percents


# Build percentage of rides by city type pie chart.
plt.subplots(figsize=(10, 6))
plt.pie(ride_percents,
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0, 0, 0.1],
    autopct='get_ipython().run_line_magic("1.1f%%',", "")
    shadow=True, startangle=150)
plt.title("% of Total Rides by City Type")
# Change the default font size from 10 to 14.
mpl.rcParams['font.size'] = 14
# Save Figure
plt.savefig("analysis/Fig6.png")
# Show Figure
plt.show()


# Calculate the percentage of drivers for each city type.
driver_percents = 100 * city_data_df.groupby(["type"]).sum()['driver_count'] / city_data_df["driver_count"].sum()
driver_percents


# Build percentage of rides by city type pie chart.
plt.subplots(figsize=(10, 6))
plt.pie(driver_percents, labels=["Rural", 'Suburban', "Urban"], explode=[0, 0, 0.1], colors=["gold", "lightskyblue", "lightcoral"], shadow=True, autopct='get_ipython().run_line_magic("1.1f%%',", " startangle=165)")

plt.title("% of Total Drivers by City Type")
# Change the default font size from 10 to 14.
mpl.rcParams['font.size'] = 14
#save figure
plt.savefig("analysis/Fig7.png")
#show figure
plt.show()






