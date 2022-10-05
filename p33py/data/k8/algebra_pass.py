from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                              'metric_k8_algebra_pass',
                                              'proficiency',
                                              'k8',
                                                    0.33,
                                              '2021___city_chi___k8_8th___math_algebra_pass___cps',
                                              '2021___usa___k8_8th___math_algebra_pass',
                                              '2017___city_chi___k8_8th___math_algebra_enrol___cps',
                                              '2017___usa___k8_8th___math_algebra_enrol')
