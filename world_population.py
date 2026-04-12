#all data sourced from worldbank official website
import csv
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RCS, LightColorizedStyle as LCS
import os


def read_csv_file(filename, year):
    """Function that reads CSV files"""
    try:
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
            try:
                year_index = header.index(year)
            except ValueError:
                raise ValueError(f"{year} not found in {filename}")
            #this iterats through the various rows in the reader
            for row in reader:
                #stores country_name
                country_name = row[0]
                #stores the value of whatever e.g GDP, population
                val = row[year_index]
                #ensures the value is not an empty string
                if val != "":
                    try:
                    #uses int(float()) to turn a string into an int (we can't directly convert strings to int)
                        val = int(float(val))
                        #val = f"{val:,}"
                    except ValueError:
                        continue
                    #using a function we already created we can get the code of the country
                    code = get_country_code(country_name)
                    #if the code exists (strings return truthy)
                    if code:
                        #we then store the country code (key) and the value of whatever (value) in the dictionary 
                        dictionary[code] = val
        #returns the dictionary so that it can be used
        return dictionary
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

def create_dif_categories(main_dictionary, val_one, val_two):
    #defines three empty dictionaries
    dict_one, dict_two, dict_three = {}, {}, {}
    #uses tuple unpacking to get cc(key) and val(value) of the dictionary
    for cc, val in main_dictionary.items():
        #uses an if/elif/else conditional to determine where each country code and value should be placed
        #val = f"{val:,}"
        if val < val_one:
            dict_one[cc] = int(val)
        elif val < val_two:
            dict_two[cc] = int(val)
        else:
            dict_three[cc] = int(val)
    #returns all three dictionaries (tuple unpacking is necessary with 3 variables)
    return dict_one, dict_two, dict_three

def create_world_map(rgb, title, label_one, label_two, label_three, dict_one, dict_two, dict_three, filename):
    #styles the worldmap using a more attractive style
    #class takes an RGB color in hex format
    #RotateStyle function returns a style object which gets stored in wm_style
    #LightColorizedStyle will use lighter colors
    wm_style = RCS(rgb, base_style = LCS)
    #creates an instance of the worldmap class, using a keyword argument to set default style to wm_style
    wm = World(style = wm_style)
    #adds a title to the worldmap
    wm.title = title + "(Source : World Bank)"
    #adds the labels and values to the worldmap
    wm.add(label_one, dict_one)
    wm.add(label_two, dict_two)
    wm.add(label_three, dict_three)
    #what we pass into pygal is a dictionary 
    #wm.value converts each entry to a tuple like ("ca", 38,000,000)
    #x = (key, value) x[0] returns key, x[1] returns value
    #x[1] will return the second value of the typle, and wm._value_format() will format it
    #pygal converts dictionary to tuple
    wm._value_format = lambda x : "{:,}".format(x[1])
    #renders this worldmap to a file
    wm.render_to_file(filename)
    #automatically opens the file
    os.startfile(filename)
#reminder to self CRTL + / creates multi-line comments

#stores these dictionaries in these variables
#because the function returned a dictionary and we store the value in the variable
#the variable will therefore become a dictionary
cc_populations = read_csv_file("POPULATION_DATA.csv", "2024")
cc_gdp = read_csv_file("GDP.csv", "2024")
cc_gdps_per_capita = read_csv_file("GDP_PER_CAPITA.csv", "2024")
#creates 3 empty dictionaries to store the country code and population

cc_pops_1, cc_pops_2, cc_pops_3 = create_dif_categories(cc_populations, 10000000, 1000000000)
cc_gdp_1, cc_gdp_2, cc_gdp_3, = create_dif_categories(cc_gdp, 1000000000000, 10000000000000)
cc_gdps_per_capita_low, cc_gdps_per_capita_moderate, cc_gdps_per_capita_high, = create_dif_categories(cc_gdps_per_capita, 1000, 10000)

create_world_map("#567689", "World Population in 2024 by Country", "0 - 10m", "10m - 1bn", ">1bn", 
    cc_pops_1, cc_pops_2, cc_pops_3, "world_population.svg")

create_world_map("#567689", "GDP per country in 2024", "<1t GDP", "1t - 10t GDP", ">10t GDP", 
    cc_gdp_1, cc_gdp_2, cc_gdp_3, "world_gdp.svg")

create_world_map("#567879", "GDP per capita 2024", "<1000 USD per capita", "1000 - 10000 USD per capita", 
    ">10000 USD per capita", cc_gdps_per_capita_low, cc_gdps_per_capita_moderate, 
    cc_gdps_per_capita_high, "gdp_per_capita.svg")

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