import pandas as pd

#%%
#     2. Define Functions for generating plots and tables in deep diving pages
#
#%% 2.1 Define the metrics function (two scopes)
# This metric function generates a new dataset contained the value of metricOne/PopulaitonOne
# and the value of metricTwo/PopulaitonTwo for different ethnic groups at two geographical scopes.

def metric_DEI_FourG_twoScopes(df,metricname,dimension,stage,weight,metricOne,metricTwo,populOne,PopulTwo):

    # CLEAN UP DATA
    ''' consider metrics with counting numbers only. no proportion '''
    df_clean = df[(df['var_type'] == 'count')]
    ''' focus on black, hispanic, white and asian ethnic individual groups '''
    df_clean_fourGroups = df_clean[(df_clean['var_ethnic'] != "all") &
                                   (df_clean['var_ethnic'] != "black_hispanic") &
                                   (df_clean['var_ethnic'] != "white_asian")
                                   ]

    # Extract and Process values
    ''' extract numerators '''
    df_subset = df_clean_fourGroups.copy()[(df_clean_fourGroups["metrics_new"] == metricOne) | (df_clean_fourGroups["metrics_new"] == metricTwo) ]
    ''' rename the value in subset dataset to subset_popul '''
    df_subset.rename(columns = {'population':'subset_popul'}, inplace = True)
    ''' extract denominators '''
    df_popul = df_clean_fourGroups[(df_clean_fourGroups["metrics_new"] == populOne) | (df_clean_fourGroups["metrics_new"] == PopulTwo) ]
    ''' merge two extracted datasets '''
    df_merge = pd.merge(df_subset, df_popul,  how = 'left', left_on=['var_scope','var_ethnic'], right_on = ['var_scope','var_ethnic'])
    ''' define the methodology '''
    df_merge['metric_value'] = (df_merge['subset_popul'] / df_merge['population'])
    ''' assign the weight to this metirc '''
    df_merge['weight'] = weight
    ''' assign the metricname to this metirc '''
    df_merge['metric_name'] = metricname
    ''' assign the dimension to this metirc '''
    df_merge['dimension'] = dimension
    ''' assign the stage to this metirc '''
    df_merge['stage'] = stage
    ''' drop redundant variables in merged dataframe '''
    df_metric = df_merge.loc[:,['metric_name','stage','dimension','metrics_new_x','var_scope','var_ethnic','subset_popul','population','metric_value','weight']]
    df_metric.rename(columns = {'metrics_new_x':'metrics_new'}, inplace = True)

    return(df_metric)

#%% 2.2 Define the metrics function (one scope)
# This metric function generates a new dataset contained the value of metricOne/PopulaitonOne
# for different ethnic groups at one geographical scope.

# define the metric funtion
def metric_DEI_FourG_oneScope(df,metricname,dimension,stage,weight,metricOne,populOne):
    # CLEAN UP DATA
    ''' consider metrics with counting numbers only. no proportion '''
    df_clean = df[(df['var_type'] == 'count')]
    ''' focus on black, hispanic, white and asian ethnic individual groups '''
    df_clean_fourGroups = df_clean[(df_clean['var_ethnic'] != "all") &
                                   (df_clean['var_ethnic'] != "black_hispanic") &
                                   (df_clean['var_ethnic'] != "white_asian")
                                   ]

    ''' extract numerators '''
    df_subset = df_clean_fourGroups.copy()[(df_clean_fourGroups["metrics_new"] == metricOne)]
    ''' rename the value in subset dataset to subset_popul '''
    df_subset.rename(columns = {'population':'subset_popul'}, inplace = True)
    ''' extract denominators '''
    df_popul = df_clean_fourGroups[(df_clean_fourGroups["metrics_new"] == populOne)]
    ''' merge two extracted datasets '''
    df_merge = pd.merge(df_subset, df_popul,  how = 'left', left_on=['var_scope','var_ethnic'], right_on = ['var_scope','var_ethnic'])
    ''' define the methodology '''
    df_merge['metric_value'] = (df_merge['subset_popul'] / df_merge['population'])
    ''' assign the weight to this metirc '''
    df_merge['weight'] = weight
    ''' assign the metricname to this metirc '''
    df_merge['metric_name'] = metricname
    ''' assign the dimension to this metirc '''
    df_merge['dimension'] = dimension
    ''' assign the stage to this metirc '''
    df_merge['stage'] = stage
    ''' drop redundant variables in merged dataframe '''
    df_metric = df_merge.loc[:,['metric_name','stage','dimension','metrics_new_x','var_scope','var_ethnic','subset_popul','population','metric_value','weight']]
    df_metric.rename(columns = {'metrics_new_x':'metrics_new'}, inplace = True)

    return(df_metric)