import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dython.nominal import associations


#overall data
data = pd.read_csv('preprocessed_data.csv')
df = data[['age','count_floors_pre_eq', 'damage_grade']]

def filter_dataframe(df, columns):
    '''
    This function receives a DataFrame object and
    a list of column names belonging to the DataFrame
    and returns the subset of the DataFrame

    :params: df, columns
    :type df: DataFrame
    :type columns: list
    :returns: DataFrame of subset of data
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(columns, list)

    for c in columns:
        assert c in list(df.columns)
    
    return df[columns]

def get_corr_matrix(df, img_name):
    '''
    This function displays the correlation matrix
    plot between variables in the dataframe.

    :params df, img_name
    :type img_name: string
    :type df: DataFrame
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(img_name, str)

    assert 'png' in img_name[-3:] or \
        'jpg' in img_name[-3:] or 'jpeg' in img_name[-4:] 

    associations(df, filename='age_correlation.png', figsize=(10,10))

def plot_stacked(df):
    '''
    This function plots the stacked barplot
    of the number of floors in the building against damage grade

    :params: df
    :type df: DataFrame
    '''
    assert isinstance(df, pd.DataFrame)
    labels = ['1','2','3','4','>4']
    df.loc[df['count_floors_pre_eq'] > 4, 0] = 5
    df.groupby([ 'damage_grade', 'count_floors_pre_eq']).size().unstack(1).plot(kind='bar', stacked=True)
    plt.title('Number of Floors vs Damage Grade')
    plt.legend(title='Number of Floors', loc='upper left', fontsize='small', labels=['1','2','3','4','> 4'])
    plt.xticks(ticks=range(5), labels=labels)
    plt.show()
