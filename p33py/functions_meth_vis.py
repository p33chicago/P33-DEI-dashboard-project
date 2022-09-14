#%%
#                         Environment settings
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
#                              FUNCTIONS
#
#%% Define the metrics function (two scopes)
# This metric function generates a new dataset contained the value of metricOne/PopulaitonOne
# and the value of metricTwo/PopulaitonTwo for different ethnic groups at two geographical scopes.

# define the metric funtion
def metric_DEI_twoScopes(df,metricname,dimension,stage,weight,metricOne,metricTwo,populOne,PopulTwo):
    
    ''' extract numerators '''
    df_subset = df[(df["metrics_new"] == metricOne) | (df["metrics_new"] == metricTwo) ]   
    ''' rename the value in subset dataset to subset_popul '''
    df_subset.rename(columns = {'population':'subset_popul'}, inplace = True)
    ''' extract denominators '''
    df_popul = df[(df["metrics_new"] == populOne) | (df["metrics_new"] == PopulTwo) ]
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

#%% Define the metrics function (one scope)
# This metric function generates a new dataset contained the value of metricOne/PopulaitonOne 
# for different ethnic groups at one geographical scope.

# define the metric funtion
def metric_DEI_oneScope(df,metricname,dimension,stage,weight,metricOne,populOne):
    
    ''' extract numerators '''
    df_subset = df[(df["metrics_new"] == metricOne)]   
    ''' rename the value in subset dataset to subset_popul '''
    df_subset.rename(columns = {'population':'subset_popul'}, inplace = True)
    ''' extract denominators '''
    df_popul = df[(df["metrics_new"] == populOne)]
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

#%% define the visualization function for deep diving plots (DDP)

# In Spyder, Plotly fails to select the default renderer unless explicitly specified.
# Hence in below, I specified a renderer that I wish to use.


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

#%% define the visualization function for deep diving tables (DDT)

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


#%% define the function caculates Equality index (EI)

# Define a function that caculates Equality Index using geometric means when there are 4 ethnic groups 

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

# Define a function that caculates Equality Index using geometric means when there are 4 ethnic groups 

def EI_dimensions_FourG_geomean(df_metircs_selected):
    ''' Caculate the weighted EI for each metrics'''
    df_dimension = EI_metric_FourG_geomean(df_metircs_selected)
    df_dimension_EI = df_dimension.groupby(by=['var_scope','stage','dimension']).sum('EI_metric_weighted').drop(['weight'], axis = 1)
    return df_dimension_EI

# test
test = EI_dimensions_FourG_geomean(df_metircs_CHI_wide)

#%% define the function that assign weights to dimensions of different educational stages

def assign_dim_weight (df):
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
        
    df['weight_dim'] = df.apply(assign_weight, axis = 1)
    df['weighted_EI_dim'] = df['EI_weighted']*df['weight_dim']
    
    return df


#%% define 



#%%
#                              Metrics and Variables
#
#%% select variables that are used 

var = df.metrics_new.unique()
print(var)

var_selected = [
    
# k-8 ---------------------
## math prof
                '2021___city_chi___k8_4th___math_prof&abov___cps',
                '2021___usa___k8_4th___math_prof&abov',
                '2021___city_chi___k8_8th___math_prof&abov___cps',
                '2021___usa___k8_8th___math_prof&abov',
## math adv               
                '2021___city_chi___k8_4th___math_advc___cps',
                '2021___usa___k8_4th___math_advc',
                '2021___city_chi___k8_8th___math_advc___cps',
                '2021___usa___k8_8th___math_advc',
## math algebra 
                '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                '2017___usa___k8_8th___math_algebra_enrol',               
                '2021___city_chi___k8_8th___math_algebra_pass___cps',
                '2021___usa___k8_8th___math_algebra_pass',
            
## magnet enroll                
                '2021___city_chi___k8_total___mag_stem_enrol___cps',
## internet access
                '2019___city_chi___k8_total___NOinternet_age5to17___cps',                
                '2019___usa___k8_total___NOinternet_age5to17',
## population                  
                '2022___city_chi___k8_4th___popul___cps',
                '2020___usa___k8_4th___popul',
                '2022___city_chi___k8_8th___popul___cps',
                '2020___usa___k8_8th___popul',
                '2022___city_chi___k8_total___popul___cps',
                '2022___usa___age_5to17__popul',
                '2022___city_chi___age_5to17__popul___cps',            
          
            
# high school   -----------            
## sat math exceeds
                '2021___city_chi___hs___sat_math_exceeds___cps',
                '2021___usa___col___sat_math_exceeds',
## sat math meet and exceeds
                '2021___city_chi___hs___sat_math_meet&exceeds___cps',
                '2021___usa___col___sat_math_meet&exceeds',
## ap cs               
                '2021___city_chi___hs___apcs_score3/4',
                '2021___usa___hs___apcs_score3/4',
                '2021___city_chi___hs___apcs_score5___cps',
                '2021___usa___hs___apcs_score5',
                '2021___state_il___hs___apcs_enrol',
                '2021___usa___hs___apcs_enrol',
## magnet enrol
                '2021___city_chi___hs___mag_enrol___cps',
## cs interest
                '2021___city_chi___hs___cs_interested___cps',
## adv math ?????? TBC
                '2017___city_chi___hs___math_advc___cps',
                '2017___usa___hs___math_advc_enroll',
## population
                '2021___city_chi___hs_SATtaker___popul___cps',
                '2021___usa___hs_SATtaker___popul',
                '2021___city_chi___hs_apcs___popul___cps',
                '2021___usa___hs_apcs___popul',
                '2022___city_chi___hs_total___popul___cps',
                '2020___usa___hs_total___popul',

# College -----------------
## CS confer
                '2021___state_il___col___cs_confer',
                '2021___usa___col___cs_confer',
## CS enrol                
                '2021___state_il___col___cs_enrol',
                '2021___usa___col___cs_enrol',              
## T3 cs enrol
                '2021___state_il___col___t3_cs_enrol',
                '2021___usa___col___t3_cs_enrol',                
## T3 cs confer
                '2021___state_il___col___t3_cs_confer',
                '2021___usa___col___t3_cs_confer',
## hs grads population              
                '2021___state_il___hs___total_grad',
                '2022___usa___hs_grads___popul',  

## immediate enrol
                '2021___state_il___col___immediate_enrol',
                '2021___usa___col___immediate_enrol',
                
## population             
                '2022___state_il___col___total_enrol',
                '2021___usa___col___total_enrol',
                '2020___state_il___col___total_confer',
                '2021___usa___col___total_confer', 
## t3 population
                '2021___state_il___col___t3_enrol',
                '2021___usa___col___t3_enrol',                  
                '2021___state_il___col___t3_confer',
                '2021___usa___col___t3_confer',
                '2020___state_il___hs_grads___popul',
                '2022___usa___hs_grads___popul',
                
                
# employement --------------
## tech job
                '2021___region_chi_msa___emp___csjob_t11_age19to24',
                '2021___usa___emp___csjob_t11_age19to24',
                '2022___region_chi_msa___emp___total_degree_holder',
                '2022___usa___emp___total_degree_holder',
## top3 tech jobs
                '2021___region_chi_msa___emp___csjob_t3',
                '2021___usa___emp___csjob_t3'
]

#%% Prepare a extracted dataset 
# pick interested ethnic groups
## create a new dataset contained metrics presented in the last section  
df_clean = df[df.metrics_new.isin(var_selected)]
## consider metrics with counting numbers only. no proportion
df_clean = df_clean[(df_clean['var_type'] == 'count')]


## focus on black, hispanic, white and asian ethnic individual groups 
df_clean_fourGroups = df_clean[(df_clean['var_ethnic'] != "all") &
   (df_clean['var_ethnic'] != "black_hispanic") &
   (df_clean['var_ethnic'] != "white_asian")
   ]

#%% create interested metrics datasets using metric functons above

# K-8 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Proficiency
metric_k4_math_profAndAbove = metric_DEI_twoScopes(df_clean_fourGroups,
                                                   'metric_k4_math_profAndAbove',
                                                   'proficiency',
                                                   'k8',
                                                   0.33,
                                                   '2021___city_chi___k8_4th___math_prof&abov___cps',  # numerators for city of chicago
                                                   '2021___usa___k8_4th___math_prof&abov', # numerators for US
                                                   '2022___city_chi___k8_4th___popul___cps', # denominators for city of chicago
                                                   '2020___usa___k8_4th___popul') # denominators for US 

metric_k8_math_profAndAbove = metric_DEI_twoScopes(df_clean_fourGroups,
                                                   'metric_k8_math_profAndAbove',
                                                   'proficiency',
                                                   'k8',
                                                   0.33,
                                                   '2021___city_chi___k8_8th___math_prof&abov___cps',
                                                   '2021___usa___k8_8th___math_prof&abov',
                                                   '2022___city_chi___k8_8th___popul___cps',
                                                   '2020___usa___k8_8th___popul') 

metric_k8_algebra_pass = metric_DEI_twoScopes(df_clean_fourGroups,
                                              'metric_k8_algebra_pass',
                                              'proficiency',
                                              'k8',
                                              0.33,
                                              '2021___city_chi___k8_8th___math_algebra_pass___cps',
                                              '2021___usa___k8_8th___math_algebra_pass',
                                              '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                                              '2017___usa___k8_8th___math_algebra_enrol') 

## Excellence
metric_k4_math_adv = metric_DEI_twoScopes(df_clean_fourGroups,
                                          'metric_k4_math_adv',
                                          'excellence',
                                          'k8',
                                          0.5,
                                          '2021___city_chi___k8_4th___math_advc___cps', 
                                          '2021___usa___k8_4th___math_advc',
                                          '2022___city_chi___k8_4th___popul___cps',
                                          '2020___usa___k8_4th___popul') 

metric_k8_math_adv = metric_DEI_twoScopes(df_clean_fourGroups,
                                          'metric_k8_math_adv',
                                          'excellence',
                                          'k8',
                                          0.5,
                                          '2021___city_chi___k8_8th___math_advc___cps',
                                          '2021___usa___k8_8th___math_advc',
                                          '2022___city_chi___k8_8th___popul___cps',
                                          '2020___usa___k8_8th___popul') # denominators for US 

## Access
metric_k8_magnet_enrol = metric_DEI_oneScope(df_clean_fourGroups,
                                             'metric_k8_magnet_enrol',
                                             'access',
                                             'k8',
                                             0.33, 
                                             '2021___city_chi___k8_total___mag_stem_enrol___cps',
                                             '2022___city_chi___k8_total___popul___cps')

#????????????
metric_k8_algebra_enrol = metric_DEI_twoScopes(df_clean_fourGroups,
                                               'metric_k8_algebra_enrol',
                                               'access',
                                               'k8',
                                               0.33,
                                               '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                                               '2017___usa___k8_8th___math_algebra_enrol',
                                               '2022___city_chi___k8_8th___popul___cps',
                                               '2020___usa___k8_8th___popul') 

#????????????
metric_k8_noInt = metric_DEI_twoScopes(df_clean_fourGroups,
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
metric_hs_sat_meetAndExceeds = metric_DEI_twoScopes(df_clean_fourGroups,
                                                    'metric_hs_sat_meetAndExceeds',
                                                    'proficiency',
                                                    'hs',
                                                    0.5,
                                                    '2021___city_chi___hs___sat_math_meet&exceeds___cps',
                                                    '2021___usa___col___sat_math_meet&exceeds',
                                                    '2021___city_chi___hs_SATtaker___popul___cps',
                                                    '2021___usa___hs_SATtaker___popul')

metric_hs_apcs_aboveThree = metric_DEI_twoScopes(df_clean_fourGroups,
                                                 'metric_hs_apcs_aboveThree',
                                                 'proficiency',
                                                 'hs',
                                                 0.5,
                                                 '2021___city_chi___hs___apcs_score3/4',
                                                 '2021___usa___hs___apcs_score3/4',
                                                 '2021___city_chi___hs_apcs___popul___cps',
                                                 '2021___usa___hs_apcs___popul')


## Excellence
metric_hs_sat_exceeds = metric_DEI_twoScopes(df_clean_fourGroups,
                                             'metric_hs_sat_exceeds',
                                             'excellence',
                                             'hs',
                                             0.5,
                                             '2021___city_chi___hs___sat_math_exceeds___cps',
                                             '2021___usa___col___sat_math_exceeds',
                                             '2021___city_chi___hs_SATtaker___popul___cps',
                                             '2021___usa___hs_SATtaker___popul')

metric_hs_apcs_five = metric_DEI_twoScopes(df_clean_fourGroups,
                                           'metric_hs_apcs_five',
                                           'excellence',
                                           'hs',
                                           0.5,
                                           '2021___city_chi___hs___apcs_score5___cps',
                                           '2021___usa___hs___apcs_score5',
                                           '2021___city_chi___hs_apcs___popul___cps',
                                           '2021___usa___hs_apcs___popul')

## Access
metric_hs_apcs_enrol = metric_DEI_twoScopes(df_clean_fourGroups,
                                            'metric_hs_apcs_enrol',
                                            'access',
                                            'hs',
                                            0.25,
                                            '2021___city_chi___hs_apcs___popul___cps',
                                            '2021___usa___hs_apcs___popul',
                                            '2022___city_chi___hs_total___popul___cps',
                                            '2020___usa___hs_total___popul')

metric_hs_magnet_enrol = metric_DEI_oneScope(df_clean_fourGroups,
                                             'metric_hs_magnet_enrol',
                                             'access',
                                             'hs',
                                             0.25,
                                             '2021___city_chi___hs___mag_enrol___cps',
                                             '2022___city_chi___hs_total___popul___cps')

metric_hs_CSInterested = metric_DEI_oneScope(df_clean_fourGroups,
                                             'metric_hs_CSInterested',
                                             'access',
                                             'hs',
                                             0.25,
                                             '2021___city_chi___hs___cs_interested___cps',
                                             '2022___city_chi___hs_total___popul___cps')

#????????????
metric_hs_advMath_enrol = metric_DEI_twoScopes(df_clean_fourGroups,
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
metric_col_cs_persist = metric_DEI_twoScopes(df_clean_fourGroups,
                                             'metric_col_cs_persist',
                                             'proficiency',
                                             'col',
                                             0.5,
                                             '2021___state_il___col___cs_confer',
                                             '2021___usa___col___cs_confer',
                                             '2021___state_il___col___cs_enrol',
                                             '2021___usa___col___cs_enrol')

metric_col_cs_confer = metric_DEI_twoScopes(df_clean_fourGroups,
                                            'metric_col_cs_confer',
                                            'proficiency',
                                            'col',
                                            0.5,
                                            '2021___state_il___col___cs_confer',
                                            '2021___usa___col___cs_confer',
                                            '2020___state_il___col___total_confer',
                                            '2021___usa___col___total_confer')

## Excellence
metric_col_topThree_cs_enrol = metric_DEI_twoScopes(df_clean_fourGroups,
                                                    'metric_col_topThree_cs_enrol',
                                                    'excellence',
                                                    'col',
                                                    0.33,
                                                    '2021___state_il___col___t3_cs_enrol',
                                                    '2021___usa___col___t3_cs_enrol',
                                                    '2021___state_il___col___t3_enrol',
                                                    '2021___usa___col___t3_enrol')

metric_col_topThree_cs_persist = metric_DEI_twoScopes(df_clean_fourGroups,
                                                      'metric_col_topThree_cs_persist',
                                                      'excellence',
                                                      'col',
                                                      0.33,
                                                      '2021___state_il___col___t3_cs_confer',
                                                      '2021___usa___col___t3_cs_confer',
                                                      '2021___state_il___col___t3_cs_enrol',
                                                      '2021___usa___col___t3_cs_enrol')

metric_col_topThree_cs_confer = metric_DEI_twoScopes(df_clean_fourGroups,
                                                     'metric_col_topThree_cs_confer',
                                                     'excellence',
                                                     'col',
                                                     0.33,
                                                     '2021___state_il___col___t3_cs_confer', 
                                                     '2021___usa___col___t3_cs_confer',
                                                     '2021___state_il___col___t3_confer',
                                                     '2021___usa___col___t3_confer')

## Access
metric_col_cs_enrol = metric_DEI_twoScopes(df_clean_fourGroups,
                                           'metric_col_cs_enrol',
                                           'access',
                                           'col',
                                           0.5,
                                           '2021___state_il___col___cs_enrol',
                                           '2021___usa___col___cs_enrol',
                                           '2022___state_il___col___total_enrol',
                                           '2021___usa___col___total_enrol')

metric_col_imdEnrol = metric_DEI_twoScopes(df_clean_fourGroups,
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
metric_emp_techJob = metric_DEI_twoScopes(df_clean_fourGroups,
                                          'metric_emp_techJob',
                                          'proficiency',
                                          'emp',
                                          0.5,
                                          '2021___region_chi_msa___emp___csjob_t11_age19to24',
                                          '2021___usa___emp___csjob_t11_age19to24',
                                          '2022___region_chi_msa___emp___total_degree_holder',
                                          '2022___usa___emp___total_degree_holder')

## Excellence
metric_emp_techJob_topThree =  metric_DEI_twoScopes(df_clean_fourGroups,
                                                    'metric_emp_techJob_topThree',
                                                    'excellence',
                                                    'emp',
                                                    0.5,
                                                    '2021___region_chi_msa___emp___csjob_t3',
                                                    '2021___usa___emp___csjob_t3',
                                                    '2022___region_chi_msa___emp___total_degree_holder',
                                                    '2022___usa___emp___total_degree_holder')


## testing 

# df_subset = df[(df["metrics_new"] == '2021___region_chi_msa___emp___csjob_t11_age19to24')]

# df_subset.rename(columns = {'population':'subset_popul'}, inplace = True)

# df_popul = df[(df["metrics_new"] == '2022___region_chi_msa___emp___total_degree_holder') | (df["metrics_new"] == '2022___usa___emp___total_degree_holder')]

# df_merge = pd.merge(df_subset, df_popul,  how = 'left', left_on=['var_scope','var_ethnic'], right_on = ['var_scope','var_ethnic'])

# df_merge['metric_value'] = (df_merge['subset_popul'] / df_merge['population'])



#%% create a dataframe of metric values for city of Chicago, Illinois and MSA

df_metircs = pd.concat([metric_k4_math_profAndAbove,
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
                            metric_emp_techJob_topThree])
# select data from one geo
df_metircs_CHI = df_metircs[(df_metircs['var_scope']!='usa')]
df_metircs_CHI_slim = df_metircs_CHI.drop(['metrics_new','subset_popul','population'], axis = 1)
df_metircs_CHI_wide = pd.pivot(df_metircs_CHI_slim, index=['metric_name','var_scope','weight','dimension','stage'], columns='var_ethnic', values='metric_value')
df_metircs_CHI_wide.reset_index(inplace=True)


#%% caculate EI of each metrics
df_metircs_CHI_EI = EI_metric_FourG_geomean(df_metircs_CHI_wide)
df_metircs_CHI_EI.columns
#%% caculate EI of each dimensions at educational stages
test = df_metircs_CHI_EI.groupby(by=['var_scope','stage','dimension']).sum('EI_metric_weighted').drop(['weight'], axis = 1)
test.reset_index(inplace=True)

#%% caculate EI of each educational stages

# assigning weights to each dimensions
test2 = assign_dim_weight(test)
test2 = test.groupby(by=['stage']).sum('EI_weighted').drop(['weight'], axis = 1)




