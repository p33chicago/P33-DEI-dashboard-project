#%%
#                        1. Environment settings
#
#%%
import os
import pandas as pd
import plotly.express as px
from plotly.offline import plot
import plotly.io as io
io.renderers.default='svg'
from viz import set_default_theme
set_default_theme()

#%% Importing csv files

## Helps to display all rows and columns in pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

## Import DEI_CSV file
df = pd.read_csv('E:/p33/P33-DEI-dashboard-project/data/df_DEI_tidy_final.csv')
os.getcwd()
os.chdir('E:/p33/P33-DEI-dashboard-project/p33py/')













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
    df_subset = df_clean_fourGroups[(df_clean_fourGroups["metrics_new"] == metricOne) | (df_clean_fourGroups["metrics_new"] == metricTwo) ]   
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
    df_subset = df_clean_fourGroups[(df_clean_fourGroups["metrics_new"] == metricOne)]   
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

#%% 2.3 Define the visualization function for deep diving plots (DDP)

# define viz function
def figure_DDP(metric):
    # extract texts and annotations

    # display(df)
    fig = px.bar(metric, 
                 x=metric.var_scope, 
                 y=metric.metric_value, 
                 color=metric.var_ethnic, 
                 barmode='group')
    fig.update_traces(texttemplate='%{y}')
    fig.update_yaxes(title='proportion')
    
    return plot(fig)

#%% 2.4 Define the visualization function for deep diving tables (DDT)

# define viz function
def figure_DDT(metric):
    # create a dataframe
    ''' drop national metrics '''
    metric_regional=metric[(metric['var_scope'] != "usa")]
    metric_clean=metric_regional.drop(['metrics_new','var_scope'], axis = 1)
    ''' caculate the target proportion by using the avg. proportion of white and asian groups ''' 
    prop_target = metric_clean[(metric_clean['var_ethnic'] == "white") |
                               (metric_clean['var_ethnic'] == "asian")]['metric_value'].mean()
    ''' add interested variables  to dataset'''
    metric_clean['popul_target'] = metric_clean['population']*prop_target
    metric_clean['gap'] = metric_clean['popul_target'] - metric_clean['subset_popul']
    ''' rearrange data for table display'''
    metric_display = metric_clean[['var_ethnic', 'population', 'subset_popul', 'popul_target', 'gap']]
    
    return metric_display












#%%
#       3. Define Functions for caculating Equality Indexes in landing pages
#
#%%3.1 create a function that combine all the individual metrics and create a dataframe contained metric value from sigular geograhpic scope

def combiner_CHIAndIL (*df_metric):
    df_metrics_combined = pd.concat(df_metric)
    
    # select data from chicago/IL
    df_metrics_CHI = df_metrics_combined[(df_metrics_combined['var_scope']!='usa')]
    # drop populations, keep only proportions (metric values)
    df_metrics_CHI_slim = df_metrics_CHI.drop(['metrics_new','subset_popul','population'], axis = 1)
    # transfer dataframe structure from long to wide for later manipualation
    df_metrics_CHI_wide = pd.pivot(df_metrics_CHI_slim, index=['metric_name','var_scope','weight','dimension','stage'], columns='var_ethnic', values='metric_value')
    # transform index to vairables for later process
    df_metrics_CHI_wide.reset_index(inplace=True)
    
    return df_metrics_CHI_wide

#%%3.2 define the function caculates Equality index (EI) of each metrics using geometric means when there are 4 ethnic groups 

def EI_metric_FourG_geomean(df_metircs_selected):
    # caculate geometric mean of proportions of 4 ethnic groups
    df_metircs_selected['avg'] = ((df_metircs_selected['black']*df_metircs_selected['hispanic']*df_metircs_selected['white']*df_metircs_selected['asian'])**(0.25))
    # caculate the Inequality Index
    ''' II '''
    df_metircs_selected['II_metric'] = ((abs(df_metircs_selected['black']-df_metircs_selected['avg'])+
                                  abs(df_metircs_selected['hispanic']-df_metircs_selected['avg'])+
                                  abs(df_metircs_selected['white']-df_metircs_selected['avg'])+
                                  abs(df_metircs_selected['asian']-df_metircs_selected['avg']))/
                                 (4*df_metircs_selected['avg'])
                                 )
    ''' II sqrt'''
    df_metircs_selected['II_metric_SQRT'] = df_metircs_selected['II_metric']**0.5
    # scaling
    ''' find the most inequal metrics and use its II_SQRT as benchmark'''
    df_metircs_selected['II_metric_MAX']=df_metircs_selected['II_metric_SQRT'].max()
    ''' Transform II_SQURT to EI, the equality index'''
    df_metircs_selected['EI_metric']=(100-((df_metircs_selected['II_metric_SQRT']/df_metircs_selected['II_metric_MAX'])*100))
    ''' Caculate the weighted EI'''
    df_metircs_selected['EI_metric_weighted']=df_metircs_selected['EI_metric']*df_metircs_selected['weight']
    
    return df_metircs_selected

#%%3.3 Define a function that caculates Equality Index of dimensions using geometric means when there are 4 ethnic groups 

def EI_dimensions_FourG_geomean(df_metircs_selected):
    ''' Caculate the weighted EI for each metrics'''
    df_metrics = EI_metric_FourG_geomean(df_metircs_selected)
    ''' caculate the EI for each dimensions '''
    df_dimension_EI = df_metrics.groupby(by=['var_scope','stage','dimension']).sum('EI_metric_weighted').drop(['weight'], axis = 1)
    ''' Rename the recaculated column '''
    df_dimension_EI.rename(columns = {'EI_metric_weighted':'EI_dim_weighted'}, inplace = True)
    ''' Transform indexes to variables '''
    df_dimension_EI.reset_index(inplace=True)
    ''' Drop redundant columns '''
    df_dimension_EI = df_dimension_EI.loc[:,['var_scope','stage','dimension','EI_dim_weighted']]
   
    return df_dimension_EI


#%%3.4 Define a function that caculates Equality Index of educational stages using geometric means when there are 4 ethnic groups 

def EI_stages_FourG_geomean(df_metircs_selected):
    
    ''' Caculate the weighted EI for each metrics'''
    df_dimension_EI = EI_dimensions_FourG_geomean(df_metircs_selected)
    
    ''' define the function that generates weighted EI for each dimensions'''
    def generates_dim_weight (df_dim_EI):
        
        ''' assgin weights to each dimensions'''
        def assign_weight(df):
            # k8
            if (df['stage'] == 'k8') & (df['dimension'] == 'access'):
                return 0.2
            elif (df['stage'] == 'k8') & (df['dimension'] == 'proficiency'):
                return 0.4
            elif (df['stage'] == 'k8') & (df['dimension'] == 'excellence'):
                return 0.4
            # hs
            elif (df['stage'] == 'hs') & (df['dimension'] == 'access'):
                return 0.2
            elif (df['stage'] == 'hs') & (df['dimension'] == 'proficiency'):
                return 0.4
            elif (df['stage'] == 'hs') & (df['dimension'] == 'excellence'):
                return 0.4
            # col
            elif (df['stage'] == 'col') & (df['dimension'] == 'access'):
                return 0.2
            elif (df['stage'] == 'col') & (df['dimension'] == 'proficiency'):
                return 0.4
            elif (df['stage'] == 'col') & (df['dimension'] == 'excellence'):
                return 0.4
            # emp
            elif (df['stage'] == 'emp') & (df['dimension'] == 'access'):
                return 0.5
            elif (df['stage'] == 'emp') & (df['dimension'] == 'proficiency'):
                return 0.5
            elif (df['stage'] == 'emp') & (df['dimension'] == 'excellence'):
                return 0.5
            
        df_dim_EI['weight_dim'] = df_dim_EI.apply(assign_weight, axis = 1)
        df_dim_EI['weighted_EI_dim'] = df_dim_EI['EI_dim_weighted']*df_dim_EI['weight_dim']
        df_dim_EI_weighted = df_dim_EI
        
        return df_dim_EI_weighted
    
    ''' Use the function above to generate a dataframe with weighted EI of dimensions'''
    df_dimension_EI_weighted = generates_dim_weight(df_dimension_EI)
    
    ''' caculate the EI of each educational stages'''
    df_stage_EI = df_dimension_EI_weighted.groupby(by=['stage','var_scope']).sum('weighted_EI_dim').drop(['weight_dim'], axis = 1)
    
    ''' Rename the recaculated column '''
    df_stage_EI.rename(columns = {'weighted_EI_dim':'weighted_EI_stage'}, inplace = True)
    
    ''' Transform indexes to variables '''
    df_stage_EI.reset_index(inplace=True)
    
    ''' Drop redundant columns '''
    df_stage_EI = df_stage_EI.loc[:,['EI_dim_weighted']]
    
    return df_stage_EI
    










#%%
#    4. Define Interested Metrics and create dataframes for plotly and EI generation
#
#%% 4.1 create interested metrics datasets using metric functons above

# K-8 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Proficiency
metric_k4_math_profAndAbove = metric_DEI_FourG_twoScopes(df,
                                                   'metric_k4_math_profAndAbove',
                                                   'proficiency',
                                                   'k8',
                                                   0.33,
                                                   '2021___city_chi___k8_4th___math_prof&abov___cps',  # numerators for city of chicago
                                                   '2021___usa___k8_4th___math_prof&abov', # numerators for US
                                                   '2022___city_chi___k8_4th___popul___cps', # denominators for city of chicago
                                                   '2020___usa___k8_4th___popul') # denominators for US 

metric_k8_math_profAndAbove = metric_DEI_FourG_twoScopes(df,
                                                   'metric_k8_math_profAndAbove',
                                                   'proficiency',
                                                   'k8',
                                                   0.33,
                                                   '2021___city_chi___k8_8th___math_prof&abov___cps',
                                                   '2021___usa___k8_8th___math_prof&abov',
                                                   '2022___city_chi___k8_8th___popul___cps',
                                                   '2020___usa___k8_8th___popul') 

metric_k8_algebra_pass = metric_DEI_FourG_twoScopes(df,
                                              'metric_k8_algebra_pass',
                                              'proficiency',
                                              'k8',
                                              0.33,
                                              '2021___city_chi___k8_8th___math_algebra_pass___cps',
                                              '2021___usa___k8_8th___math_algebra_pass',
                                              '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                                              '2017___usa___k8_8th___math_algebra_enrol') 

## Excellence
metric_k4_math_adv = metric_DEI_FourG_twoScopes(df,
                                          'metric_k4_math_adv',
                                          'excellence',
                                          'k8',
                                          0.5,
                                          '2021___city_chi___k8_4th___math_advc___cps', 
                                          '2021___usa___k8_4th___math_advc',
                                          '2022___city_chi___k8_4th___popul___cps',
                                          '2020___usa___k8_4th___popul') 

metric_k8_math_adv = metric_DEI_FourG_twoScopes(df,
                                          'metric_k8_math_adv',
                                          'excellence',
                                          'k8',
                                          0.5,
                                          '2021___city_chi___k8_8th___math_advc___cps',
                                          '2021___usa___k8_8th___math_advc',
                                          '2022___city_chi___k8_8th___popul___cps',
                                          '2020___usa___k8_8th___popul') # denominators for US 

## Access
metric_k8_magnet_enrol = metric_DEI_FourG_oneScope(df,
                                             'metric_k8_magnet_enrol',
                                             'access',
                                             'k8',
                                             0.33, 
                                             '2021___city_chi___k8_total___mag_stem_enrol___cps',
                                             '2022___city_chi___k8_total___popul___cps')

#????????????
metric_k8_algebra_enrol = metric_DEI_FourG_twoScopes(df,
                                               'metric_k8_algebra_enrol',
                                               'access',
                                               'k8',
                                               0.33,
                                               '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                                               '2017___usa___k8_8th___math_algebra_enrol',
                                               '2022___city_chi___k8_8th___popul___cps',
                                               '2020___usa___k8_8th___popul') 

#????????????
metric_k8_noInt = metric_DEI_FourG_twoScopes(df,
                                       'metric_k8_noInt',
                                       'access',
                                       'k8',
                                       0.33,
                                       '2019___city_chi___k8_total___NOinternet_age5to17___cps',
                                       '2019___usa___k8_total___NOinternet_age5to17',
                                       '2022___city_chi___age_5to17__popul___cps',
                                       '2022___usa___age_5to17__popul') # denominators for US 

# High School >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Proficiency
metric_hs_sat_meetAndExceeds = metric_DEI_FourG_twoScopes(df,
                                                    'metric_hs_sat_meetAndExceeds',
                                                    'proficiency',
                                                    'hs',
                                                    0.5,
                                                    '2021___city_chi___hs___sat_math_meet&exceeds___cps',
                                                    '2021___usa___col___sat_math_meet&exceeds',
                                                    '2021___city_chi___hs_SATtaker___popul___cps',
                                                    '2021___usa___hs_SATtaker___popul')

metric_hs_apcs_aboveThree = metric_DEI_FourG_twoScopes(df,
                                                 'metric_hs_apcs_aboveThree',
                                                 'proficiency',
                                                 'hs',
                                                 0.5,
                                                 '2021___city_chi___hs___apcs_score3/4',
                                                 '2021___usa___hs___apcs_score3/4',
                                                 '2021___city_chi___hs_apcs___popul___cps',
                                                 '2021___usa___hs_apcs___popul')


## Excellence
metric_hs_sat_exceeds = metric_DEI_FourG_twoScopes(df,
                                             'metric_hs_sat_exceeds',
                                             'excellence',
                                             'hs',
                                             0.5,
                                             '2021___city_chi___hs___sat_math_exceeds___cps',
                                             '2021___usa___col___sat_math_exceeds',
                                             '2021___city_chi___hs_SATtaker___popul___cps',
                                             '2021___usa___hs_SATtaker___popul')

metric_hs_apcs_five = metric_DEI_FourG_twoScopes(df,
                                           'metric_hs_apcs_five',
                                           'excellence',
                                           'hs',
                                           0.5,
                                           '2021___city_chi___hs___apcs_score5___cps',
                                           '2021___usa___hs___apcs_score5',
                                           '2021___city_chi___hs_apcs___popul___cps',
                                           '2021___usa___hs_apcs___popul')

## Access
metric_hs_apcs_enrol = metric_DEI_FourG_twoScopes(df,
                                            'metric_hs_apcs_enrol',
                                            'access',
                                            'hs',
                                            0.25,
                                            '2021___city_chi___hs_apcs___popul___cps',
                                            '2021___usa___hs_apcs___popul',
                                            '2022___city_chi___hs_total___popul___cps',
                                            '2020___usa___hs_total___popul')

metric_hs_magnet_enrol = metric_DEI_FourG_oneScope(df,
                                             'metric_hs_magnet_enrol',
                                             'access',
                                             'hs',
                                             0.25,
                                             '2021___city_chi___hs___mag_enrol___cps',
                                             '2022___city_chi___hs_total___popul___cps')

metric_hs_CSInterested = metric_DEI_FourG_oneScope(df,
                                             'metric_hs_CSInterested',
                                             'access',
                                             'hs',
                                             0.25,
                                             '2021___city_chi___hs___cs_interested___cps',
                                             '2022___city_chi___hs_total___popul___cps')

#????????????
metric_hs_advMath_enrol = metric_DEI_FourG_twoScopes(df,
                                               'metric_hs_advMath_enrol',
                                               'access',
                                               'hs',
                                               0.25,
                                               '2017___city_chi___hs___math_advc___cps',
                                               '2017___usa___hs___math_advc_enroll',
                                               '2022___city_chi___hs_total___popul___cps',
                                               '2020___usa___hs_total___popul')

# College >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Proficiency
metric_col_cs_persist = metric_DEI_FourG_twoScopes(df,
                                             'metric_col_cs_persist',
                                             'proficiency',
                                             'col',
                                             0.5,
                                             '2021___state_il___col___cs_confer',
                                             '2021___usa___col___cs_confer',
                                             '2021___state_il___col___cs_enrol',
                                             '2021___usa___col___cs_enrol')

metric_col_cs_confer = metric_DEI_FourG_twoScopes(df,
                                            'metric_col_cs_confer',
                                            'proficiency',
                                            'col',
                                            0.5,
                                            '2021___state_il___col___cs_confer',
                                            '2021___usa___col___cs_confer',
                                            '2020___state_il___col___total_confer',
                                            '2021___usa___col___total_confer')

## Excellence
metric_col_topThree_cs_enrol = metric_DEI_FourG_twoScopes(df,
                                                    'metric_col_topThree_cs_enrol',
                                                    'excellence',
                                                    'col',
                                                    0.33,
                                                    '2021___state_il___col___t3_cs_enrol',
                                                    '2021___usa___col___t3_cs_enrol',
                                                    '2021___state_il___col___t3_enrol',
                                                    '2021___usa___col___t3_enrol')

metric_col_topThree_cs_persist = metric_DEI_FourG_twoScopes(df,
                                                      'metric_col_topThree_cs_persist',
                                                      'excellence',
                                                      'col',
                                                      0.33,
                                                      '2021___state_il___col___t3_cs_confer',
                                                      '2021___usa___col___t3_cs_confer',
                                                      '2021___state_il___col___t3_cs_enrol',
                                                      '2021___usa___col___t3_cs_enrol')

metric_col_topThree_cs_confer = metric_DEI_FourG_twoScopes(df,
                                                     'metric_col_topThree_cs_confer',
                                                     'excellence',
                                                     'col',
                                                     0.33,
                                                     '2021___state_il___col___t3_cs_confer', 
                                                     '2021___usa___col___t3_cs_confer',
                                                     '2021___state_il___col___t3_confer',
                                                     '2021___usa___col___t3_confer')

## Access
metric_col_cs_enrol = metric_DEI_FourG_twoScopes(df,
                                           'metric_col_cs_enrol',
                                           'access',
                                           'col',
                                           0.5,
                                           '2021___state_il___col___cs_enrol',
                                           '2021___usa___col___cs_enrol',
                                           '2022___state_il___col___total_enrol',
                                           '2021___usa___col___total_enrol')

metric_col_imdEnrol = metric_DEI_FourG_twoScopes(df,
                                           'metric_col_imdEnrol',
                                           'access',
                                           'col',
                                           0.5,
                                           '2021___state_il___col___immediate_enrol',
                                           '2021___usa___col___immediate_enrol',
                                           '2020___state_il___hs_grads___popul',
                                           '2022___usa___hs_grads___popul')
                
# Employment >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Proficiency
metric_emp_techJob = metric_DEI_FourG_twoScopes(df,
                                          'metric_emp_techJob',
                                          'proficiency',
                                          'emp',
                                          0.5,
                                          '2021___region_chi_msa___emp___csjob_t11_age19to24',
                                          '2021___usa___emp___csjob_t11_age19to24',
                                          '2022___region_chi_msa___emp___total_degree_holder',
                                          '2022___usa___emp___total_degree_holder')

## Excellence
metric_emp_techJob_topThree =  metric_DEI_FourG_twoScopes(df,
                                                    'metric_emp_techJob_topThree',
                                                    'excellence',
                                                    'emp',
                                                    0.5,
                                                    '2021___region_chi_msa___emp___csjob_t3',
                                                    '2021___usa___emp___csjob_t3',
                                                    '2022___region_chi_msa___emp___total_degree_holder',
                                                    '2022___usa___emp___total_degree_holder')


#%% 4.2 create a dataframe contained interested metric value from sigular geograhpic scope

df_metrics_CHI = combiner_CHIAndIL(metric_k4_math_profAndAbove,
                         metric_k8_math_profAndAbove,
                         metric_k8_algebra_pass,
                         metric_k4_math_adv,
                         metric_k8_math_adv,
                         metric_k8_magnet_enrol,
                         metric_k8_algebra_enrol,
                         metric_k8_noInt,
                         metric_hs_sat_meetAndExceeds,
                         metric_hs_apcs_aboveThree,
                         metric_hs_sat_exceeds,
                         metric_hs_apcs_five,
                         metric_hs_apcs_enrol,
                         metric_hs_magnet_enrol,
                         metric_hs_CSInterested,
                         metric_hs_advMath_enrol,
                         metric_col_cs_persist,
                         metric_col_cs_confer,
                         metric_col_topThree_cs_enrol,
                         metric_col_topThree_cs_persist,
                         metric_col_topThree_cs_confer,
                         metric_col_cs_enrol,
                         metric_col_imdEnrol,
                         metric_emp_techJob,
                         metric_emp_techJob_topThree)







#%%
#    5. Generates Plotly for deep diving pages and Generates EI for landing pages 
#
#%% 5.1 EI index for Landing pages

# caculate EI of each metrics
df_EI_metric_CHI = EI_metric_FourG_geomean(df_metrics_CHI)

# caculate EI of each dimensions at educational stages
df_EI_dimensions_CHI = EI_dimensions_FourG_geomean(df_metrics_CHI)

# caculate EI of each educational stages
df_EI_stages_CHI = EI_stages_FourG_geomean(df_metrics_CHI)

#%% 5.2 plots and tables for Deep diving pages

# k8      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## proficiency

### 4th grade Math proficiency and above
figure_DDP(metric_k4_math_profAndAbove)
figure_DDT(metric_k4_math_profAndAbove)
### 8th grade Math proficiency and above
figure_DDP(metric_k8_math_profAndAbove)
figure_DDT(metric_k8_math_profAndAbove)
### 8th grade passing algebra
figure_DDP(metric_k8_algebra_pass)
figure_DDT(metric_k8_algebra_pass)

## excellence
### 4th Math advanced
figure_DDP(metric_k4_math_adv)
figure_DDT(metric_k4_math_adv)
### 8th Math advanced
figure_DDP(metric_k8_math_adv)
figure_DDT(metric_k8_math_adv)

## access
### Lack of Household Internet Access
figure_DDP(metric_k8_noInt)
figure_DDT(metric_k8_noInt)
### STEM Magnet School Enrollment 
figure_DDP(metric_k8_magnet_enrol)
figure_DDT(metric_k8_magnet_enrol)
### 8th grade algebra 1 enrollment
figure_DDP(metric_k8_algebra_enrol)
figure_DDT(metric_k8_algebra_enrol)


# HS      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## proficiency

### HS SAT Math Proficiency and Above 
figure_DDP(metric_hs_sat_meetAndExceeds)
figure_DDT(metric_hs_sat_meetAndExceeds)
### AP CS scoring 3 or higher
figure_DDP(metric_hs_apcs_aboveThree)
figure_DDT(metric_hs_apcs_aboveThree)

## excellence
### HS SAT Math Advanced
figure_DDP(metric_hs_sat_exceeds)
figure_DDT(metric_hs_sat_exceeds)
### HS CPS AP CS scored 5
figure_DDP(metric_hs_apcs_five)
figure_DDT(metric_hs_apcs_five)

## access
### AP CS Enrollment
figure_DDP(metric_hs_apcs_enrol)
figure_DDT(metric_hs_apcs_enrol)
### CPS HS STEM Magnet School Enrollment
figure_DDP(metric_hs_magnet_enrol)
figure_DDT(metric_hs_magnet_enrol)
### CS Interest
figure_DDP(metric_hs_CSInterested)
figure_DDT(metric_hs_CSInterested)
### Advanced Math Enrollment
figure_DDP(metric_hs_advMath_enrol)
figure_DDT(metric_hs_advMath_enrol)


# col      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## proficiency
### Illinois CS/Computing Degree Persistence
figure_DDP(metric_col_cs_persist)
figure_DDT(metric_col_cs_persist)
### Illinois CS/Computing Degree Persistence
figure_DDP(metric_col_topThree_cs_confer)
figure_DDT(metric_col_topThree_cs_confer)

## excellence
### Illinois CS/Computing Degree Enrollment for Top 3 
figure_DDP(metric_col_topThree_cs_enrol)
figure_DDT(metric_col_topThree_cs_enrol)
### Illinois CS/Computing Degree Persistence for Top 3 
figure_DDP(metric_col_topThree_cs_persist)
figure_DDT(metric_col_topThree_cs_persist)
### Illinois CS/Computing Degree Conferral for Top 3 
figure_DDP(metric_col_topThree_cs_confer)
figure_DDT(metric_col_topThree_cs_confer)

## access
### Illinois CS/Computing Degree Enrollment 
figure_DDP(metric_col_cs_enrol)
figure_DDT(metric_col_cs_enrol)
### Illinois Immediate College Enrollment Rates 
figure_DDP(metric_col_imdEnrol)
figure_DDT(metric_col_imdEnrol)

# emp      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## proficiency
### Chicago MSA tech employee demographics
figure_DDP(metric_emp_techJob)
figure_DDT(metric_emp_techJob)

## excellence
### Chicago MSA tech employee demographics
figure_DDP(metric_emp_techJob_topThree)
figure_DDT(metric_emp_techJob_topThree)