from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes


def calculate():
    return metric_DEI_FourG_twoScopes(
        df,
        "metric_k4_math_adv",
        "excellence",
        "k8",
        0.5,
        "2021___city_chi___k8_4th___math_advc___cps",
        "2021___usa___k8_4th___math_advc",
        "2022___city_chi___k8_4th___popul___cps",
        "2020___usa___k8_4th___popul",
    )
