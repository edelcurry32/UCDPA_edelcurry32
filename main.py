import pandas as pd
import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_2019 = pd.read_csv(r"2019.csv")
data_2018 = pd.read_csv(r"2018.csv")
concat_data= pd.concat([data_2019, data_2018])

left = data_2019.set_index(['Country or region', 'Score'])

right = data_2018.set_index(['Country or region', 'Score'])

join_data = left.join(right, lsuffix='_2019', rsuffix='_2018')

#print (data.columns)
plt.show()

