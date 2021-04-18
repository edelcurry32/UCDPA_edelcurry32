import pandas as pd
import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"2019.csv")

#print (data.columns)

import pandas as pd
import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"2019.csv")

#print (data.column s)

x=data['Generosity']
y=data['Score']

sns.scatterplot(x=data['Generosity'], y=data['Score'])

sns.regplot(x=data['Generosity'], y=data['Score'])

plt.show()

