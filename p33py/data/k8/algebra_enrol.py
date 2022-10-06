"""Ratio of students enrolled in algebra to all students for each race"""

from p33py.df import df
from p33py.metrics import metric_DEI_FourG_twoScopes


def calculate():
    return metric_DEI_FourG_twoScopes(
        df,
        "metric_k8_algebra_enrol",
        "access",
        "k8",
        0.33,
        "2017___city_chi___k8_8th___math_algebra_enrol___cps",
        "2017___usa___k8_8th___math_algebra_enrol",
        "2022___city_chi___k8_8th___popul___cps",
        "2020___usa___k8_8th___popul",
    )
