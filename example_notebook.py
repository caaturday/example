#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Set some plotting options.
grid_style =   {     'alpha' : '0.75',
                 'linestyle' : ':' }
legend_style = {  'fontsize' : '10' }
font_syle =    {      'size' : '14' }

mpl.rc(  'font', **font_syle)
mpl.rc(  'grid', **grid_style)
mpl.rc('legend', **legend_style)


# # Example Data
# 
# Make an $xy$ data set, where
# 
# $y = \frac{\sin^2{x}}{x^2}$.

# In[12]:


x = np.linspace(-6*np.pi, 6*np.pi, 202)
y = (np.sin(x) / x)**2


# ## Plot the Data

# In[17]:


fig, ax = plt.subplots(1,1, figsize=(8,4))
ax.plot(x, y, label='sinc(x)')
ax.plot(x, np.abs(np.cos(x)), label=r'$|\cos{x}|$')
ax.set(xlabel=r'$x$',
       ylabel=r'$y = \sin^2{x}/x^2$')
ax.grid()
ax.legend()
fig.tight_layout()

# fig.savefig('sinc_function.pdf')


# In[ ]:




