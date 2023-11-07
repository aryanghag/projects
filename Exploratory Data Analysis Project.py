#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\aryan\OneDrive\Desktop\Sem 3\Diwali Sales\Diwali Sales Data.csv", encoding="unicode_escape")
df.head()


# In[3]:


df.info()


# In[5]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[6]:


df.info()


# In[7]:


pd.isnull(df).sum()


# In[8]:


df.shape


# In[9]:


#drop null values
df.dropna(inplace=True)


# In[10]:


df.shape


# In[11]:


#change data type
df['Amount'] = df['Amount'].astype('int')


# In[12]:


df.dtypes


# In[13]:


df.columns


# In[14]:


#rename column
df.rename(columns = {'Marital_Status':'Shaadi'})


# In[15]:


#describe() gives the description of the data (i.e. mean, count, std, etc)
df.describe()


# In[19]:


#using describe() on specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[24]:


a = sns.countplot(x = 'Gender', data = df)


# In[23]:


a = sns.countplot(x = 'Gender', data = df)

for bars in a.containers:
    a.bar_label(bars)


# In[30]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sales_gen


# In[33]:


sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# # Age

# In[35]:


b = sns.countplot(x = 'Age Group', data = df)

for bars in b.containers:
    b.bar_label(bars)


# In[38]:


c = sns.countplot(x = 'Age Group',hue = 'Gender', data = df)

for bars in c.containers:
    c.bar_label(bars)


# In[43]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sales_age


# In[44]:


sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# # State

# In[45]:


#total number of orders from top 10 states
df.columns


# In[47]:


sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False)
sales_state


# In[60]:


sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(7)
sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(x = 'State', y = 'Orders', data = sales_state)


# In[61]:


sales_state = df.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(7)
sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(x = 'State', y = 'Amount', data = sales_state)


# # Marital Status

# In[62]:


df.columns


# In[82]:


d = sns.countplot(x = 'Marital_Status', data = df)

sns.set(rc={'figure.figsize':(5,5)})

for bars in d.containers:
    d.bar_label(bars)


# In[83]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(x = 'Marital_Status', y = 'Amount', hue='Gender', data = sales_state)


# In[89]:


sns.set(rc={'figure.figsize':(20,10)})
e = sns.countplot(data = df, x = 'Occupation')

for bars in e.containers:
    e.bar_label(bars)


# In[92]:


sales_state = df.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x = 'Occupation', y = 'Amount', data = sales_state)


# In[93]:


df.columns


# In[96]:


sns.set(rc={'figure.figsize':(27,10)})
f = sns.countplot(data = df, x = 'Product_Category')

for bars in f.containers:
    f.bar_label(bars)


# In[99]:


sales_state = df.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(7)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_Category', y = 'Amount', data = sales_state)


# In[101]:


sales_state = df.groupby(['Product_ID'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(7)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_ID', y = 'Amount', data = sales_state)


# In[ ]:


#Married women from age group 26-35 years from Maharashtra, UP and Karnataka working in IT, Healthcare and Aviation sector are more likely to buy products from Food, Clothing and Electronics category.

