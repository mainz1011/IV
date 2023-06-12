import matplotlib.pyplot as plt
import csv
  
x = ["Classic_bike; Member", "Classic_bike; Casual", "Electric_bike; Member", "Electric_bike; Casual", "Docked_bike; Member", "Docked_bike; Casual"]
y = [0, 0, 0, 0, 0, 0]

with open('JC-202112-citibike-tripdata.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        if row[1] == "classic_bike" and row[12] == "member":
            y[0] += 1
        elif row[1] == "classic_bike" and row[12] == "casual":
            y[1] += 1
        elif row[1] == "electric_bike" and row[12] == "member":
            y[2] += 1
        elif row[1] == "electric_bike" and row[12] == "casual":
            y[3] += 1
        elif row[1] == "docked_bike" and row[12] == "member":
            y[4] += 1
        elif row[1] == "docked_bike" and row[12] == "casual":
            y[5] += 1


plt.bar(x, y, color = 'g')
plt.ylabel("Number of rides")
plt.title("The relationship between the “Rideable type” and the “Member or casual” category", fontsize = 20)
plt.show()
