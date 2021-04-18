import pandas as pd
import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"2019.csv")

#print (data.columns)

seq_list = [1,2,3,4,5]
print(list(reversed(seq_list)))

x = data['Country or region'].head(10)
h = data['Score'].head(10)
c = ["blue"]
plt.bar(x,h,width =0.6, linewidth =20, edgecolor = "yellow", color = "blue")
plt.xlabel("Country")
plt.ylabel("Score")
plt.title("2019 Happiest Countries")
plt.show()


