# 19.09.2017
from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Gambia, The':
        return 'gm'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Slovak Republic':
        return 'sk'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Yemen, Rep.':
        return 'ye'

    # If the country wasn't found, return None.
    else:
        return None
