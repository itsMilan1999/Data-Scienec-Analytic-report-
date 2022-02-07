#!/usr/bin/env python
# coding: utf-8

# # Loading necessary files

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# # DataFrame

# In[4]:


df=pd.read_csv("F:\Downloads\DataSet\Datasets\SampleSuperstore.csv")


# # Profit_Loss By city

# In[3]:


city=df['City'].drop_duplicates()
Profit=df.groupby('City').sum('Profit')['Profit']
plt.figure(figsize=(45,20))

plt.stem(city,Profit)
plt.xlabel('City',fontsize=25)
plt.ylabel('Profit',fontsize=25)

plt.title('Profit by cities',fontsize=35)
plt.yticks(np.arange(min(Profit), max(Profit)+1, 5000))
plt.xticks(rotation=90)
plt.grid()
plt.show()


# # Everage Profile  By Individual Regions

# In[237]:


ProfitWithRegion = df.groupby('Region').sum('Profit')['Profit']
Region=df['Region'].drop_duplicates()
plt.figure(figsize=(8,8))
BAR=plt.bar(Region,ProfitWithRegion)
BAR[0].set_color('r')
BAR[1].set_color('g')
BAR[2].set_color('b')


plt.title('Profit By Regions',fontsize=20,color='Red')
plt.xlabel('Region',fontsize=14)
plt.ylabel('Profit',fontsize=14)
plt.show()


# # Profits-Loss by Sates 

# In[64]:


#df.filter(["Region", "City",'Profit']).groupby('Region').head(50)
data=df.query("Region == 'South'")
Profit=data.groupby('State').sum('Profit')['Profit']
state=data.sort_values('State')['State'].drop_duplicates()


plt.plot(state, Profit , 'g*--' ,label='Profit')
plt.xticks(rotation=90)
plt.title('Profit in South Region States',fontsize=25,color='red')
plt.xlabel('States',fontsize=14)
plt.ylabel('Profit',fontsize=14)
plt.legend(loc='best')
plt.grid()
plt.show()


# In[68]:


data=df.query("Region == 'East'")
Profit=data.groupby('State').sum('Profit')['Profit']
state=data.sort_values('State')['State'].drop_duplicates()


plt.plot(state, Profit , 'g*--' ,label='Profit')
plt.xticks(rotation=90)
plt.title('Profit in East Region States',fontsize=25,color='red')
plt.xlabel('States',fontsize=14)
plt.ylabel('Profit',fontsize=14)
plt.legend(loc='best')
plt.grid()
plt.show()


# In[67]:


data=df.query("Region == 'West'")
Profit=data.groupby('State').sum('Profit')['Profit']
state=data.sort_values('State')['State'].drop_duplicates()


plt.plot(state, Profit , 'g*--' ,label='Profit')
plt.xticks(rotation=90)
plt.title('Profit in West Region States',fontsize=25,color='red')
plt.xlabel('States',fontsize=14)
plt.ylabel('Profit',fontsize=14)
plt.legend(loc='best')
plt.grid()
plt.show()


# In[238]:


data=df.query("Region == 'Central'")
Profit=data.groupby('State').sum('Profit')['Profit']
state=data.sort_values('State')['State'].drop_duplicates()


plt.plot(state, Profit , 'g*--' ,label='Profit')
plt.xticks(rotation=90)
plt.title('Profit in Central States',fontsize=25,color='red')
plt.xlabel('States',fontsize=14)
plt.ylabel('Profit',fontsize=14)
plt.legend(loc='best')
plt.grid()
plt.show()


# # Sales of individual Products

# In[5]:


Profit=df.groupby('Sub-Category').sum('Profit')['Profit']
Quantity=df.groupby('Sub-Category').sum('Profit')['Quantity']

SubCategory=df['Sub-Category'].drop_duplicates().sort_values()

plt.figure(figsize=(8,8))


plt.stem(SubCategory,Profit , label='Profit_loss')
plt.xticks(rotation=90)
plt.legend()

plt.title('Profit',fontsize=20)
plt.xlabel('Product',fontsize=14)
plt.ylabel('Income in $',fontsize=14)
plt.yticks(np.arange(-20000,65000,5000))


plt.grid()
plt.show()


# In[213]:


Sells=df.groupby('Category').sum('Profit')['Sales']
Profit=df.groupby('Category').sum('Profit')['Profit']
Category=df['Category'].drop_duplicates().sort_values()

plt.figure(figsize=(7,7))

plt.bar(Category,Sells,label='Sells')
bar=plt.bar(Category,Profit,label='Profit')

bar[0].set_hatch('/')
bar[1].set_hatch('/')
bar[2].set_hatch('/')

plt.title('Profit and Sales Ratio',fontsize=20)
plt.xlabel('Category',fontsize=14)
plt.ylabel('Income in $ ',fontsize=14)
plt.legend()
plt.show()


# In[208]:


Discount=df.groupby('Category').sum('Profit')['Discount']
Category=df['Category'].drop_duplicates().sort_values()

plt.figure(figsize=(5,5))

explode = (0, 0.1, 0)
plt.pie(Discount, explode=explode, labels=Category, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Total discount on various section',fontsize=20)
plt.show()


# In[206]:


Quantity=df.groupby('Sub-Category').sum('Profit')['Quantity']
SubCategory=df['Sub-Category'].drop_duplicates().sort_values()

plt.figure(figsize=(8,8))

plt.bar(SubCategory,Quantity)

plt.xticks(rotation=90)
plt.yticks(np.arange(0,7000,500))
plt.title('Sales of individual Products',fontsize=25)
plt.xlabel('Number of Product',fontsize=20)
plt.ylabel('Quntatity',fontsize=20)
plt.grid()
plt.show()


# In[5]:


df.groupby('Sub-Category').sum('Profit')['Profit']


# In[ ]:




