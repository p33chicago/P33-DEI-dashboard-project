from p33py.df import df
from p33py.metrics import metric_DEI_FourG_oneScope

def calculate():
	return metric_DEI_FourG_oneScope(df,
                                             'metric_k8_magnet_enrol',
                                             'access',
                                             'k8',
                                                   0.33,
                                             '2021___city_chi___k8_total___mag_stem_enrol___cps',
                                             '2022___city_chi___k8_total___popul___cps')
