#!/usr/bin/env python
# coding: utf-8



# /!\ Pour reconstituer le Jupyter Notebook, il faut copier chaque code situé 
#     après un "# In[...]:" dans une cellule différente



# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


# Reading a dataset in CSV format
df = pd.read_csv("nat2018.csv",sep=";")
# Extraction of a random subset
print(df.sample(n=5))


# In[11]:


# Extraction of lines containing "HERVÉ"
df_prenom = df[ df["preusuel"] == "Hervé".upper() ]
### or also with ".loc" which is richer in extraction possibilities
##df_prenom = df.loc[ df["preusuel"] == "HERVÉ" ]
# If you need to sort by year of birth:
df_prenom = df_prenom.sort_values(by="annais")

print(df_prenom.sample(n=5))


# In[14]:


# Display of the occurrences of the first name according to the years
df_prenom.plot(x="annais",y="nombre")
### or via Matplotlib
##plt.plot(df_prenom["annais"],df_prenom["nombre"])


# In[25]:


# Extraction of lines from the year 1967
df_an = df[ df["annais"] == "1967" ]
print(df.sample(n=5))


# In[29]:


# Concatenation of DataFrames of certain first names
df_3 = pd.concat( [
    df_an[df_an["preusuel"] == "Hervé".upper()],
    df_an[df_an["preusuel"] == "PAUL"],
    df_an[df_an["preusuel"] == "CLAUDE"]
    ])
print(df_3)


# In[30]:


# Addition of a column with the overall percentage compared to the first names of the year
df_3["%"] = df_3["nombre"] / df_an["nombre"].sum() * 100
print(df_3)


# In[36]:


# Display with the mutual proportion between the selected names
df_3.plot() # "hack" not to overwrite the last "plot"
grph = plt.pie(df_3["nombre"],
        labels=df_3["preusuel"],
        autopct='%1.1f%%',
        textprops={'fontsize':14}
        )
plt.legend().remove()
plt.show()

