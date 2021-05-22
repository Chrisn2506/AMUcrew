import pandas as p

data = p.read_csv('Value_file.csv', header=0, usecols=['Reading_nr', 'YValue', 'Temperature', 'Humidity%', 'Pressure'])

data.plot(x = 'Reading_nr', y = 'Pressure', kind = 'scatter')