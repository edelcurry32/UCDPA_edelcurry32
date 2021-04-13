import pandas as pd
import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"2019.csv")

#print (data.column s)

palette = sns.color_palette("bright")
sns.palplot(palette)

fig= plt.figure(figsize=(15,8))
g=gs.GridSpec(ncols=1, nrows=2, figure=fig)
plt.suptitle("World's Happiness Index 2019", family='Calibri', weight='bold', size=16)
ax1=plt.subplot(g[0,0])


top_10=data.head(10)
bot_10= data.tail(10)
ax1=sns.barplot(data=top_10, x=top_10 ['Score'],y=top_10 ['Country or region'])
#ax1.set_xlabel('')
ax1.xaxis.set_visible(False)
ax1.annotate("Top 10 Happiest Countries",xy=(8,2), family='Calibri', weight='bold', size=9)
ax2=plt.subplot(g[1,0], sharex=ax1)
ax2=sns.barplot(data=bot_10, x=bot_10['Score'],y=bot_10 ['Country or region'])
ax2.annotate("10 Least Happiest Countries",xy=(8,2), family='Calibri', weight='bold', size=9)
for s in ['left','right','top','bottom']:
    ax1.spines[s].set_visible(False)
    ax2.spines[s].set_visible(False)

plt.show()