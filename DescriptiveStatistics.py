#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import pandas_profiling
from scipy import stats
 


# In[13]:


from scipy import stats


# In[14]:


import scipy


# In[15]:


df = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )


# In[13]:


df


# In[16]:


#Barchart
df['Survived'].value_counts().head(10).plot.bar()


# In[20]:


#Histogram
df[df['Fare'] < 100]['Fare'].plot.hist()


# In[24]:


import matplotlib


# In[26]:


sns.boxplot(x = 'Survived',y = 'Age',data = df)


# In[27]:


print(df.describe())


# In[28]:


print(df.info())


# In[28]:


#piechart
# import the pyplot library


import numpy as np

 
import matplotlib.pyplot as plotter


# In[31]:


plotter.pie(df['Age'].head(5), labels = {"A", "B", "C", 
                             "D", "E"}, 
                               
autopct ='% 1.1f %%', shadow = True) 
plotter.show() 


# In[25]:


#Scatterplot
# import pyplot and numpy modules

import matplotlib.pyplot as plot

import numpy as np

 



 

# Draw the scatter plot

plot.scatter(df.Age, df.Fare)

plot.title('Hypothetical:Student age group and GMAT Score')

plot.xlabel('Age')

plot.ylabel('Fare')

plot.show()


# In[32]:


# Import statistics module 
import statistics 


# In[36]:


#Harmonic Mean
print("Harmonic Mean is % s " % (statistics.harmonic_mean(df['Age'].head(5)))) 


# In[37]:


#Arithmetic Mean
print("Arithmetic Mean is % s " % (statistics.mean(df['Age'].head(5)))) 


# In[41]:


#Geometric Mean
from scipy import stats
#axis=0 argument calculates the column wise geometric mean of the dataframe so the result will be
 
scipy.stats.gmean(df.iloc[:,9:10].head(5),axis=0)


# In[43]:


#IQR
scipy.stats.iqr(df['Fare'], axis=0, interpolation='linear')


# In[ ]:




