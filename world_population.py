#imports the JSON module
#all data sourced from worldbank official website
import json
import csv
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RCS, LightColorizedStyle as LCS
import os


def read_csv_file(filename, year):
    """Function that reads CSV files"""
    #this opens the file and stores it in f
    with open(filename) as f:
        #this creates a reader that reads the contents of the csv file
        #it returns each row as a list of strings
        reader = csv.reader(f)
        #creates a dictionary 
        dictionary = {}
        #creates a for loop that occurs 4 times (this ensures that we skip the metadata)
        for line in range(4):
            next(reader)
        #after skipping the metadata, we now can store the values of header 
        header = next(reader)
        #this stores the index of our year in the variable year_index
        #this variable can be used to find other key information of our country
        year_index = header.index(year)
        #this iterats through the various rows in the reader
        for row in reader:
            #stores country_name
            country_name = row[0]
            #stores the value of whatever e.g GDP, population
            val = row[year_index]
            #ensures the value is not an empty string
            if val != "":
                #uses int(float()) to turn a string into an int (we can't directly convert strings to int)
                val = int(float(val))
                #using a function we already created we can get the code of the country
                code = get_country_code(country_name)
                #if the code exists (strings return truthy)
                if code:
                    #we then store the country code (key) and the value of whatever (value) in the dictionary 
                    dictionary[code] = val
    #returns the dictionary so that it can be used
    return dictionary

#reminder to self CRTL + / creates multi-line comments

#stores these dictionaries in these variables
#because the function returned a dictionary and we store the value in the variable
#the variable will therefore become a dictionary
cc_populations = read_csv_file("POPULATION_DATA.csv", "2024")
cc_gdp = read_csv_file("GDP.csv", "2024")
cc_gdps_per_capita = read_csv_file("GDP_PER_CAPITA.csv", "2024")
#creates 3 empty dictionaries to store the country code and population
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
#users tuple unpacking to unpack the key (cc) and value (population)
#this will sort the populations accordingly based on their values
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#the subsequent lines will loop over the values of cc (country code) and total gdp
#using if / else conditional, they will create seperate lists which will then be used by an instance of World() and added to the world map
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp, in cc_gdp.items():
    if gdp < 1000000000000:        # under 1 trillion
        cc_gdp_1[cc] = gdp
    elif gdp < 10000000000000:     # 1T to 10T
        cc_gdp_2[cc] = gdp
    else:                          # 10T+
        cc_gdp_3[cc] = gdp

cc_gdps_per_capita_low, cc_gdps_per_capita_moderate, cc_gdps_per_capita_high = {}, {}, {}
for cc, gdp_per_capita in cc_gdps_per_capita.items():
    if gdp_per_capita < 1000:
        cc_gdps_per_capita_low[cc] = gdp_per_capita
    elif gdp_per_capita < 10000:
        cc_gdps_per_capita_moderate[cc] = gdp_per_capita
    else:
        cc_gdps_per_capita_high[cc] = gdp_per_capita


#creates an instance of worldmap
#wm = World()
#styles the worldmap using a more attractive style
#class takes an RGB color in hex format
#RotateStyle function returns a style object which gets stored in wm_style
#LightColorizedStyle will use lighter colors
wm_style = RCS("#567689", base_style = LCS)
#we pass this in as a keyword argument (keyword args order doesn't matter)
wm = World(style = wm_style)
wm2 = World(style = wm_style)
wm3 = World(style = wm_style)
#creates the title for the worldmap
wm.title = "World population in 2024 by Country"
wm2.title = "GDP per country in 2024"
wm3.title = "GDP per capita per country 2024"
#adds a label and list of countries to worldmap
#each label and country will be differently colored
wm.add("0 - 10m", cc_pops_1)
wm.add("10m - 1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)

wm2.add("<1t GDP", cc_gdp_1)
wm2.add("1t to 10t GDP", cc_gdp_2)
wm2.add(">10t GDP", cc_gdp_3)

wm3.add("<1000 USd per capita", cc_gdps_per_capita_low)
wm3.add("1000 to 10000 USD per capita", cc_gdps_per_capita_moderate)
wm3.add(">10000 USD per capita", cc_gdps_per_capita_high)
#renders the worldmap into an svg file
wm.render_to_file("world_population.svg")
wm2.render_to_file("world_gdp.svg")
wm3.render_to_file("gdp_per_capita.svg")
#automatically opens the file
os.startfile("world_population.svg")
os.startfile("world_gdp.svg")
os.startfile("gdp_per_capita.svg")



#plan for later (modulariziation?)
#find a more recent GDP list



#JSON example for personal review and reference

#with open(filename) as f:
    #then uses json.load to convert data into a format python can use
    #this is a list in our case
    #pop_data = json.load(f)

#cc_populations = {}
#for pop_dict in pop_data:
    #checks for 2010 in the "Year" key of each dictionary
    #dictionary is outdated and only includes up to 2010
    #if pop_dict["Year"] == "2010":
        #stores the relevant values in variables
        #country_name = pop_dict["Country Name"]
        #the float turns into a decimal then the int drops the decimal
        #population = int(float(pop_dict["Value"]))
        #population = "{:,}".format(population)
        #code = get_country_code(country_name)
        #if code:
            #builds a dictionary using country code as key and population as value
            #cc_populations[code] = population
            #print(code + ": " + str(population))