#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


install numpy as np


# In[3]:


install pip


# In[4]:


import sys
get_ipython().system('{sys.executable} -m pip install numpy')


# In[5]:


pip install notebook


# In[7]:


import numpy as np
a=np.array([3,4,5,6,2])
b=np.array([6,2,1,5,0])
print(a*b)


# In[14]:


b=np.array([[3,9,2,4,6],[10,11,23,8,5]])
b.shape


# In[16]:


# get tpye
b.dtype


# In[17]:


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a


# In[24]:


a[0,1:6:2]


# In[35]:


np.zeros((2,3))


# In[36]:


np.ones((2,5))


# In[38]:


np.random.rand(4,2)


# In[39]:


np.identity(5)


# In[40]:


np.identity(8)


# In[45]:


a =np.array([1,2,3])
b = a.copy()
b[0]=100
print(a)


# In[41]:


arr=np.array([[1,2,3]])
r1=np.repeat(arr,3, axis=0)
print(r1)


# In[46]:


stats = np.array([[1,2,3],[4,5,6]])
stats


# In[47]:


np.min(stats)


# In[49]:


np.max(stats,axis=1)


# In[51]:


x= np.array([3,6,7,9,10])
y= np.array([2,4,5,9,13])
np.vstack([x,y,x])


# In[ ]:


np.genfromtxt('biggs.txt', delimiter =',')

