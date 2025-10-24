#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def area(r):
    print("area of circle is:", math.pi * r**2)
def peri(r):
    print("perimeter of circle is:", 2* math.pi * r)


# In[3]:


get_ipython().system('jupyter nbconvert --to python circle.ipynb')


# In[ ]:




