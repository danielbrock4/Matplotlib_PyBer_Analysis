# Add Matplotlib inline magic command
get_ipython().run_line_magic("matplotlib", " inline")
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


#print(pyber_data_df['type'].value_counts())


#  1. Get the total rides for each city type
total_rides = pyber_data_df.groupby(['type']).count()['ride_id']
total_rides


# 2. Get the total drivers for each city type
total_drivers = city_data_df.groupby(['type']).sum()['driver_count']
total_drivers


#  3. Get the total amount of fares for each city type
total_fares = pyber_data_df.groupby(['type']).sum()['fare']
total_fares


#  4. Get the average fare per ride for each city type. 
avg_fare_per_ride = total_fares / total_rides
avg_fare_per_ride 


# 5. Get the average fare per driver for each city type. 
avg_fare_per_driver = total_fares / total_drivers
avg_fare_per_driver


#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
    "Total Rides": total_rides,
    "Total Driver": total_drivers,
    "Total Fares": total_fares,
    "Average Fare per Ride": avg_fare_per_ride,
    "Average Fare per Driver": avg_fare_per_driver
})


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None


#  8. Format the columns.
pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:.2f}".format)
pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:.2f}".format)
pyber_summary_df


# 1. Read the merged DataFrame
pyber_data_df.head()


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
daily_fares_df = pyber_data_df.groupby(['date', 'type']).sum()[['fare']]
# daily_fares_df


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
daily_fares_df = daily_fares_df.reset_index()
# daily_fares_df


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
daily_fares_pivot = daily_fares_df.pivot(index='date', columns='type', values='fare')
# daily_fares_pivot


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
daily_fares_jan_apr19 = daily_fares_pivot.loc['2019-01-01':"2019-04-29"] 
daily_fares_jan_apr19.tail(3)


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
daily_fares_jan_apr19.index = pd.to_datetime(daily_fares_jan_apr19.index)
# daily_fares_jan_apr19


# 7. Check that the datatype for the index is datetime using df.info()
daily_fares_jan_apr19.info()


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
weekly_fares_df = daily_fares_jan_apr19.resample("W").sum()
weekly_fares_df.head()


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

fig = plt.figure()
ax = weekly_fares_df.plot(figsize=(20, 6))
ax.set_title("Total Fare by City Type", fontsize=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Fares($USD)", fontsize=12)

lgnd = plt.legend(fontsize=12, loc="best", title="City Type")
lgnd.get_title().set_fontsize(12)

plt.savefig("analysis/Fig8.png")



