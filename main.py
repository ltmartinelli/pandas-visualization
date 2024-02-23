import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('ice-cream-rating.csv')
df = df.set_index('Date')

df.plot(kind='line', title='Ice Cream Ratings', xlabel='Daily Ratings', ylabel='Scores')
plt.show()
