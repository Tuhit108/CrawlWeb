import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('data.csv')

duoi500tr =len(df[df["Giá"]<= 500000000]) 
duoi1ty =len(df[(df["Giá"] > 500000000) & (df["Giá"]<= 1000000000)]) 
duoi1ty5 = len(df[(df["Giá"]> 1000000000) & (df["Giá"]<= 1500000000)])
duoi2ty = len(df[(df["Giá"] > 1500000000) & (df["Giá"]<= 2000000000)])
duoi2ty5 = len(df[(df["Giá"]> 2000000000) & (df["Giá"]<= 2500000000)])
duoi3ty = len(df[(df["Giá"] > 2500000000) & (df["Giá"]<= 3000000000)])
duoi3ty5 = len(df[(df["Giá"]> 3000000000) & (df["Giá"]<=3500000000)])
duoi4ty = len(df[(df["Giá"] > 3500000000) & (df["Giá"]<= 4000000000)])
duoi4ty5 = len(df[(df["Giá"]> 4000000000) & (df["Giá"]<=4500000000)])
duoi5ty = len(df[(df["Giá"] > 4500000000) & (df["Giá"]<= 5000000000)])
duoi5ty5 = len(df[(df["Giá"]> 5000000000) & (df["Giá"]<=5500000000)])
duoi6ty = len(df[(df["Giá"] > 5500000000) & (df["Giá"]<= 6000000000)])
duoi6ty5 = len(df[(df["Giá"]> 6000000000) & (df["Giá"]<=6500000000)])
duoi7ty = len(df[(df["Giá"] > 6500000000) & (df["Giá"]<= 7000000000)])
duoi7ty5 = len(df[(df["Giá"]> 7000000000) & (df["Giá"]<=7500000000)])
duoi8ty = len(df[(df["Giá"] > 7500000000) & (df["Giá"]<= 8000000000)])
duoi8ty5 = len(df[(df["Giá"]> 8000000000) & (df["Giá"]<=8500000000)])
duoi9ty = len(df[(df["Giá"] > 8500000000) & (df["Giá"]<= 9000000000)])
duoi9ty5 = len(df[(df["Giá"]> 9000000000) & (df["Giá"]<=9500000000)])
tren9ty5 =  len(df[df["Giá"]>= 9500000000])
gia = np.array([duoi500tr, duoi1ty,duoi1ty5, duoi2ty, duoi2ty5, duoi3ty, duoi3ty5,duoi4ty, duoi4ty5,duoi5ty,duoi5ty5,duoi6ty,duoi6ty5,duoi7ty,duoi7ty5,duoi8ty,duoi8ty5,duoi9ty,duoi9ty5,tren9ty5])
khoanggia=[ "0,5", "1", "1,5", "2", "2,5", "3", "3,5", "4", "4,5", "5", "5,5", "6", "6,5", "7", "7,5", "8", "8,5", "9", "9,5", "10"]

plt.bar(khoanggia, gia, color = 'blue', width = 0.5, alpha = 0.7)

plt.title('Giá xe')
plt.xlabel('Giá')
plt.ylabel('Số xe')
plt.show()

do = df['Xuất xứ'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
print(do)
ax.pie(do.values, labels = do.index,autopct='%1.2f%%')
plt.show()

do = df['Hộp số'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
print(do)
ax.pie(do.values, labels = do.index,autopct='%1.2f%%')

plt.show()
do = df['Nhiên liệu'].value_counts()
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
print(do)
ax.pie(do.values, labels = do.index,autopct='%1.2f%%')

plt.show()

do = df['Kiểu dáng'].value_counts()
fig = plt.figure()
plt.title('Kiểu dáng')
plt.bar(do.index, do.values,color='red')
plt.show()



sort = df.sort_values('Năm sản xuất')
plt.title('Kiểu dáng')
plt.xlabel('Năm')
plt.ylabel('Số lượng xe')
do = sort['Năm sản xuất'].value_counts().sort_index()
do.plot( marker = 'o')
plt.show()











