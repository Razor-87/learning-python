# 15.07.2017
car = 'Toyota'
print("car = 'Toyota'")
print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print("Is car == 'toyota'? I predict False.")
print(car == 'toyota')
print("Is car == 'toyota'? I predict True.")
print(car.lower() == 'toyota')
print("Is car != 'subaru'? I predict True.")
print(car != 'subaru')
print("Is car != 'toyota'? I predict False.")
print(car.lower() != 'toyota')

year = 2017
print('\nyear = 2017')
print("Is year == 2000? I predict False.")
print(year == 2000)
print("Is year == 2017? I predict True.")
print(year == 2017)
print("Is year != 2017? I predict True.")
print(year != 2000)
print("Is year != 2000? I predict False.")
print(year != 2017)
print("Is year > 2017? I predict True.")
print(year > 2000)
print("Is year > 2000? I predict False.")
print(year > 2018)
print("Is year >= 2017? I predict True.")
print(year >= 2000)
print("Is year >= 2017? I predict True.")
print(year >= 2017)
print("Is year < 2000? I predict False.")
print(year < 2000)
print("Is year < 2017? I predict True.")
print(year < 2018)
print("Is year <= 2000? I predict False.")
print(year <= 2000)
print("Is year <= 2017? I predict True.")
print(year <= 2017)

print("\nIs year == 2017 and != 2000? I predict True.")
print(year == 2017 and year != 2000)
print("Is year > 2010 and != 2000? I predict True.")
print(year > 2010 and year != 2000)
print("Is year < 2020 and != 2017? I predict False.")
print(year < 2020 and year != 2017)
print("Is year < 2020 and >= 2017? I predict True.")
print(year < 2020 and year >= 2017)

print("\nIs year == 2017 or != 2017? I predict True.")
print(year == 2017 or year != 2017)
print("Is year != 2016 or < 2016? I predict True.")
print(year != 2016 or year < 2016)

leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028]
print('\nLeap years:')
print(leap_years)
year = 2001
print('\nyear = 2001')
print("Is this year a leap year? I predict False.")
print(year in leap_years)
year = 2004
print('year = 2004')
print("Is this year a leap year? I predict True.")
print(year in leap_years)
year = 2005
print('year = 2005')
print("This year is not a leap year? I predict True.")
if year not in leap_years:
    print('True')
else:
    print('False')
year = 2012
print('year = 2012')
print("This year is not a leap year? I predict False.")
if year not in leap_years:
    print('True')
else:
    print('False')
