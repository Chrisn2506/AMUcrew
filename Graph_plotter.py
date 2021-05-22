import pandas as p #Importing the library i will use to plot the graphs

data = p.read_csv('Value_file.csv', header=0, usecols=['Reading_nr', 'YValue', 'Temperature', 'Humidity%', 'Pressure']) #Creates a dataframe with all the values i want to make a graph out of.

data.plot(x = 'Reading_nr', y = 'Pressure', kind = 'scatter') #Plots the graph. Changed the y axis to get the different graphs. Scatter graph seemed like the best way to visualize the data.
