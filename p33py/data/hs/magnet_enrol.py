from p33py.df import df
from p33py.data.metrics import metric_DEI_FourG_oneScope

def calculate():
    return metric_DEI_FourG_oneScope(df,
                                             'metric_hs_magnet_enrol',
                                             'access',
                                             'hs',
                                                   0.25,
                                             '2021___city_chi___hs___mag_enrol___cps',
                                             '2022___city_chi___hs_total___popul___cps')
