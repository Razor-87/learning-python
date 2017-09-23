# 23.09.2017
import requests
import pygal
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
names, submission_dicts = [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    names.append(response_dict['title'])
    submission_dict = {
        'value': response_dict.get('descendants', 0),
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    }
    submission_dicts.append(submission_dict)
    submission_dicts = sorted(submission_dicts, key=itemgetter('value'),
                              reverse=True)

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 16
my_style.major_label_font_size = 16

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Top 15 active discussions on Hacker News'
chart.x_labels = names[:15]

chart.add('', submission_dicts[:15])
chart.render_to_file('hn_repos.svg')
