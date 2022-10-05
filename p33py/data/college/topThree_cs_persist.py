from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                                      'metric_col_topThree_cs_persist',
                                                      'excellence',
                                                      'col',
                                                            0.33,
                                                      '2021___state_il___col___t3_cs_confer',
                                                      '2021___usa___col___t3_cs_confer',
                                                      '2021___state_il___col___t3_cs_enrol',
                                                      '2021___usa___col___t3_cs_enrol')
