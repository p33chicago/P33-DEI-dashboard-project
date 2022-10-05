from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                       'metric_k8_noInt',
                                       'access',
                                       'k8',
                                             0.33,
                                       '2019___city_chi___k8_total___NOinternet_age5to17___cps',
                                       '2019___usa___k8_total___NOinternet_age5to17',
                                       '2022___city_chi___age_5to17__popul___cps',
                                       '2022___usa___age_5to17__popul') # denominators for US
