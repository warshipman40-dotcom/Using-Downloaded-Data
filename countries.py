from pygal_maps_world.i18n import COUNTRIES
#COUNTRIES is a dictionary that contains country code as key and country name as value
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
