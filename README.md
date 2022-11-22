# ECE143 FA22 Group 10 Earthquake Analysis
## Data Preprocessing 
Three data files are needed: csv_building_ownership_and_use.csv; csv_building_structure.csv; train_values.csv. 
Previous two files are downloaded from the official website http://eq2015.npc.gov.np/#/ which contain different features; we would like to combine them to make the complete dataset. The third data file is a preprocessed version provided by https://www.drivendata.org/competitions/57/nepal-earthquake/page/136/. 

We are unsatisfied with the truncated version provided by the drivendata website as it removes data rows with damage grade (the output feature) greater than 3, which causes a lost of about 40,000 rows of data. Also, the drivendata website uses some random letters to represent the categorical data, which obfuscates the true meaning of the each category. For example, a building from "train_values.csv" has the feature "land_surface_condition" drawn from {'n', 'o', 't'}, while it is represented by {'Flat','Steep slope', 'Moderate slope'} in the original file.

To perform the preprocessing step, download all 3 required files and run "data_preprocessing.py". 

## Data Analysis Task 
The earthquake dataset includes 39 columns plus one output column called "damage_grade". We study how the individual features as well as their interactions correlate with the building's damage level. 

To study the impact of the building's age feature, land feature ('land_surface_condition') and structure features (i.e. 'foundation_type', 'ground_floor_type', 'roof_type', 'count_floor_pre_eq', 'position'), run "age, land features and structure features.py".

#### ```Number of Floors in Building vs Damage Grade```
It seemed intuitive to take a look and analyze how the number of floors in a building could cause more or lesser damage. We represented the distribution in a stacked barplot, and then visualized it in a line plot of the average damage grade vs. the number of floors in a building. We came to a conclusion that there is some increasing trend in damage grade for low rise buildings, but the damage startes decreasing as the number of floors go past four. We assume that there is some underlying reason for this pattern, like the materials used for example.


### Task4:Superstructure Materials VS Damage Grade 
Check the code of this part by using [superstructure.py](https://github.com/yongyx/ECE143_Earthquake_Analysis/blob/main/superstructure.py)
* CONCLUSION:
  * For buildings using single material on superstructure, rc engineered & rc-non-engineered & cement-mortar-brick can lead to low damage grade
  * For buildings using combined materials on superstructure, combining natural materails like timber,bambo, adobe mud with rc-engineered can avoid serious damage. 
