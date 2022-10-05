from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes

def calculate():
    return metric_DEI_FourG_twoScopes(df,
                                            'metric_col_cs_confer',
                                            'proficiency',
                                            'col',
                                                  0.5,
                                            '2021___state_il___col___cs_confer',
                                            '2021___usa___col___cs_confer',
                                            '2020___state_il___col___total_confer',
                                            '2021___usa___col___total_confer')
