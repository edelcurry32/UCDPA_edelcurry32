import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"2019.csv")

#print (data.columns)

x = data['Country or region'].head(10)
h = data['Score'].head(10)
c = ["red", "green", "orange"]
plt.bar(x,h,width =0.5, linewidth =20, edgecolor = "red", color = "c")
plt.xlabel("Country")
plt.ylabel("Score")
plt.title("2019 Happiest Countries")
plt.show()