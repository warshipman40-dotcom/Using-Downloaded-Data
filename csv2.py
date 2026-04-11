import csv
from matplotlib import pyplot as plt
from datetime import datetime
#get dates, high, and low temperatures from file
filename = "sitka_weather_07-2014.csv"
filename = "sitka_weather_2014.csv"
filename = "death_valley_2014.csv"
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    #creates empty lists for the dates and highs
    dates, highs, lows = [], [], []
    for row in reader:
        #each time we examine a row we try to extract the key info
        try:
            #converts to a datetime object
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #this gives us the first row which stores high temperature
            high = int(row[1])
            low = int(row[3])
        #if data is missing, python raises a ValueError and we print an error message
        #that includes the date of the missing data
        except ValueError:
            print(current_date, "missing data")
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
fig = plt.figure(dpi = 128, figsize = (10, 6))
#passes dates and high temperatures in the color red and passes in the list to plot()
plt.plot(dates, highs, c = "red")
#passes dates and low temperatures, plotting them with the color blue
plt.plot(dates, lows, c = "blue")
#fills the area between to show the range between the high and low temps
#takes a series of x-values and two series of y_values
#alpha controls transparency (0 is completely transparent while 1 (default) is completely opaque)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)
plt.title(title, fontsize = 24)
#modifys font size for readability
plt.xlabel("", fontsize = 16)
#this call draws labels diagonally to prevent overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)
plt.show()
