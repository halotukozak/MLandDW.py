import matplotlib.pyplot as plt

import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.ticker import FormatStrFormatter

# data generation
fig, ax = plt.subplots()
actual_year = 2020
X = np.linspace(1880, actual_year, 100)
np.random.seed(100)
delta = np.random.uniform(-0.6, 1.2, 100)
Y = 0.0001 * (X - 1880) ** 2 + delta / 2 - 1.2
max_ = max(Y)
min_ = min(Y)
average = np.average(Y[0:20])

ax.plot(X, Y, "-o")
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%+.1f °C'))

# average line
plt.plot(X, [average] * 100, c='lightgray')

# gradient
norm = plt.Normalize(min_ - abs(average), max_)
points = np.array([X, Y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap='coolwarm', norm=norm)

lc.set_array(Y)
line = ax.add_collection(lc)

plt.text(1890, .55, "Rising Global Temperature", weight='bold', size='x-large')
plt.text(1890, .4,
         "How much cooler or warmer every year\nwas compared with the average\ntemperature of the late 19th century.",
         weight='light', size='large', verticalalignment='top')
plt.text(actual_year, average + 0.05, "Hotter than the\n1880-1899 average", horizontalalignment='right',
         verticalalignment='bottom', weight='light')
plt.text(actual_year, average - 0.05, "Colder", horizontalalignment='right',
         verticalalignment='top', weight='light')

plt.grid(axis='y', linestyle="dotted", c='lightgray')

for _, spine in ax.spines.items():
    spine.set_visible(False)

fig.set_size_inches(10, 7)
plt.show()
