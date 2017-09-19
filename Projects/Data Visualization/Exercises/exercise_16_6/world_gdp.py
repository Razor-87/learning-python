# 19.09.2017
import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# Load the data into a list.
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2016-09-18':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

# See how many countries are in each level.
print(len(cc_gdp))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World Gross Domestic Product in 2016, by Country'
wm.add('GDP', cc_gdp)

wm.render_to_file('world_gdp.svg')
