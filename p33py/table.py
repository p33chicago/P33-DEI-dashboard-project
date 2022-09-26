def table(metric):
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
