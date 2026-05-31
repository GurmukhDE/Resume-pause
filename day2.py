#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib as mlt


# In[3]:


df = pd.read_csv("Combined_data.csv")
df


# In[4]:


df.head()


# In[5]:


df.isnull()


# In[6]:


df.describe()


# In[14]:


df.isnull().sum()


# In[23]:


df[df['Detected State'].isnull()]


# In[8]:


type(df)


# In[9]:


df.shape


# In[17]:


df.fillna(0)


# In[21]:


df.isnull().head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




