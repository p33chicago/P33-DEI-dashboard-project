from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                               'metric_hs_advMath_enrol',
                                               'access',
                                               'hs',
                                                     0.25,
                                               '2017___city_chi___hs___math_advc___cps',
                                               '2017___usa___hs___math_advc_enroll',
                                               '2022___city_chi___hs_total___popul___cps',
                                               '2020___usa___hs_total___popul')
