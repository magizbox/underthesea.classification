import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
df = pd.read_excel("data/data.xlsx", encoding='sys.getfilesystemencoding()')
print("Dataset is loaded!")
rcParams['figure.figsize'] = 13, 6
df.drop("text", axis=1).sum().plot.barh()
plt.savefig("labels_distribution.png")
plt.show()
>>>>>>> origin/master
