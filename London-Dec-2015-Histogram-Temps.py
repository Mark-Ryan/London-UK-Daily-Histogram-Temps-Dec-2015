"""
This histogram example uses December 2015 daily High
and Low temperatures in London, UK.
"""

import numpy as np
import matplotlib.pyplot as plt

# store data in NumPy arrays for later use.
# (could also read data from a file using 'open' or 'np.loadtxt')

sf_high_temp = np.array([14, 14, 13, 13, 13, 14, 14, 14, 12, 12, 10, 13, 10, 10, 13, 15, 15, 14, 16, 15, 13, 15, 12, 13, 15, 15, 15, 14, 12, 14, 12])
sf_low_temp = np.array([9, 12, 12, 6, 11, 12, 11, 6, 3, 8, 5, 5, 6, 6, 10, 13, 12, 11, 13, 9, 6, 10, 8, 6, 4, 14, 11, 9, 9, 10, 5])

# set up histograms

plt.hist(sf_low_temp, bins = 10, alpha=0.4, label='Low')
plt.hist(sf_high_temp, bins = 10, alpha=0.4, label='High')

# make the graph easy to read.

plt.xlabel('Temperatures (C)')
plt.ylabel('Distrubution')
plt.title('London UK Low and High Temperatures for December 2015')

# move the legend so that it does not cover any data.

plt.legend(loc='upper left')

# make the plot.

plt.show()

