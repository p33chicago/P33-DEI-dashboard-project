from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes


def calculate():
    return metric_DEI_FourG_twoScopes(
        df,
        "metric_emp_techJob_topThree",
        "excellence",
        "emp",
        0.5,
        "2021___region_chi_msa___emp___csjob_t3",
        "2021___usa___emp___csjob_t3",
        "2022___region_chi_msa___emp___total_degree_holder",
        "2022___usa___emp___total_degree_holder",
    )
