"""
Task 2: analyze the relationship between superstructures' materials and damage grade

* SITUATION 1: ONE MATERIALS mean damage grade
** SITUATION 1.1:ONE MATERIALS number of differnt damage grade (all)
** SITUATION 1.2:ONE MATERIALS number of differnt damage grade (PARTIAL)

* SITUATION 2: TWO MATERIALS
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

md_s = []
dn_al = pd.DataFrame()
dn_pl = pd.DataFrame()
hpt = pd.DataFrame()
data_hpt = np.array()

df = pd.read_csv('/content/drive/MyDrive/FALL22_proj/preprocessed_data.csv')

## DATA PROCESSING: extract columns contains information of superstructure
flag = df.columns.str.contains('building_id|superstructure|damage_grade')  
df = df[df.columns[flag]] 
df['materials_num'] = df.iloc[:,1:-1].sum(axis = 1)
df.rename( columns = dict(zip(df.columns,df.columns.str.replace('has_superstructure_',''))),inplace = True)


## SITUATION1: ONE MATERIALS mean damage grade
grp_sig = df.groupby(by = 'materials_num').get_group(1)

for item in grp_sig.columns[1:-2]:
    md_s.append((item,grp_sig.groupby(by=item).get_group(1).damage_grade.mean()))
md_s = pd.DataFrame(md_s)
md_s.rename(columns={0:'materials',1:'damage_grade'},inplace=True)
md_s.sort_values(by = 'damage_grade',inplace = True,ascending=False)

## SITUATION1: ONE MATERIALS number of differnt damage grade (all)
grp = grp_sig.groupby(by = 'damage_grade')

for i in range(1,6):
  temp = grp.get_group(i).iloc[:,1:-2].sum()
  temp = pd.DataFrame({'materials':temp.index,'count':temp.values},index = range(11))
  temp['damaga_grade'] = i
  dn_al = dn_al.append(temp,ignore_index=True)

## SITUATION1: ONE MATERIALS number of differnt damage grade (partial)
dn_pl = dn_al.drop(dn_al[dn_al.materials == 'mud_mortar_stone'].index)


## SITUATION2: TWO MATERIALS
grp_2 = df.groupby(by = 'materials_num').get_group(2)
grp_2['bimaterials'] = grp_2.apply(lambda x:' '.join(grp_2.columns[x.apply(lambda y:y!=0)][1:3]) ,axis=1)
grp_2 = grp_2[['bimaterials','damage_grade','materials_num']]
a = grp_2.groupby(by = 'bimaterials').damage_grade.mean()
grp_2['mean_damage'] = grp_2.apply(lambda x:a[x.bimaterials],axis = 1)
grp_2[['first','second']]=grp_2.bimaterials.str.split(' ',expand = True)

temp = grp_2.drop(['damage_grade','materials_num'],axis = 1)
temp.drop_duplicates('bimaterials',inplace = True)

a = list(temp.bimaterials)
a = [tuple(item.split(' '))for item in a]
b = list(temp.mean_damage)
dct = dict(zip(a,b))

idx = list(df.columns)[1:-2]
data_hpt = np.zeros(len(idx)*len(idx)).reshape(len(idx),len(idx))
for i in range(len(idx)):
  for j in range(len(idx)):
    if i == j:
      continue
    if (idx[i],idx[j]) in dct.keys():
      data_hpt[i][j] = dct[(idx[i],idx[j])]
    else:
      data_hpt[i][j] = dct[(idx[j],idx[i])]

hpt = pd.DataFrame(data = data_hpt, index = idx, columns= idx)
