from pygal_maps_world.maps import World
import os
#creates an instance of the worldmap class
wm = World()
#gives the worldmap class a title
wm.title = "North, Central and South America"
#uses the add method, which takes in a label and a list of country codes
wm.add("North America", ["ca", "mx", "us"])
wm.add("Central America", ["bz", "cr", "gt", "hn", "ni", "pa", "sv"])
wm.add("South America", ["ar", "bo", "br", "cl", "co", "ec", "gf,"
    "gy", "pe", "py", "sr", "uy", "ve"])
wm.render_to_file("americas.svg")
os.startfile("americas.svg")