import pandas as pd

# IMPORTANT: edit appropriate file path
space_data = pd.read_csv('preprocessed_data.csv', usecols = ['area_percentage','height_percentage','damage_grade','age'])

# Task 5
# separating data based on damage levels
data_dmg_1 = space_data[space_data['damage_grade'] == 1]
data_dmg_2 = space_data[space_data['damage_grade'] == 2]
data_dmg_3 = space_data[space_data['damage_grade'] == 3]
data_dmg_4 = space_data[space_data['damage_grade'] == 4]
data_dmg_5 = space_data[space_data['damage_grade'] == 5]

# extracting height
height_dmg_1 = data_dmg_1['height_percentage']
height_dmg_1 = height_dmg_1.reset_index(drop=True)
height_dmg_2 = data_dmg_2['height_percentage']
height_dmg_2 = height_dmg_2.reset_index(drop=True)
height_dmg_3 = data_dmg_3['height_percentage']
height_dmg_3 = height_dmg_3.reset_index(drop=True)
height_dmg_4 = data_dmg_4['height_percentage']
height_dmg_4 = height_dmg_4.reset_index(drop=True)
height_dmg_5 = data_dmg_5['height_percentage']
height_dmg_5 = height_dmg_5.reset_index(drop=True)

height_vs_damage = pd.DataFrame()
height_vs_damage['1'] = height_dmg_1
height_vs_damage['2'] = height_dmg_2
height_vs_damage['3'] = height_dmg_3
height_vs_damage['4'] = height_dmg_4
height_vs_damage['5'] = height_dmg_5
height_vs_damage.to_csv('space_height_damage.csv', index=False)

# extracting area
area_dmg_1 = data_dmg_1['area_percentage']
area_dmg_1 = area_dmg_1.reset_index(drop=True)
area_dmg_2 = data_dmg_2['area_percentage']
area_dmg_2 = area_dmg_2.reset_index(drop=True)
area_dmg_3 = data_dmg_3['area_percentage']
area_dmg_3 = area_dmg_3.reset_index(drop=True)
area_dmg_4 = data_dmg_4['area_percentage']
area_dmg_4 = area_dmg_4.reset_index(drop=True)
area_dmg_5 = data_dmg_5['area_percentage']
area_dmg_5 = area_dmg_5.reset_index(drop=True)

area_vs_damage = pd.DataFrame()
area_vs_damage['1'] = area_dmg_1
area_vs_damage['2'] = area_dmg_2
area_vs_damage['3'] = area_dmg_3
area_vs_damage['4'] = area_dmg_4
area_vs_damage['5'] = area_dmg_5
area_vs_damage.to_csv('space_area_damage.csv', index=False)

# task 10

# separating data into age groups
data_lt_10 = space_data[space_data['age'] < 10]
data_10to50 = space_data[space_data['age'] >= 10]
data_10to50 = data_10to50[data_10to50['age'] < 50]
data_gt_50 = space_data[space_data['age'] >= 50]

# Q1 - Height vs Damage in 3 Age groups...{age < 10, 10 <= age < 50, and age >= 50}
# extracting height age group 1
h_age1_d1 = data_lt_10[data_lt_10['damage_grade'] == 1]
h_age1_d1 = h_age1_d1.reset_index(drop=True)
h_age1_d2 = data_lt_10[data_lt_10['damage_grade'] == 2]
h_age1_d2 = h_age1_d2.reset_index(drop=True)
h_age1_d3 = data_lt_10[data_lt_10['damage_grade'] == 3]
h_age1_d3 = h_age1_d3.reset_index(drop=True)
h_age1_d4 = data_lt_10[data_lt_10['damage_grade'] == 4]
h_age1_d4 = h_age1_d4.reset_index(drop=True)
h_age1_d5 = data_lt_10[data_lt_10['damage_grade'] == 5]
h_age1_d5 = h_age1_d5.reset_index(drop=True)

age1_h_v_d = pd.DataFrame()
age1_h_v_d['1'] = h_age1_d1['height_percentage']
age1_h_v_d['2'] = h_age1_d2['height_percentage']
age1_h_v_d['3'] = h_age1_d3['height_percentage']
age1_h_v_d['4'] = h_age1_d4['height_percentage']
age1_h_v_d['5'] = h_age1_d5['height_percentage']
age1_h_v_d.to_csv('age1_h_v_d.csv', index=False)

# extracting height age group 2
h_age2_d1 = data_10to50[data_10to50['damage_grade'] == 1]
h_age2_d1 = h_age2_d1.reset_index(drop=True)
h_age2_d2 = data_10to50[data_10to50['damage_grade'] == 2]
h_age2_d2 = h_age2_d2.reset_index(drop=True)
h_age2_d3 = data_10to50[data_10to50['damage_grade'] == 3]
h_age2_d3 = h_age2_d3.reset_index(drop=True)
h_age2_d4 = data_10to50[data_10to50['damage_grade'] == 4]
h_age2_d4 = h_age2_d4.reset_index(drop=True)
h_age2_d5 = data_10to50[data_10to50['damage_grade'] == 5]
h_age2_d5 = h_age2_d5.reset_index(drop=True)

age2_h_v_d = pd.DataFrame()
age2_h_v_d['1'] = h_age2_d1['height_percentage']
age2_h_v_d['2'] = h_age2_d2['height_percentage']
age2_h_v_d['3'] = h_age2_d3['height_percentage']
age2_h_v_d['4'] = h_age2_d4['height_percentage']
age2_h_v_d['5'] = h_age2_d5['height_percentage']
age2_h_v_d.to_csv('age2_h_v_d.csv', index=False)

# extracting height age group 3
h_age3_d1 = data_gt_50[data_gt_50['damage_grade'] == 1]
h_age3_d1 = h_age3_d1.reset_index(drop=True)
h_age3_d2 = data_gt_50[data_gt_50['damage_grade'] == 2]
h_age3_d2 = h_age3_d2.reset_index(drop=True)
h_age3_d3 = data_gt_50[data_gt_50['damage_grade'] == 3]
h_age3_d3 = h_age3_d3.reset_index(drop=True)
h_age3_d4 = data_gt_50[data_gt_50['damage_grade'] == 4]
h_age3_d4 = h_age3_d4.reset_index(drop=True)
h_age3_d5 = data_gt_50[data_gt_50['damage_grade'] == 5]
h_age3_d5 = h_age3_d5.reset_index(drop=True)

age3_h_v_d = pd.DataFrame()
age3_h_v_d['1'] = h_age3_d1['height_percentage']
age3_h_v_d['2'] = h_age3_d2['height_percentage']
age3_h_v_d['3'] = h_age3_d3['height_percentage']
age3_h_v_d['4'] = h_age3_d4['height_percentage']
age3_h_v_d['5'] = h_age3_d5['height_percentage']
age3_h_v_d.to_csv('age3_h_v_d.csv', index=False)

# Q2 - Area vs Damage in 3 Age groups...{age < 10, 10 <= age < 50, and age >= 50}
# extracting area age group 1
age1_a_v_d = pd.DataFrame()
age1_a_v_d['1'] = h_age1_d1['area_percentage']
age1_a_v_d['2'] = h_age1_d2['area_percentage']
age1_a_v_d['3'] = h_age1_d3['area_percentage']
age1_a_v_d['4'] = h_age1_d4['area_percentage']
age1_a_v_d['5'] = h_age1_d5['area_percentage']
age1_a_v_d.to_csv('age1_a_v_d.csv', index=False)

# extracting area age group 2
age2_a_v_d = pd.DataFrame()
age2_a_v_d['1'] = h_age2_d1['area_percentage']
age2_a_v_d['2'] = h_age2_d2['area_percentage']
age2_a_v_d['3'] = h_age2_d3['area_percentage']
age2_a_v_d['4'] = h_age2_d4['area_percentage']
age2_a_v_d['5'] = h_age2_d5['area_percentage']
age2_a_v_d.to_csv('age2_a_v_d.csv', index=False)

# extracting area age group 3
age3_a_v_d = pd.DataFrame()
age3_a_v_d['1'] = h_age3_d1['area_percentage']
age3_a_v_d['2'] = h_age3_d2['area_percentage']
age3_a_v_d['3'] = h_age3_d3['area_percentage']
age3_a_v_d['4'] = h_age3_d4['area_percentage']
age3_a_v_d['5'] = h_age3_d5['area_percentage']
age3_a_v_d.to_csv('age3_a_v_d.csv', index=False)
