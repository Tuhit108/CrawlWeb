import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('data1.csv')
do = df['Xuất xứ'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
print(do)
ax.pie(do.values, labels = do.index,autopct='%1.2f%%')
plt.show()
