import pandas as pd

def material_damage_by_age_group(data):
    """ For the earthquake data set, it is grouped into age ranges of 5 years then organized by material,
    with all other columns besides damage_grade, materials, and age dropped.
    
    Data set is then ready for damage vs material by age plots

    Args:
        data (DataFrame): earthquake data set

    Returns:
        DatatFrame: dataset groups by age range and material used
    """
    
    assert isinstance(data, pd.DataFrame), "Passed in data must be a DataFrame"
    
    assert 'age' in list(data.columns), "data set must have age column"

    data = data.sort_values(by=['age']).reset_index(drop=True)

    for row in range(711960,len(data['age'])):
        age = data.loc[row,'age']

        if isinstance(age,str):
            continue
        
        assert isinstance(age,int) or isinstance(age,float), "all age values must be integers"

        if 0 <= age <= 5:
            data.loc[row, 'age'] = '0-5 years'

        elif 6 <= age <= 10:
            data.loc[row,'age'] = '6-10 years'

        elif 11 <= age <= 15:
            data.loc[row,'age'] = '11-15 years'

        elif 16 <= age <= 20:
            data.loc[row,'age'] = '16-20 years'

        elif 21 <= age <= 25:
            data.loc[row,'age'] = '21-25 years'

        elif 26 <= age <= 30:
            data.loc[row,'age'] = '26-30 years'

        elif 31 <= age <= 35:
            data.loc[row,'age'] = '31-35 years'

        elif 36 <= age <= 40:
            data.loc[row,'age'] = '36-40 years'

        elif 41 <= age <= 45:
            data.loc[row,'age'] = '41-45 years'

        elif 46 <= age <= 50:
            data.loc[row,'age'] = '46-50 years'

        elif 51 <= age <= 55:
            data.loc[row,'age'] = '51-55 years'

        elif 56 <= age <= 60:
            data.loc[row,'age'] = '56-60 years'

        elif 61 <= age <= 65:
            data.loc[row,'age'] = '61-65 years'

        elif 66 <= age <= 70:
            data.loc[row,'age'] = '66-70 years'

        elif 71 <= age <= 75:
            data.loc[row,'age'] = '71-75 years'

        elif 76 <= age <= 80:
            data.loc[row,'age'] = '76-80 years'

        elif 81 <= age <= 85:
            data.loc[row,'age'] = '81-85 years'

        elif 86 <= age <= 90:
            data.loc[row,'age'] = '86-90 years'

        elif 91 <= age <= 95:
            data.loc[row,'age'] = '91-95 years'

        elif 96 <= age <= 100:
            data.loc[row,'age'] = '96-100 years'

        else:
            data.loc[row,'age'] = '100+ years'
        
    materials = ['has_superstructure_adobe_mud', 'has_superstructure_mud_mortar_stone',
       'has_superstructure_stone_flag',
       'has_superstructure_cement_mortar_stone',
       'has_superstructure_mud_mortar_brick',
       'has_superstructure_cement_mortar_brick', 'has_superstructure_timber',
       'has_superstructure_bamboo', 'has_superstructure_rc_non_engineered',
       'has_superstructure_rc_engineered', 'has_superstructure_other']
    
    for material in materials:
        assert material in list(data.columns), "data set must have provided materials"
        
    assert 'damage_grade' in list(data.columns), "data set must have damage grade column"
    
    damage_vs_materials = data[['age','has_superstructure_adobe_mud', 'has_superstructure_mud_mortar_stone',
       'has_superstructure_stone_flag',
       'has_superstructure_cement_mortar_stone',
       'has_superstructure_mud_mortar_brick',
       'has_superstructure_cement_mortar_brick', 'has_superstructure_timber',
       'has_superstructure_bamboo', 'has_superstructure_rc_non_engineered',
       'has_superstructure_rc_engineered', 'has_superstructure_other', 'damage_grade']].copy()
    
    damage_rates = []
    plot_labels = []

    for material in materials:
        material_damage = damage_vs_materials.loc[damage_vs_materials[material] == True]
        material_damage = material_damage[['age','damage_grade']].copy()

        material_damage = material_damage.groupby('age').mean()

        damage_rates.append(material_damage)

        plot_labels.append(material.replace('has_superstructure_', ''))
        
    damages = pd.DataFrame(columns=plot_labels)

    for index in range(0,len(plot_labels)):
        column_name = plot_labels[index]

        damages[column_name] = damage_rates[index]

    damages = damages.drop(columns=['other'])

    damages.to_csv("material_damages_by_age_group.csv")
    
    return damages
