#imports the JSON module
#all data sourced from worldbank official website
import json
import csv
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RCS, LightColorizedStyle as LCS
import os
#load the data into a list
filename = "population_data.json"
#opens the file and stores it into f
with open(filename) as f:
    #then uses json.load to convert data into a format python can use
    #this is a list in our case
    pop_data = json.load(f)

filename = "gdp.csv"
with open(filename) as f:
    reader = csv.reader(f)
    cc_gdp = {}
    #this gives each possible header (always on first line for csv files)
    header = next(reader)
    year_index = header.index("2024")
    #examines each row in this file
    for row in reader:
        #country name is in first row
        country_name = row[0]
        #gets the gdp for each country in 2022
        gdp = row[year_index]
        #if the gdp is not an empty string
        if gdp != "":
            #convert the gdp to an int by first floating and then removing decimal point
            gdp = int(float(gdp))
            #store the country code using our function
            code = get_country_code(country_name)
            if code:
                #population the gdp dictionary
                cc_gdp[code] = gdp

#builds a dictionary of population data
cc_populations = {}
#print the 2024 population for each country
for pop_dict in pop_data:
    #checks for 2010 in the "Year" key of each dictionary
    if pop_dict["Year"] == "2024":
        #stores the relevant values in variables
        country_name = pop_dict["Country Name"]
        #the float turns into a decimal then the int drops the decimal
        population = int(float(pop_dict["Value"]))
        #population = "{:,}".format(population)
        code = get_country_code(country_name)
        if code:
            #buidls a dictionary using country code as key and population as value
            cc_populations[code] = population
            #print(code + ": " + str(population))

filename = "GDP_PER_CAPITA.csv"
with open(filename) as f:
    reader = csv.reader(f)
    cc_gdps_per_capita = {}
    #skip 4 lines because the first 4 lines contain metadata
    for line in range(4):
        next(reader)
    #stores the value of each header in a variable
    header = next(reader)
    #gets the index of the year 2024
    year_index = header.index("2024")
    #examines each row in the file
    for row in reader:
        #first row will contain country name
        country_name = row[0]
        gdp_per_capita = row[year_index]
        if gdp_per_capita != "":
            gdp = float(gdp_per_capita)
            code = get_country_code(country_name)
            if code:
                cc_gdps_per_capita[code] = gdp_per_capita

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
wm2.title = "Gdps for each country in 2024"
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
wm3.render_to_file("world_gdp_per_capita.svg")
#automatically opens the file
os.startfile("world_population.svg")
os.startfile("world_gdp.svg")
os.startfile("gdp_per_capita.svg")