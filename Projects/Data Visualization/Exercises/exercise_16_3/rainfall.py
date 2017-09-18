# 18.09.2017
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and precipitations from file.
filename = 'san_francisco_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precipitations = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            precipitation = int(row[-5])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precipitations, c='blue', alpha=0.5)

# Format plot.
title = "Daily precipitations - 2014 (San Francisco, CA)"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.axis([dates[0], dates[-1], -1, 9])
plt.ylabel("Precipitation (in)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
