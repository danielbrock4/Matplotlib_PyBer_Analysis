get_ipython().run_line_magic("matplotlib", " inline")


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd


# cvs file
pyber_ride_df = pd.read_csv("Resources/pyber_ride_data.csv")
pyber_ride_df


pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")


# Set x-axis and tick locations.
    #create an array that is the length of the DataFrame
x_axis = np.arange(len(pyber_ride_df))
tick_locations = [value for value in x_axis]
# plot the data
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.xticks(tick_locations, pyber_ride_df["Month"])


pyber_ride_df.plot.bar(x="Month", y="Avg. Fare ($USD)")
plt.show()


#  other approach is to add the kind parameter to the plot() function.
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)", kind='bar')
plt.show()


stdev = statistics.stdev(pyber_ride_df["Avg. Fare ($USD)"])
x_axis = np.arange(len(pyber_ride_df["Month"]))
ticklocations = [value for value in x_axis]
pyber_ride_df.plot.bar(x="Month", y="Avg. Fare ($USD)", yerr=stdev, capsize=3, color="skyblue")
plt.xticks(tick_locations, pyber_ride_df["Month"], rotation = 0)



