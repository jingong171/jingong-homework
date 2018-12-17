from pygal_maps_world.i18n import COUNTRIES
"""Return the Pygal 2-digit country code for the given country."""
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None
