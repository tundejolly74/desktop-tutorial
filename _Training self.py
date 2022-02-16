#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install numpy


# In[5]:


import numpy as np
array = np.array([1,2,3,4,5,6,7])
array[1:5]


# In[7]:


random = np.random.rand(3,4)
print(random)


# In[16]:


random = np.random.randint(0, 9)
print(random)


# In[18]:


eye = np.eye(7)
eye


# In[20]:


even = np.arange(6)
print(even)


# In[21]:


array = np.arange(0,15,2)
print(array)


# In[22]:


array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b= array.reshape(4,3)
print(b)


# In[23]:


array = np.arange(0,5)
print(array)


# In[24]:


print("subtract:", array -10)


# In[25]:


print("multuply:", array * 10)


# In[26]:


print("Divide:", array/10)


# In[27]:


print("Power:", array**2)


# In[31]:


a = np.arange(1,10).reshape(3,3)
print(a)


# In[32]:


b = np.arange(10,19).reshape(3,3)
print(b)


# In[33]:


c = np.dot(a,b)
print(c)


# In[34]:


c = np.dot(a, b)
sum = np.sum(c)
print(sum)


# In[36]:


e = np.sum(c,axis=0)
e

