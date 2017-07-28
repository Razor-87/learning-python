# 21.07.2017
cities = {
    'moskow': {
        'country': 'russia',
        'population': 13197596,
        'fact': 'The Moscow Kremlin is the the world’s \
largest medieval fortress.',
    },
    'sydney': {
        'country': 'australia',
        'population': 5005400,
        'fact': 'It officially became a city in 1842.',
    },
    'tokio': {
        'country': 'japan',
        'population': 13617445,
        'fact': 'The Tokyo Skytree is the tallest \
free-standing tower in the world, measuring 634m.',
    },
}

for name, info in cities.items():
    print("\n" + name.title() + ":")
    country = info['country']
    population = info['population']
    fact = info['fact']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + str(population))
    print("\tFact: " + fact)
