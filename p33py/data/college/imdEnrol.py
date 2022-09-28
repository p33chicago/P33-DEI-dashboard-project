from p33py.df import df
from p33py.data.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                           'metric_col_imdEnrol',
                                           'access',
                                           'col',
                                                 0.5,
                                           '2021___state_il___col___immediate_enrol',
                                           '2021___usa___col___immediate_enrol',
                                           '2020___state_il___hs_grads___popul',
                                           '2022___usa___hs_grads___popul')
