# 18.09.2017
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, visibility, wind from file.
filename = 'tokyo.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, visibility, winds = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            vis = int(row[14])
            wind = int(row[-8])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            visibility.append(vis)
            winds.append(wind)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, visibility, c='red', alpha=0.5)
plt.plot(dates, winds, c='blue', alpha=0.5)

# Format plot.
title = "Daily visibility and wind - 2015 (Tokyo)"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.axis([dates[0], dates[-1], 1, 25])
plt.ylabel("Visibility (mi) / Wind (mph)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
