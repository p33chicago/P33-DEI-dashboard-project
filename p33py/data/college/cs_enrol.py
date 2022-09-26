from p33py.df import df
from p33py.data.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                           'metric_col_cs_enrol',
                                           'access',
                                           'col',
                                                 0.5,
                                           '2021___state_il___col___cs_enrol',
                                           '2021___usa___col___cs_enrol',
                                           '2022___state_il___col___total_enrol',
                                           '2021___usa___col___total_enrol')
