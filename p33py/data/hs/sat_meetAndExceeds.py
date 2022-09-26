from p33py.df import df
from p33py.data.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                                    'metric_hs_sat_meetAndExceeds',
                                                    'proficiency',
                                                    'hs',
                                                          0.5,
                                                    '2021___city_chi___hs___sat_math_meet&exceeds___cps',
                                                    '2021___usa___col___sat_math_meet&exceeds',
                                                    '2021___city_chi___hs_SATtaker___popul___cps',
                                                    '2021___usa___hs_SATtaker___popul')
