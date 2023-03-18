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

# baseline
ax.plot(X, Y, c="gray", zorder=10)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%+.1f °C'))

# average line
plt.plot(X, [average] * 100, c='lightgray', zorder=0)
plt.text(actual_year, average + 0.05, "Hotter than the\n1880-1899 average", horizontalalignment='right',
         verticalalignment='bottom', weight='light')
plt.text(actual_year, average - 0.05, "Colder", horizontalalignment='right',
         verticalalignment='top', weight='light')
# gradient dots
norm = plt.Normalize(min_ - abs(average), max_)
ax.scatter(X, Y, c=Y, cmap='coolwarm', edgecolor="gray", norm=norm, zorder=20)

# texts
plt.text(1890, .55, "Rising Global Temperature", weight='bold', size='x-large')
plt.text(1890, .4,
         "How much cooler or warmer every year\nwas compared with the average temperature\nof the late 19th century.",
         weight='light', size='large', verticalalignment='top', zorder=10)

# annotations
for i in [15, 50, 83, len(X) - 1]:
    x, y = int(X[i]), Y[i]
    plt.text(x, y + 0.05, x, wrap=True, zorder=20, weight='bold')

for i in [4, 43, 58, 78]:
    x, y = int(X[i]), Y[i]
    plt.text(x, y - 0.1, x, zorder=20, weight='bold')

# other
plt.grid(axis='y', linestyle="dotted", c='silver')
for _, spine in ax.spines.items():
    spine.set_visible(False)
fig.set_size_inches(10, 7)
plt.show()
# plt.savefig("fig.png")
