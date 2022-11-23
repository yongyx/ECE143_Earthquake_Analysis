# ECE143 FA22 Group 10 Earthquake Analysis
## Dependencies
The following packages are needed to run this files in this repository:

- pandas
- seaborn
- matplotlib
- numpy
- dython

They can be run using the following command: ```pip install package_name```

```
+--src/
   ┣ age, land features and structure features.py
   ┣ building_count.py
   ┣ damage_by_age.py
   ┣ data_preprocessing.py
   ┣ height_area_age_damage.py
   ┗ superstructure.py
+--data/
   ┗ material_damages_by_age_group.csv
+--README.md/
+--visualizations.ipynb/
```

## Data Preprocessing 
Three data files are needed: csv_building_ownership_and_use.csv; csv_building_structure.csv; train_values.csv. 
Previous two files are downloaded from the official website http://eq2015.npc.gov.np/#/ which contain different features; we would like to combine them to make the complete dataset. The third data file is a preprocessed version provided by https://www.drivendata.org/competitions/57/nepal-earthquake/page/136/. 

We are unsatisfied with the truncated version provided by the drivendata website as it removes data rows with damage grade (the output feature) greater than 3, which causes a lost of about 40,000 rows of data. Also, the drivendata website uses some random letters to represent the categorical data, which obfuscates the true meaning of the each category. For example, a building from "train_values.csv" has the feature "land_surface_condition" drawn from {'n', 'o', 't'}, while it is represented by {'Flat','Steep slope', 'Moderate slope'} in the original file.

To perform the preprocessing step, download all 3 required files and run "data_preprocessing.py". 

## Data Analysis Task 
The earthquake dataset includes 39 columns plus one output column called "damage_grade". We study how the individual features as well as their interactions correlate with the building's damage level. 

#### ```Age, Land, and Structure Features```

**NOTE**: To study the impact of the building's age feature, land feature ('land_surface_condition') and structure features (i.e. 'foundation_type', 'ground_floor_type', 'roof_type', 'count_floor_pre_eq', 'position'), run "age, land features and structure features.py".

#### CONCLUSION:
* The number of floors alone has no correlation with the building's damage level. However, buildings with more floors tend to use more robust materials (i.e. RC) as the construction material and thus causing a smaller damage grade on average, while buildings with less floors tend to use more natural materials (e.g. mud, bamboo etc.) for the construction, thus the buildings are more vulnerable to the earthquake.
---
#### ```Number of Floors in Building vs Damage Grade```

**NOTE**: Check the code of this part by using [building_count.py](https://github.com/yongyx/ECE143_Earthquake_Analysis/blob/main/building_count.py)

* Intuitively, it seemed like the number of floors in the building could affect the damage done to the building, so we extracted that feature to conduct an analysis.
* We represented the distribution in a stacked barplot, and then visualized it in a line plot of the average damage grade vs. the number of floors in a building. 
#### CONCLUSION:
* There is some increasing trend in damage grade for low rise buildings, but the damage startes decreasing as the number of floors go past four. We assume that there is some underlying reason for this pattern, like the materials used for example.

---
#### ```Damage Grade vs Materials by Age Group```

We wanted to see if the age of a building changed the impact that the building materials used had on the damage grade. The data is grouped in age ranges of 5 years, and only maintains features detailing the average damage rate of each material. This cut-down dataset can be reproduced by runing \'damage_by_age.py\' using the dataset prodcued from running \'data_preprocessing.py\'. It will automatically save the damage by age data to the file \'material_damages_by_age_group.csv\'.

---
#### ```Superstructure Materials VS Damage Grade ```
**NOTE:** Check the code of this part by using [superstructure.py](https://github.com/yongyx/ECE143_Earthquake_Analysis/blob/main/superstructure.py)  
#### CONCLUSION:
* For buildings using single material on superstructure, rc-engineered & rc-non-engineered & cement-mortar-brick can lead to low damage grade.
* For buildings using two materials on superstructure, combining natural materails like timber,bambo, adobe mud with rc-engineered can avoid serious damage. 
---
#### ```Height/Area vs Damage Grade (by Age Groups)```

**NOTE:** Check the code of this part by using [height_area_age_damage.py](https://github.com/yongyx/ECE143_Earthquake_Analysis/blob/main/height_area_age_damage.py).
* Running this file using the output of data_preprocessing.py will output the categorized data sets.
* The Jupyter notebook file contains visualizations of the above described processed data.
#### CONCLUSION:
* Buildings with higher height percentages tend to have higher damage grades.
* Buildings with higher area percentages tend to have lower damage grades.
* There has not been significant findings from categorizing the above characterstics by age groups.

---
