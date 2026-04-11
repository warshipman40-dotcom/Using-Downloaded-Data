import csv
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
import os

#creates a dictionary
gdp_inflation = {}

filename = "GDP_DEFLATOR.csv"
with open(filename) as f:
    reader = csv.reader(f)
    #this skips the first 4 metadata lines
    for line in range(4):
        next(reader)
    #gives each possible header
    header = next(reader)
    #gets the index of the most recent data from 2024
    #while the header goes up to 2025 (the value only goes to 2024)
    recent_year_index = header.index("2024")
    for row in reader:
        #stores the country name in this variable
        country_name = row[0]
        gdp_inflation_val = row[recent_year_index]
        #print(country_name, gdp_inflation_val)
        #length of the rows is 71
        #print(len(row), row[-5:])
        #value of recent_year_index for all countries is 69
        # print(recent_year_index)
        if gdp_inflation_val != "":
            #converts to a rounded float
            gdp_inflation_val = round(float(gdp_inflation_val), 2)
            #gets the country code using this function we built
            code = get_country_code(country_name)
            #if the country has a code, store it in the dictionary along with the value of gdp inflation
            if code:
                gdp_inflation[code] = gdp_inflation_val
                
gdp_inflation_low, gdp_inflation_moderate, gdp_inflation_high = {}, {}, {}
for cc, gdp_inflation_val in gdp_inflation.items():
    if gdp_inflation_val < 2:
        gdp_inflation_low[cc] = gdp_inflation_val
    elif gdp_inflation_val < 3:
        gdp_inflation_moderate[cc] = gdp_inflation_val
    else:
        gdp_inflation_high[cc] = gdp_inflation_val

wm_style = RS("#336699", base_style = LCS)
wm = World(style = wm_style)
wm.title = "GDP inflation rate by each country (2025)"
wm.add("<2%", gdp_inflation_low)
wm.add("2%-3%", gdp_inflation_moderate)
wm.add(">4%", gdp_inflation_high)
wm.render_to_file("gdp_inflation.svg")
os.startfile("gdp_inflation.svg")