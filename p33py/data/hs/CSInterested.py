from p33py.df import df
from p33py.metrics import metric_DEI_FourG_oneScope

def calculate():
    return metric_DEI_FourG_oneScope(df,
                                             'metric_hs_CSInterested',
                                             'access',
                                             'hs',
                                                   0.25,
                                             '2021___city_chi___hs___cs_interested___cps',
                                             '2022___city_chi___hs_total___popul___cps')
