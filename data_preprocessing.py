# -*- coding: utf-8 -*-
"""data preprocessing 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15sSfKj5lC8vA6u2OdeFBVhYyr0qdAr5J

# Data Preprocessing for the Original File 

Files needed:  csv_building_ownership_and_use.csv; csv_building_structure.csv; train_values.csv. 
Previous two files downloaded from the official website https://www.npc.gov.np/en, contain different features; the third datafile is a preprocessed version provided by https://www.drivendata.org/competitions/57/nepal-earthquake/page/136/. 

We are unsatisfied with the truncated version provided by the drivendata website as it removes data rows with damage grade (the output feature) greater than 3, which causes a lost of about 40,000 rows of data. Also, the drivendata use some random letters to represents the categorical data, which obfuscate the true meaning of the categorical features. For example, a building has land_surface_condition drawn from {'n', 'o', 't'}, while in the original data file it is reprented by {'Flat','Steep slope', 'Moderate slope'}. 

In the meanwhile, we want to preprocessed the original file so that its column names are unified with that of the drivendata website. Also, the original file's damage grade is represented by text rather than number (e.g., "grade 3" rather than 3). We would like to have a simple number representing the damage grade instead of the clumsy text message.

The following preprocessing steps are taken.

Step 1. Merge the 2 original datasets into one dataset with complete features.

Step 2. Remove rows with null entries

Step 3. Unify the features names with the truncated dataset from the drivedata website.

Step 4. Convert the data type of "damage_grade" from text object to integer type.

Step 5. Remove unwanted columns (columns that do not exist in the data file from the drivendata weibsite)
"""

from google.colab import drive
drive.mount('/content/drive')

import sys
import pandas as pd
import csv

"""#Step 1. Join the two datafiles  """

input_file1 = '/content/drive/MyDrive/earthquake/csv_building_structure.csv'  
input_file2 = '/content/drive/MyDrive/earthquake/csv_building_ownership_and_use.csv'
df1 = pd.read_csv(input_file1) # return a dataframe type
df2 = pd.read_csv(input_file2) # return a dataframe type

print(df1.columns) # check all the features' names
print(df1.shape)
df1.head()

print(df2.columns) # check all the features' names
print(df2.shape)
df2.head()

df_merged = pd.merge(df1, df2, how="left", on=['building_id', 'district_id', 'vdcmun_id', 'ward_id'])
print(df_merged.shape)
print(df_merged.columns)
df_merged.head()

"""# Step 2. Remove rows with empty entries"""

# Check if there is null values 
df_merged.isnull().sum()

df_merged.dropna(inplace=True)

# final check if there is null values 
df_merged.isnull().sum()

"""# Step 3. Unify the field names."""

input_file3 = '/content/drive/MyDrive/train_values.csv'   
df3 = pd.read_csv(input_file3) # return a dataframe type 
missing_col = []
for col in df3.columns:
  if col not in df_merged.columns:
    missing_col.append(col)
print(missing_col)

print(df_merged.columns)

df_merged.rename(columns = {'age_building':'age', \
                            'plinth_area_sq_ft':'area_percentage', \
                            'height_ft_pre_eq':'height_percentage', \
                            'district_id':'geo_level_1_id',\
                            'vdcmun_id':'geo_level_2_id', \
                            'ward_id':'geo_level_3_id'}, inplace = True)

"""## Normalize the area percentage and height percentage. """

df3['area_percentage']

df_merged['area_percentage'] = round(df_merged['area_percentage']*100/max(df_merged['area_percentage'])).astype('int64')

df3['height_percentage']

df_merged['height_percentage'] = round(df_merged['height_percentage']*100/max(df_merged['height_percentage'])).astype('int64')

"""# Step 4. Rewrite "Damge grade" feature"""

df_merged['damage_grade']

replace_dict = {}
for d in range(1,6):
  replace_dict['Grade {}'.format(d)] = d
print(replace_dict)

df_merged['damage_grade'].replace(replace_dict, inplace=True)
df_merged['damage_grade'] = df_merged['damage_grade'].astype("int64")

df_merged['damage_grade'].hist()

"""#Step 5. Remove unwanted columns 
We remove columns that are in the datafile of the drivendata website.
"""

unwanted_col = []
for col in df_merged.columns:
  if col not in df3.columns:
    unwanted_col.append(col)
unwanted_col

df_merged.drop('count_floors_post_eq', axis=1, inplace=True) 
df_merged.drop('height_ft_post_eq', axis=1, inplace=True) 
df_merged.drop('condition_post_eq', axis=1, inplace=True) 
df_merged.drop('technical_solution_proposed', axis=1, inplace=True)

df_merged.shape

"""# Save the preprocessed file to output csv"""

# Save file to csv.
output_file = '/content/drive/MyDrive/earthquake/preprocessed_data.csv'
df_merged.to_csv(output_file, index=False)