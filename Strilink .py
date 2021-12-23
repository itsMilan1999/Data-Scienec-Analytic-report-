#!/usr/bin/env python
# coding: utf-8

# # Importing files and data

# In[1]:


import pandas as pd

df= pd.read_csv('F:/Downloads/DataSet/starlink_launches.csv' , encoding='cp1252')
df


# # Seprating year and month columns

# In[2]:


#CREATE MONTHS AND YEAR COLUMNS
df['launch_Month']=df['launch_date'].str.split(' ').str[1]
df['launch_Year']=df['launch_date'].str.split(' ').str[2]

#REPLACE DATA FOR EASY ACCESS
df['launch_outcome']=df['launch_outcome'].str.replace('Success\r\n' , 'Success')

#CREATE DATAFRAME TO STORE RESULTS 
result = pd.DataFrame()
result=df[df['launch_outcome'] == 'Success'].groupby('launch_Month').count()

df


# # Number of launch per month

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(5,5))
months = ["January", "Feb", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

Months= range(1,13)
plt.bar(Months,result['launch_outcome'].reindex(months))

plt.title("Succes ratio of lunch")
plt.ylabel('Number Of launch',fontsize=12)
plt.xlabel('Months',fontsize=12)
plt.xticks(np.arange(1,13))
plt.grid()
plt.savefig('F:\Downloads\DataSet\Starlink_Succes.png')
plt.show()


# # Total number of satellite working and launch

# In[4]:


df.columns
launch=pd.DataFrame()
working= pd.DataFrame()

plt.figure(figsize=(8,5))
#launch =df[df['satellite_working'] > 0].groupby('launch_Month').count().reindex(months)
#working=df[df['satellite_deployed'] > 0].groupby('launch_Month').count().reindex(months)
#df[df['satellite_working'] > 0].groupby('launch_Month').sum()['satellite_working'].reindex(months)
#df[df['satellite_working'] > 0].groupby('launch_Month').sum()['satellite_deployed'].reindex(months)

launch=df.groupby('launch_Month').sum()['satellite_working'].reindex(months)
working=df.groupby('launch_Month').sum()['satellite_deployed'].reindex(months)


plt.plot(months , working, 'b*-' , label='Working Satellites')
plt.plot(months , launch, 'r.--' ,label='launch Statellites')

plt.title('Total Number of Satellite',fontsize=25)
plt.xlabel('Months',fontsize=15)
plt.ylabel('Number of launch',fontsize=15)
plt.xticks(rotation=45)
plt.yticks(np.arange(0,600,50))

plt.legend()
plt.grid()
plt.savefig('F:/Downloads/DataSet/totalsatellite.png')
plt.show()


# # Avrage orbital height of satellight 

# In[23]:


df.columns
df['height']=df['orbit_inclination'].str.split('°').str[0]


# In[69]:


y= range(28,100)

plt.figure(figsize=(8,5))
plt.plot(y,df['height'])
plt.xticks(np.arange(20,100,5))

plt.title('Average Orbital Height ' , fontsize=20)
plt.ylabel('Orbital Height °/r/n', fontsize=15)
plt.xlabel('Number of Satellite',fontsize=15)
plt.savefig('F:/Downloads/DataSet/Average_OrbitalHeight.png')
plt.show()s


# # Percentage of satellite deployed per year

# In[144]:


YearData=df.groupby('launch_Year').sum()

plt.figure(figsize =(5,8))
YearData['satellite_deployed']
x=[2018,2019,2020,2021]
exp = [0.1,0.1,0.1,0.1]

plt.title('percentage of satellites deployed per year' , fontsize=20)
plt.pie(YearData['satellite_deployed'] , explode=exp ,labels=x ,autopct='%2.1f%%')
plt.savefig('F:/Downloads/DataSet/YearlyLaunch.png')
plt.show()



# In[ ]:




