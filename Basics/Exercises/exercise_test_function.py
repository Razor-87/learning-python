# 13.08.2017
def city_country(city, country, population=''):
    """Displays the city and country."""
    if population:
        population = " - population " + str(population) + "."
        city_country = city.title() + ", " + country.title() + population
    else:
        city_country = city.title() + ", " + country.title()
    return city_country
