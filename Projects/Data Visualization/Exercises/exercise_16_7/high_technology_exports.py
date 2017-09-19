# 19.09.2017
import csv

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# Load the data into a list.
filename = 'hte.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Build a dictionary of HTE data.
    hte_dic = {}
    for row in reader:
        country_name = row[0]
        if row[-3].isdigit():
            hte = int(row[-3])
            code = get_country_code(country_name)
            hte_dic[code] = int(hte)
        else:
            print(country_name, 'missing data')

# See how many countries are in each level.
print(len(hte_dic))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World High-technology exports in 2014, by Country'
wm.add('HTE', hte_dic)

wm.render_to_file('world_hte.svg')
