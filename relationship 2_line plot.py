import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
import csv
  
x = []
y = [0] * 31

for days in range(31):
    x.append(days + 1)

with open('JC-202112-citibike-tripdata.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        timeStr = row[2]
        timeArr = timeStr.split("/")
        if len(timeArr) == 3:
            day = int(timeArr[1])
            y[day - 1] += 1

plt.plot(x, y, color = 'g', linestyle= 'dashed', marker = 'o')
plt.xlabel("Day of December 2021")
plt.ylabel("Number of rides")
plt.xlim([1,31])
plt.title("Number of bike rides in each day of December 2021", fontsize = 20)
plt.show()
