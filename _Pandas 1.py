#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pandas


# In[7]:


import pandas as pd
inventory = {"Code": [475984412, 475871129, 476214584, 475854812], "Produce": ["Avocado", "Banana", "Courgette", "Cauliflower"], 
             "Origin": ["Mexico", "Costa Rica", "France", "UK"], "Price": [1.75, 0.73, 2.00, 1.80]}
#create variables
myframe = pd.DataFrame(inventory)
print(myframe)


# In[10]:


# Set the index for frameframe.index= [“AV", “BN", “CG", "CF"]
myframe = pd.DataFrame(inventory)
myframe.index = ["AV", "BN", "CG", "CF"]
print(myframe)


# In[12]:


#myframe = pd.DataFrame(inventory)
vetdata = pd.read_csv("vet_data.csv")
print(vetdata)


# In[13]:


print(vetdata["Pet_Name"])


# In[14]:


print(vetdata[["Pet_Name"]])


# In[15]:


print(vetdata[0:4])


# In[16]:


print(vetdata[8:12])


# In[17]:


print(vetdata.iloc[1])


# In[20]:


vetdata = pd.read_csv("vet_data.csv", index_col="Owner_Surname")
print(vetdata.loc[["Smith", "Sorola"]])


# In[21]:


data = pd.read_csv("vet_data.csv")
print(data.iloc[3:7,2:4])


# In[22]:


dataone = pd.read_csv("ign.csv")
print(dataone)


# In[23]:


dataone.shape


# In[24]:


dataone.head(5)


# In[25]:


dataone.tail(5)


# In[26]:


dataone.tail()


# In[27]:


dataone["platform"]


# In[29]:


type(dataone["platform"])


# In[36]:


import pandas as pd
frame = pd.DataFrame([[8.96, 1884],[7.87, 1149],[7.13, 428]],
                     index = ["Copper", "Iron", "Zinc"], columns = ["Density g/cm3", "Melting Point BC"])
frame


# In[37]:


print(frame.loc["Copper"])


# In[38]:


dataone.mean()


# In[39]:


dataone["score"].mean()


# In[40]:


dataone["score"] /2


# In[41]:


myfilter = dataone["score"] > 8
print(myfilter)


# In[43]:


highscore = dataone[myfilter]
highscore.head()


# In[44]:


dataone[(dataone.score > 8) & (dataone.platform =="iPad")]


# In[ ]:




