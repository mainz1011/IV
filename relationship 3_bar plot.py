import matplotlib.pyplot
import matplotlib.pyplot as plt
import csv
import datetime as dt
import time

def toUnixTime(val):
    part1 = val.split("/")
    if len(part1) == 3:
        part2 = part1[2].split(" ")
        part3 = part2[1].split(":")
        month = int(part1[0])
        day = int(part1[1])
        year = int(part2[0])
        hour = int(part3[0])
        minute = int(part3[1])
        dateTime = dt.datetime(year, month, day, hour,minute)
        return int(time.mktime(dateTime.timetuple()))


x = ["Member", "Casual"]
y = [0, 0]

memberTimes = [];
casualTimes = [];


with open('JC-202112-citibike-tripdata.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        startTimeStr = row[2]
        endTimeStr = row[3]
        startTimeUnix = toUnixTime(startTimeStr)
        endTimeUnix = toUnixTime(endTimeStr)
        if isinstance(startTimeUnix, int) and isinstance(endTimeUnix, int):
            rideTime = (endTimeUnix - startTimeUnix) / 60
            if row[12] == "member":
                memberTimes.append(rideTime)
            elif row[12] == "casual":
                casualTimes.append(rideTime)

    memberTime = 0
    casualTime = 0
    for time in memberTimes:
        memberTime += time

    for time in casualTimes:
        casualTime += time

    y[0] = memberTime / len(memberTimes)
    y[1] = casualTime / len(casualTimes)

plt.bar(x, y, color = 'orange')
plt.ylabel("Riding Time Length (in minutes)")
plt.title("The relationship between the “Riding Time Length” (in minutes) and the “Member or casual” category", fontsize = 15)
plt.show()
