from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                            'metric_hs_apcs_enrol',
                                            'access',
                                            'hs',
                                                  0.25,
                                            '2021___city_chi___hs_apcs___popul___cps',
                                            '2021___usa___hs_apcs___popul',
                                            '2022___city_chi___hs_total___popul___cps',
                                            '2020___usa___hs_total___popul')
