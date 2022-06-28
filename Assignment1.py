#!/usr/bin/env python
# coding: utf-8

# # 1. Import necessary libraries

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # 2. Print the	info()	of	the	dataframe	and	describe	your	observations.

# In[24]:


df=pd.read_csv("F:/Downloads/DataSet/WineQT.csv")
print(df.info())
print(df.max())
print(df.min())


# # 3. What	is	the	data	type	of	the	density	column?

# In[30]:


df['density'].dtype


# # 4. Check	how	many	missing	values	are	in	the	dataset per	column? Fill	missing	values using an appropriate	technique. Provide	the	codes	and	a	description	why	you	have	chosen	that	specific	method,	per	column

# In[31]:


df.isnull()
#NO null value in database 


# # 5. Create	a	simple	plot	of	the	dataframe	indicating	the	alcohol	value	per wine. Provide	the	plot	and	code

# In[65]:


y=df['alcohol']
x=df['Id']

plt.figure(figsize=(20,20))
plt.step(x,y)

plt.xlabel('Alchohol Id',fontsize=25)
plt.ylabel('Alcohol Percentage',fontsize=25)
plt.title('Alchohol Id and Percentage ',fontsize=45,color='Red')
plt.grid()
plt.show()


# # 6. Change	the	name	of	the	column	“residual	sugar”	to	“sugar” and	“citric	acid”	to	“citric_acid”. Provide	the	code	and	column	headers.

# In[67]:


df['residual sugar']
df.rename(columns = {'residual sugar':'sugar', 'citric acid':'citric_acid'})

#df.rename(columns = {'residual sugar':'sugar', 'citric acid':'citric_acid'}, inplace = True)   
#UAE ABOVE LINE OF CODE TO MAKE IN PLACE CHANGE IN DATABASE BUT I SUGGET TO ACOID INPLACE AS IT MAKE CHNGE IN DEFUALT DATABASE 


# # 7. Sort	the	rows	of	the	dataset	based	on	“quality”	and	“alcohol”	features	in	an	ascending	order. Provide	the	code	and	top	5	rows	of	the	sorted	data.

# In[72]:


data=df.sort_values(by=["quality","alcohol"],ascending = False)
data.head(5)


# # 8. Plot	the	histogram	of	the	“total	sulfur	dioxide” column.	Provide	the	code and	describe	your	observations.

# In[89]:


x=df['total sulfur dioxide']
plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('sulfur dioxide',fontsize=15)
plt.ylabel('Probability',fontsize=15)
plt.title('Histogram of total sulfur dioxide',fontsize=20,color='Red')

plt.xlim(0, 300)
plt.ylim(0, 0.03)
plt.grid(True)

plt.show()


# # 9. Scatter	plot	the “fixed	acidity”	and	“pH”	variables,	provide	the	code and	discuss	your	observations	from	a	bivariate	analysis	perspective	(including	direction,	form,	strength,	outlier).

# In[99]:


x=df['fixed acidity']
y=df['pH']

plt.figure(figsize=(8,8))
plt.scatter(x, y)

plt.xlabel('fixed acidity',fontsize=18)
plt.ylabel('PH',fontsize=18)
plt.title('Scatter plot the “fixed acidity” and “pH” variables',fontsize=20,color='Red')
plt.grid(True)

plt.show()


# In[ ]:




