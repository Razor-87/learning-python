# 25.07.2017
def city_country(city, country):
    """Displays the city and country."""
    city_country = city.title() + ", " + country.title()
    return city_country


print(city_country('tokyo', 'japan'))
print(city_country('moskow', 'russia'))
print(city_country('detroit', 'united states'))
