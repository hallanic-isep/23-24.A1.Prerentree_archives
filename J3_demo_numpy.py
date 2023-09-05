#!/usr/bin/env python
# coding: utf-8



# /!\ Pour reconstituer le Jupyter Notebook, il faut copier chaque code situé 
#     après un "# In[...]:" dans une cellule différente



# Chargement des bibliothèques Python utilisées dans cette page

# In[1]:


import math
import numpy as np
from scipy import special
import matplotlib.pyplot as plt


# Modes d'affichage :
# * V1 - dans la page

# In[9]:


#get_ipython().run_line_magic('matplotlib', 'inline')


# * V2 - dans une fenêtre interactive (zoom, rotation...)

# In[11]:


get_ipython().run_line_magic('matplotlib', 'qt')


# Code de la fonction mathématique visualisée (fonction de Bessel)

# In[2]:


def bessel(n, k, distance, angle, t):
   kth_zero = special.jn_zeros(n, k)[-1]
   return np.cos(t) * np.cos(n*angle) * special.jv(n, distance*kth_zero)


# ### Coordonnées polaires de 5 * 10 points autour de l'origine

# 5 points répartis entre 0 et 1

# In[3]:


radius = np.linspace(0, 1, 5, endpoint=True)
print("radius", radius)


# 10 angles répartis entre 0 et 2*PI

# In[4]:


theta = np.linspace(0, 2*np.pi, 10, endpoint=True)
print("theta", theta)


# ### Calcul des coordonnées (x,y) correspondantes
# pour chaque groupes de 5 points répartis sur les 10 angles

# **Les x sont calculés de manière classique**

# In[5]:


lst_x = []
for r in radius:
    lst_cos = []
    for a in theta:
        lst_cos.append( r * math.cos(a) )
    lst_x.append(lst_cos)
x = np.array(lst_x)
print("x -------")
print(x)


# **Les y sont calculés en tirant avantage de numpy et de la "list comprehention"**
# * "numpy", contrairement à "math", peut calculer le sinus sur tous les éléments d'une matrice en un seul appel
# * la "list comprehention" est une syntaxe où les élément de la liste sont générés par un "for"

# In[6]:


y = np.array([r * np.sin(theta) for r in radius])
print("y -------")
print(y)


# ### V1 - Tous les z sont à zéro

# In[7]:


z = np.zeros( (len(radius), len(theta)) )
print("z -------")
print(z)


# ### V2 - Appel de la fonction de Bessel

# In[13]:


#z = np.array([bessel(1, 1, r, theta, 0.5) for r in radius])
#print("z -------")
#print(z)


# ### Dessin de la surface 3D correcpondante

# In[14]:


fig = plt.figure()
ax = fig.add_axes(rect=(0, 0.05, 0.95, 0.95), projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, vmin=-0.5, vmax=0.5)
# Avec une palette différente...
#ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='RdBu_r', vmin=-0.5, vmax=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xticks(np.arange(-1, 1.1, 0.5))
ax.set_yticks(np.arange(-1, 1.1, 0.5))
ax.set_zlabel('Z')
plt.show()

