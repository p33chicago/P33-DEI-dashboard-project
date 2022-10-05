from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                                         'metric_k8_math_profAndAbove',
                                                         'proficiency',
                                                         'k8',
                                                         0.33,
                                                         '2021___city_chi___k8_8th___math_prof&abov___cps',
                                                         '2021___usa___k8_8th___math_prof&abov',
                                                         '2022___city_chi___k8_8th___popul___cps',
                                                         '2020___usa___k8_8th___popul')
