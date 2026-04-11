import csv
#name of the file we will work with
filename = "sitka_weather_07-2014.csv"
#opens the file and stores it in the variable file
with open(filename) as file:
    #calls csv.reader(), which returns the next line in the object (file)
    reader = csv.reader(file)
    #csv module includes a next function()
    #this returns the next line of the file when passed the reader object
    #next is called only once so we get the first line (file headers)
    #this data is stored in header_row
    header_row = next(reader)
    print(header_row)
    #we can see that the first value in header_row is AKDT
    #that tells us that the first value in each line is the Alaska Daylight Time
    #enumerate gets the index and value of each item
    #uses tuple unpacking to store the index and values in new variables then prints them
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    