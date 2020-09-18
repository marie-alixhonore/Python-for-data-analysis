#!/usr/bin/env python
# coding: utf-8

# # Python for Data Analysis : TD 1

# In[1]:


print("Hello World !")


# In[4]:


get_ipython().run_line_magic('autosave', '60')


# In[2]:


b=1.1
type(b)


# In[3]:


print(b+2)
type(b+2)


# ## Type casting

# In[6]:


c=int("1")
print(c+2)
type(c+2)


# ## Listes

# In[8]:


une_liste = [1, 2, "a", "b"]
une_liste


# In[11]:


#une liste commence à l'indice 0
une_liste[1]


# In[12]:


#dernier élément de la liste
une_liste[-1]


# In[13]:


une_liste.append("z")


# In[14]:


une_liste


# ## List slicing

# In[16]:


#une_liste[a:b] -> va de l'indice a compris à l'indice b exclu
une_liste[2:4]


# In[17]:


une_liste[-2:]


# In[18]:


une_liste[:-2]


# ## Pandas/Matplotlib

# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


# In[74]:


#chargement dataset
prenoms = pd.read_csv("dpt2018.csv", sep=";")


# In[27]:


prenoms


# ## Analyse rapide de la structure

# In[28]:


prenoms.head()


# In[30]:


prenoms.tail()


# In[35]:


nb_lignes, nb_col=prenoms.shape
print(nb_lignes)
print(nb_col)


# In[32]:


prenoms.describe()


# In[34]:


prenoms.dtypes


# In[36]:


prenoms.columns


# ## Exercice 1
Les prénoms rares sont-ils majoritairement masculins ou féminins ?
Quel département regroupe le plus de prénoms rares ? 
Le nombre total de naissance par année ?


Afficher le nombre de prénoms rares par département 
Afficher le nombre de prénoms rares par année de naissance
Afficher le nombre de naissance par année
Afficher la proportion des naissances de femmes par année
# In[37]:


prenoms.count()


# ## Filtrer 

# In[38]:


prenoms[prenoms.preusuel=="GERMAIN"]


# In[39]:


prenoms[prenoms.preusuel=="GERMAIN"].count()


# In[42]:


prenoms[prenoms.dpt=="XX"]


# In[43]:


prenoms[prenoms.dpt=="XX"].count()


# In[44]:


prenoms[prenoms.dpt!="XX"].count()


# ## Sélectionner une colonne

# In[45]:


prenoms["sexe"]


# In[46]:


prenoms[prenoms.preusuel=="GERMAIN"]["sexe"]


# In[52]:


#Classé par ordre croissant 
prenoms[prenoms["nombre"]>3000].sort_values(by="nombre")


# In[53]:


#classé par ordre décroissant
prenoms[prenoms["nombre"]>3000].sort_values(by="nombre", ascending= False)


# In[58]:


#FILTER, SORT and SLICE
prenoms[prenoms.preusuel=="GERMAIN"].sort_values(by="annais")[10:]


# In[59]:


#GROUP BY
prenoms.groupby("sexe").nombre.sum()


# In[61]:


prenoms.groupby("dpt").nombre.sum().sort_values()[-20:]


# In[65]:


#Top given name
prenoms.groupby("preusuel").nombre.sum().sort_values()[-20:]


# In[63]:


prenoms.groupby("preusuel").nombre.sum().sort_values()[:20]


# ## Nettoyage des données

# In[67]:


prenoms.count()


# In[75]:


prenoms=prenoms[(prenoms.dpt!="XX")]
prenoms.count()


# In[ ]:





# In[76]:


prenoms[(prenoms.preusuel=="PAUL")].groupby(prenoms.annais).nombre.sum().plot()


# In[77]:


total_naissances=prenoms.pivot_table('nombre', index='annais', columns='sexe', aggfunc=sum)


# In[78]:


total_naissances


# ## Exercice 2

# In[88]:


#chargement dataset
#https://www.data.gouv.fr/fr/datasets/depenses-d-assurance-maladie-hors-prestations-hospitalieres-donnees-nationales/#_
dep_maladie= pd.read_csv("C:\\Users\\Honoré Marie-Alix\\Documents\\2 ESILV\\A5\\Python for data analysis\\TD1\\N201912.csv", sep=';', encoding ="ANSI")


# In[89]:


dep_maladie


# In[93]:


nb_ligne, nb_col = dep_maladie.shape
print(nb_ligne)
print(nb_col)


# In[95]:


dep_maladie.describe()


# ## Combien de personnes ont-elles été remboursées à 100% pour un acte de santé ?

# In[98]:


dep_maladie["REM_TAU"]


# In[103]:


dep_maladie[dep_maladie["REM_TAU"]==100].count


# In[111]:


dep_maladie.groupby("REM_TAU").count()[-1:].l_serie


# In[201]:


#proportion
proportion = dep_maladie.groupby("REM_TAU").count()[-1:].l_serie/nb_ligne *100
proportion


# In[202]:


# 120 173 personnes ont été remboursées à 100% durant cette période
# Cela représente 53.05% des remboursements sur cette période


# ## Histogramme du nombre de consultations par spécialité

# In[124]:


nb_nature = dep_maladie.groupby("l_pre_spe").count().l_serie
print(nb_nature)


# In[145]:


type(nb_nature)


# In[146]:


nb_cons_nature=nb_nature.values
nb_cons_nature


# In[217]:


import numpy as np
#problème axe abscisse
plt.figure(figsize=(12,10), dpi=80)
plt.bar(nb_nature.index, nb_cons_nature)
xticks_pos = np.arange( len( nb_nature.index)) +1
plt.xticks(xticks_pos ,nb_nature.index, rotation=45 )
plt.xlabel('spécialités')
plt.ylabel('nombre de consultation')
plt.title('Diagramme bar du nombre de consultations par spécialité')


# ## nombre de remboursements par date

# In[162]:


import datetime
dep_maladie["rem_date"]= 
df['Datetime'] = df['Datetime'].apply(lambda _: datetime.strptime(_,"%m/%d/%Y, %H:%M:%S"))


# In[157]:


dep_maladie["rem_date"]


# In[160]:


type(dep_maladie["rem_date"])


# In[188]:


dep_maladie["rem_date"] = pd.to_datetime(dep_maladie["rem_date"], format= '%Y%m')


# In[193]:


dep_maladie["rem_date"]


# In[196]:


dep_maladie.groupby(dep_maladie["rem_date"]).sum().plot()


# In[199]:


# Pas très révélant ici, 
# mais pratique pour comparer le nombre de remboursements avec les autres périodes 
# qui sont dans les autres fichiers


# ### Corrélation & Heatmap

# In[178]:


corr = dep_maladie.corr()
corr


# In[180]:


import seaborn as sb


# In[182]:


ax = sb.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sb.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);


# ### Pivot table

# In[175]:


table = pd.pivot_table(dep_maladie, values='l_asu_nat', index=['rem_mon', 'dep_mon'],

                    columns=['l_exe_spe'], aggfunc=np.sum)
print(table)


# ### Lorsqu'il y a un remboursement quel est-il en moyenne ?

# In[220]:


type(dep_maladie["rem_mon"][1])


# In[244]:


#conversion des remboursements en float
dep_maladie["rem_mon"] = dep_maladie["rem_mon"].apply(lambda x : x.replace('.', '').replace(',','.')).astype(float)


# In[245]:


type(dep_maladie["rem_mon"][1])
dep_maladie["rem_mon"][1]


# In[247]:


#problème plusieurs remboursements pour plusieurs actes sur même ligne
dep_maladie.groupby("l_exe_spe")["rem_mon"].mean()


# In[263]:


dep_maladie["moy_rem"] = dep_maladie["rem_mon"]/dep_maladie["act_dnb"].astype(float)
dep_maladie2 = dep_maladie


# In[264]:


dep_maladie2["moy_rem"]


# In[265]:


dep_maladie2.fillna(1)


# In[266]:


dep_maladie2["moy_rem"]


# In[267]:


dep_maladie2.groupby("l_exe_spe")["moy_rem"].mean()


# ### Quelle est la spécialité qui a fait le plus de consultations remboursées ?

# In[268]:


dep_maladie.groupby("l_exe_spe")["act_dnb"].sum()


# In[269]:


# Comme attendu, c'est en médecine générale qu'il y a le plus de consultations,
# 30 fois plus qu'en Anesthésiologie

