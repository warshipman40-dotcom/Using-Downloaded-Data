from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Returns the Pygal 2-digit country code for a country"""
    for code, name in COUNTRIES.items():
        #these are countries which we can't get a return of the country code
        #therefore we have to manually use an if/elif to return country code
        if name == country_name:
            return code
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Tanzania':
            return 'tz'
            #if country wasn't found, returns None
            #return None

#print(get_country_code("Andorra"))
#print(get_country_code("United Arab Emirates"))
#print(get_country_code("Canada"))