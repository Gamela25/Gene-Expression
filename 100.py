#بسم الله الرحمن الرحيم
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path='C:\\Users\\hp\\OneDrive\\Desktop\\gene expression data\\100.txt'

data=pd.read_csv(path,header=None,names=['COL5A1','TNC',
                                         'category'])

print('data=\n',data.head(10))
print('***************************************')
print('data.describe=\n',data.describe())

positive=data[data['category'].isin([1])]
negative=data[data['category'].isin([0])]

print("patient\n",positive)
print("health\n",negative)


fig,ax=plt.subplots(figsize=(8,5))

ax.scatter(negative['COL5A1'],negative['TNC'],
           s=60,c='b',marker='o',label='category')


ax.scatter(positive['COL5A1'],positive['TNC'],
           s=60,c='r',marker='x',label='category')
ax.legend()
ax.set_xlabel('COL5A1')  
ax.set_ylabel('TNC') 


def sigmoid(z):
    return 1/(1+np.exp(-z))

nums=np.arange(-10,10,step=1)
fig,ax=plt.subplots(figsize=(8,5))
ax.plot(nums,sigmoid(nums),'r')


data.insert(0,'ones',1)
#print(data)




