# Description
This is a python project that also relates to data. 
This time, I've decided to do something different by using CSV  files instead of JSON files.
Most of the world information such as GDPs and populations were only downloadable as CSV files.
In this project, I was able to modularize my functions for reusability and convenience.
I also made my own get_country_name() function (imports the default dictionary from pygal_maps COUNTRIES)
However some countries were missing so I was forced to add a manaul check.
Additonally some of the entries (Arab World) aren't actually countries so I ignored them in the function.
This project was a great chance for me to use dictionaries, which I haven't used as frequently as lists.
One of the most interesting parts of my project was how wm.value() converted dictionaries into tuples.
I linked a lamba (anonymous) function to wm.value() which retrieved the country name, key piece of info, and pecrentage of world from the tuple.
Overall, the worldmap() library is a library that doesn't have very good documentation, which made it really tricky to debug.

# Exe File Download : 
https://github.com/warshipman40-dotcom/Using-Downloaded-Data/releases/tag/exe_file
Instruction : run the world_popualation.py class!

#Watch Youtube Video Here:
https://youtu.be/_p_yNmBL-cA
