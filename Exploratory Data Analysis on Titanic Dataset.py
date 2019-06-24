#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pandas_profiling


# In[2]:


df = pd.read_csv(
       "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
   )


# In[3]:


df.profile_report()


# In[5]:


profile = df.profile_report(title="Titanic Dataset")


# In[13]:


profile.to_file(output_file="C:/Users/Admin/Desktop/titanic_report.html")

