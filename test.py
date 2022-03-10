from os import sep
import numpy as np
np.random.randn(3)
import matplotlib.pyplot as plt
plt.plot([2,3,2,1,11,3])
plt.show()

import seaborn as sns

df = sns.load_dataset('iris')
df.head(2)

plt.plot(df.sepal_length)
plt.show()