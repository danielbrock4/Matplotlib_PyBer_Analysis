# determine version of matplotlib
import matplotlib
matplotlib.__version__


# Include this line to make plots interactive and displayed in a Jupyter Notebook
    #Important - use "inline" instead of notebook. It has less errors when running a kernal
    #% is a magic command which behind the seens sets the backend processor used for charts. If you develop for web or apps the backend processor much match to build your application
get_ipython().run_line_magic("matplotlib", " inline")


# matplotlib needs .pyplot so you dont have to type matplotlib.pyplot everytime you code for matplotlib
    #Important - use inline instead of plt. It has less errors when running a kernal
    #"as" is the alias used to run commands from matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import statistics


#set the x-axis to a list of strings for each month
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# set the y-axis to a list of floats as teh total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


#create the plot
    # in the parentheses before the commas is the x-axis and after the commma is the y-axis
plt.plot(x_axis, y_axis)


#Create a Line Chart Using the OBJECT-ORIENTED INTERFACE
    # Method 1 - Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)


#Create a Line Chart Using the OBJECT-ORIENTED INTERFACE
    # Method2 - Create the plot with ax.plt()
fig = plt.figure()
    # to change figure-level attributes(such as axes labes, title or legend) or save the figue as an in image use fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_axis, y_axis)


#Create a Line Chart Using the OBJECT-ORIENTED INTERFACE
    # Method3 (FASTEST) - Create the plot with ax.plt()
ax = plt.axes()
ax.plot(x_axis, y_axis)


#Use plt.show()
    # the plt.show() function looks for all the active figures objects and opes a window that displays them in you have two or more data sets
        # IMPORTANT - only use plt.show() once per session because it can cause the graph to dislay improperly
    # Create the plot.
#plt.plot(x_axis, y_axis)
#plt.show()


#create the plot and add a label fo the legend
plt.plot(x_axis, y_axis, marker="*", color="midnightblue", linewidth=1.75, label="Boston")
# create labels for the x and y axis
plt.xlabel('Dates')
plt.ylabel('Fare($)')
# set y limt between 0 and 45
plt.ylim(0, 45)
# set x limt between Jan and July by using a INDEX
plt.xlim(0, 5) 
# set x limt between Jan and July by using a STRING
plt.xlim("Jan", "June")
#create a title
plt.title("Pyber Fare by Month")
# add legend
plt.legend()
# set figure seix to 20 pixles wide by 10 pixels high
plt.figure(figsize=(20, 10))
#or
# plt.subplots(figize-(20, 10))


#create line color, marker, width, & tile
     # to change figure-level attributes(such as axes labes, title or legend) or save the figue as an in image use fig = plt.figure()
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_axis, y_axis, label='Boston', color='g', marker='D', linewidth=2)
#add legend
ax.legend()
#add title and axes labels
ax.set_title('PyBer Fare by Month')
ax.set_xlabel('Dates')
ax.set_ylabel('Fares($)')
#add y-axis limit
ax.set_ylim(0, 45)
#add gridlines
ax.grid()


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


# create the plot
plt.bar(x_axis, y_axis, color="green", label='boston' )
#create labels for teh x and y axe
plt.xlabel('dates')
plt.ylabel('fare ($)')
#create title
plt.title("PyBer Fare by Month")
#add legend
plt.legend()


# Create the plot
    #To create a horizontal chart, we use the plt.barh() function [put the h behind bar]
plt.barh(x_axis, y_axis)


# Oppsite Axis Horizontal Bar Chart
    #f you want the data on opposite axes, switch the arguments in the barh() function 
plt.barh(y_axis, x_axis)


#invert the axis
    #To invert the y-axis to have the months in ascending order, use the gca() method. The gca() method means "get current axes." 
    #We can chain the gca() method to the invert_yaxis() method by using gca().invert_yaxis()
plt.barh(x_axis, y_axis)
plt.gca().invert_yaxis()


# create the plot
plt.barh(x_axis, y_axis, color="magenta", label='Boston' )
plt.gca().invert_yaxis()
#create labels for teh x and y axe
plt.xlabel('Fare ($)')
plt.ylabel('Date')
#create title
plt.title("PyBer Fare by Month")
#add legend
plt.legend()


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


# Create the plot with ax.plt()
fig = plt.figure()
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis, color="k", label="New York")


fig = plt.figure()
fig, ax = plt.subplots()
ax.barh(x_axis, y_axis, color="blue", label="New York")


# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.barh(y_axis, x_axis)


fig = plt.figure()
fig, ax = plt.subplots()
ax.barh(x_axis, y_axis, label="Chicago", color="cyan")
ax.set_title("PyBer Fare by Month")
ax.set_ylabel("Dates")
ax.set_xlabel("Fares")
ax.set_xlim(0, 45)
ax.legend()
ax.invert_yaxis()


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


#using plt.plot() function to create a scatter plot, we need to add a lowercase "o" as a parameter inside the parentheses
plt.plot(x_axis, y_axis, 'o')


#plt.scatter() function
    #plt.scatter() function, add the x-axis and y-axis parameters inside the parentheses
plt.scatter(x_axis, y_axis, c="r", label="Chicago")
plt.gca().invert_yaxis
plt.title("PyBer Fare by Month")
plt.xlabel("Fares($)")
plt.ylabel("Dates")
plt.legend()


#create a bubble chart by making a simple modification to the existing scatter plot code
plt.scatter(x_axis, y_axis, s=y_axis)


#adjust the size by multiplying the data in the y-axis by any value.
y_axis_larger = []
for data in y_axis:
    y_axis_larger.append(data*3)
    
plt.scatter(x_axis, y_axis, s=y_axis_larger)


# use LIST COMPREHENSION to replace many for and while loops
    #format
        #new_list = [expression for item in list if conditional
plt.scatter(x_axis, y_axis, s = [i * 3 for i in y_axis])


# created a scatter plot using the MATLAB approach
fig = plt.figure()
fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=y_axis) 


#Change the color of the markers to sky blue.
#Change the size of the markers to 5 times each data point.
#Make the color 20% transparent.
#Add a black edge color to the circles.
#Make the linewidth of the circles 2 points.
fig = plt.figure()
fig, ax = plt.subplots()
ax.scatter(y_axis, x_axis, s = [i * 10 for i in y_axis], marker="o", edgecolors="black", linewidth=2, c="skyblue", alpha=0.8, label="Boston")
ax.legend()
ax.set_xlabel("Fares($)")
ax.set_ylabel("Dates")
ax.set_title("Pyber Fare by Month")
ax.invert_yaxis()


# add percentages for each month and "explode" the largest percentage, which is July, the seventh value in the x_axis.
    # The "EXPLODE" parameter will offset the indicated wedge by a fraction of the radius, where "0" is zero distance from the center of the pie, and "1" is completely outside the diameter of the pie.
# add the percentage of each wedge on the pie chart
    #AUTOPACT parameter provides the format of one decimal place using .1f% 
# assign a "colors" variable to an array with the names of our 12 colors.   
explode_values = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
colors = ["slateblue", "magenta", "lightblue", "green", "yellowgreen", "greenyellow", "yellow", "orange", "gold", "indianred", "tomato", "mistyrose"]
plt.subplots(figsize=(8, 8))
plt.pie(y_axis, explode=explode_values, colors=colors, labels=x_axis, autopct='get_ipython().run_line_magic(".1f%%')", "")
plt.show()


#shadow : bool, default: False
#startangle : float, optional, default: None If not None, rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.
#counterclock : bool, optional, default: True Specify fractions direction, clockwise or counterclockwise.
fig = plt.figure()
fig, ax = plt.subplots(figsize=(8, 8))
explode_values = (0, 0, 0.2, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
ax.pie(y_axis, labels=x_axis, autopct="get_ipython().run_line_magic(".1f%%",", " explode=explode_values, shadow=True, startangle=80, counterclock=True, colors=colors)")
plt.show()


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


# Get the standard deviation of the values in the y-axis.
    #The standard deviation is a measure of the amount of variation, or spread, of a set of values from the mean.
stdev = statistics.stdev(y_axis)
stdev


# create a line chart with error bars using the MATLAB approach
    #errorbar() function = show either the standard deviation, standard error, confidence intervals, or minimum and maximum values of a dataset. 
    #When errorbar() to a chart, they can visually show the variability of the plotted data. By looking at the error bars, one can infer the significance of the data.
    #yerr paramater = adds the parameters
    #capsize= parameter =  adding a "cap" to the error bars that's equal to a scalar value
plt.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)    


#### Add Error Bars to a Line Chart Using Object-Oriented Approach
fig = plt.figure()
fig, ax = plt.subplots()
ax.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)


plt.bar(x_axis, y_axis, yerr=stdev, capsize=3)


fig, ax = plt.subplots()
ax.bar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()


#xticks() function - To adjust the major x-axis ticks on a horizontal bar chart
#use the numpy module to create an array of numbers using the arange() function. We defined the lower and upper limit of the x-axis and the increment frequency with the code: np.arange(0, 51, step=5.0)
plt.barh(x_axis, y_axis)
plt.xticks(np.arange(0, 51, step=5.0))
plt.gca().invert_yaxis()


fig, ax = plt.subplots()
ax.barh(x_axis, y_axis)
ax.set_xticks(np.arange(0, 51, step=5.0))           


# add minor ticks without numerical values between the major ticks on the x- or y-axis. Minor ticks make it even easier to estimate values for the data in the chart.

from matplotlib.ticker import MultipleLocator
# Increase the size of the plot figure.
fig = plt.figure()
fig, ax = plt.subplots(figsize=(5, 5))
ax.barh(x_axis, y_axis)
ax.set_xticks(np.arange(0, 51, step=5))

# Create minor ticks at an increment of 1.
ax.xaxis.set_minor_locator(MultipleLocator(1))



