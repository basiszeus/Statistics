#!/usr/bin/env python
# coding: utf-8

# In[25]:


import seaborn as sns
import pandas as pd
import math


# In[19]:


P = {"Product_1" : [1.1, 1.7,2.1, 1.4, 0.2], "Product_2" : [3,4.2,4.9,4.1,2.5]}


# In[20]:


df = pd.DataFrame(data=P )
df.head()


# In[21]:


df['Product_1'].mean()


# In[22]:


df['Product_2'].mean()


# In[40]:


sns.scatterplot(data = df, x = 'Product_1', y='Product_2')


# In[2]:


P12 = [[1.1, 1.7,2.1, 1.4, 0.2], [3,4.2,4.9,4.1,2.5]]


# In[10]:


def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)


# In[11]:


def covariance(x):
    list_1 = [i[0] for i in x]
    list_2 = [i[0] for i in x]
    list_1_mean=mean(*list_1[0])
    list_2_mean=mean(*list_2[0])
    numerator = 0
    if len(list_1[0]== len(list_2[0])): # We must have the same number of elements
        for i in range(len(list_1[0])):
            numerator += (list_1[0][i] - list_1_mean)*(list_2[0][i] - list_2_mean) # xi - x mean * yi - y mean
        denominator = len(list_1[0])#If it's a sample you will write denominator = len(list_1[0])-1
        return numerator/denominator
    else:
        print("Error")


# In[24]:


covariance(P12)


# In[ ]:




