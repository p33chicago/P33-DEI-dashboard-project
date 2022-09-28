from p33py.df import df

from p33py.data.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                                   'metric_k4_math_profAndAbove',
                                                   'proficiency',
                                                   'k8',
                                                         0.33,
                                                   '2021___city_chi___k8_4th___math_prof&abov___cps',  # numerators for city of chicago
                                                   '2021___usa___k8_4th___math_prof&abov',  # numerators for US
                                                   '2022___city_chi___k8_4th___popul___cps',  # denominators for city of chicago
                                                   '2020___usa___k8_4th___popul') # denominators for US
