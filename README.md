# ECE143 FA22 Group 10 Earthquake Analysis
## Data Preprocessing 
Three data files are needed: csv_building_ownership_and_use.csv; csv_building_structure.csv; train_values.csv. 
Previous two files are downloaded from the official website http://eq2015.npc.gov.np/#/ which contain different features; we would like to combine them to make the complete dataset. The third data file is a preprocessed version provided by https://www.drivendata.org/competitions/57/nepal-earthquake/page/136/. 

We are unsatisfied with the truncated version provided by the drivendata website as it removes data rows with damage grade (the output feature) greater than 3, which causes a lost of about 40,000 rows of data. Also, the drivendata website uses some random letters to represent the categorical data, which obfuscates the true meaning of the each category. For example, a building from "train_values.csv" has the feature "land_surface_condition" drawn from {'n', 'o', 't'}, while it is represented by {'Flat','Steep slope', 'Moderate slope'} in the original file.

To perform the preprocessing step, download all 3 required files and run "data_preprocessing.py". 

## Data Analysis Task 
The earthquake dataset includes 39 columns plus one output column called "damage_grade". We study how the individual features as well as their interactions correlate with the building's damage level. 

To study the impact of the building's age feature, land feature ('land_surface_condition') and structure features (i.e. 'foundation_type', 'ground_floor_type', 'roof_type', 'count_floor_pre_eq', 'position'), run "age, land features and structure features.py".
