import pandas as pd
from pandas import DataFrame


def combiner_CHIAndIL(*df_metric: list[DataFrame]) -> DataFrame:
    """Returns individual metrics int a dataframe with metrics from distinct geographic scope"""

    df_metrics_combined = pd.concat(df_metric)

    # select data from chicago/IL
    df_metrics_CHI = df_metrics_combined[(df_metrics_combined["var_scope"] != "usa")]
    # drop populations, keep only proportions (metric values)
    df_metrics_CHI_slim = df_metrics_CHI.drop(
        ["metrics_new", "subset_popul", "population"], axis=1
    )
    # transfer dataframe structure from long to wide for later manipualation
    df_metrics_CHI_wide = pd.pivot(
        df_metrics_CHI_slim,
        index=["metric_name", "var_scope", "weight", "dimension", "stage"],
        columns="var_ethnic",
        values="metric_value",
    )
    # transform index to vairables for later process
    df_metrics_CHI_wide.reset_index(inplace=True)

    return df_metrics_CHI_wide


####### added on Oct. 12
def combiner_US(*df_metric: list[DataFrame]) -> DataFrame:
    """Returns individual metrics int a dataframe with metrics from distinct geographic scope"""

    df_metrics_combined = pd.concat(df_metric)

    # select data from chicago/IL
    df_metrics_USA = df_metrics_combined[(df_metrics_combined["var_scope"] == "usa")]
    # drop populations, keep only proportions (metric values)
    df_metrics_USA_slim = df_metrics_USA.drop(
        ["metrics_new", "subset_popul", "population"], axis=1
    )
    # transfer dataframe structure from long to wide for later manipualation
    df_metrics_USA_wide = pd.pivot(
        df_metrics_USA_slim,
        index=["metric_name", "var_scope", "weight", "dimension", "stage"],
        columns="var_ethnic",
        values="metric_value",
    )
    # transform index to vairables for later process
    df_metrics_USA_wide.reset_index(inplace=True)

    return df_metrics_USA_wide


####### added on Oct. 12


def EI_metric_FourG_geomean(df_metrics_selected: DataFrame) -> DataFrame:
    """Returns Equality index (EI) of each metric using geometric mean when there are 4 ethnic groups"""

    # Copy input to avoid updating original dataframe
    df_metrics_selected = df_metrics_selected.copy()

    # caculate geometric mean of proportions of 4 ethnic groups
    df_metrics_selected["avg"] = (
        df_metrics_selected["black"]
        * df_metrics_selected["hispanic"]
        * df_metrics_selected["white"]
        * df_metrics_selected["asian"]
    ) ** (0.25)
    # caculate the Inequality Index
    """ II """
    df_metrics_selected["II_metric"] = (
        abs(df_metrics_selected["black"] - df_metrics_selected["avg"])
        + abs(df_metrics_selected["hispanic"] - df_metrics_selected["avg"])
        + abs(df_metrics_selected["white"] - df_metrics_selected["avg"])
        + abs(df_metrics_selected["asian"] - df_metrics_selected["avg"])
    ) / (4 * df_metrics_selected["avg"])
    """ II sqrt"""
    df_metrics_selected["II_metric_SQRT"] = df_metrics_selected["II_metric"] ** 0.5
    # scaling
    """ find the most inequal metrics and use its II_SQRT as benchmark"""
    df_metrics_selected["II_metric_SQRT_MAX"] = df_metrics_selected[
        "II_metric_SQRT"
    ].max()
    """ Transform II_SQURT to EI, the equality index"""
    df_metrics_selected["EI_metric"] = 100 - (
        (
            df_metrics_selected["II_metric_SQRT"]
            / df_metrics_selected["II_metric_SQRT_MAX"]
        )
        * 100
    )
    """ Caculate the weighted EI"""
    df_metrics_selected["EI_metric_weighted"] = (
        df_metrics_selected["EI_metric"] * df_metrics_selected["weight"]
    )

    return df_metrics_selected


def EI_indicators_FourG_geomean(df_metrics_selected: DataFrame) -> DataFrame:
    """Returns Equality Index of dimensions using geometric mean when there are 4 ethnic groups"""

    # Copy input to avoid updating original dataframe
    df_metrics_selected = df_metrics_selected.copy()

    """ Caculate the weighted EI for each metrics"""
    df_metrics = EI_metric_FourG_geomean(df_metrics_selected)
    """ caculate the EI for each dimensions """
    df_dimension_EI = (
        df_metrics.groupby(by=["var_scope", "stage", "dimension"])
        .sum("EI_metric_weighted")
        .drop(["weight"], axis=1)
    )
    """ Rename the recaculated column """
    df_dimension_EI.rename(
        columns={"EI_metric_weighted": "EI_dim_weighted"}, inplace=True
    )
    """ Transform indexes to variables """
    df_dimension_EI.reset_index(inplace=True)
    """ Drop redundant columns """
    df_dimension_EI = df_dimension_EI.loc[
        :, ["var_scope", "stage", "dimension", "EI_dim_weighted"]
    ]

    return df_dimension_EI


def EI_stages_FourG_geomean(df_metrics_selected: DataFrame) -> DataFrame:
    """Returns Equality Index of life stages using geometric mean when there are 4 ethnic groups"""

    # Copy input to avoid updating original dataframe
    df_metrics_selected = df_metrics_selected.copy()

    """ Caculate the weighted EI for each metrics"""
    df_indicators_EI = EI_indicators_FourG_geomean(df_metrics_selected)

    """ define the function that generates weighted EI for each dimensions"""

    def generates_dim_weight(df_dim_EI):

        """assgin weights to each dimensions"""

        def assign_weight(df):
            # k8
            if (df["stage"] == "k8") & (df["dimension"] == "access"):
                return 0.3
            elif (df["stage"] == "k8") & (df["dimension"] == "proficiency"):
                return 0.3
            elif (df["stage"] == "k8") & (df["dimension"] == "excellence"):
                return 0.2
            # hs
            elif (df["stage"] == "hs") & (df["dimension"] == "access"):
                return 0.2
            elif (df["stage"] == "hs") & (df["dimension"] == "proficiency"):
                return 0.4
            elif (df["stage"] == "hs") & (df["dimension"] == "excellence"):
                return 0.4
            # col
            elif (df["stage"] == "col") & (df["dimension"] == "access"):
                return 0.2
            elif (df["stage"] == "col") & (df["dimension"] == "proficiency"):
                return 0.4
            elif (df["stage"] == "col") & (df["dimension"] == "excellence"):
                return 0.4
            # emp
            elif (df["stage"] == "emp") & (df["dimension"] == "access"):
                return 0.5
            elif (df["stage"] == "emp") & (df["dimension"] == "proficiency"):
                return 0.5
            elif (df["stage"] == "emp") & (df["dimension"] == "excellence"):
                return 0.5

        df_dim_EI["weight_dim"] = df_dim_EI.apply(assign_weight, axis=1)
        df_dim_EI["weighted_EI_dim"] = (
            df_dim_EI["EI_dim_weighted"] * df_dim_EI["weight_dim"]
        )
        df_dim_EI_weighted = df_dim_EI

        return df_dim_EI_weighted

    """ Use the function above to generate a dataframe with weighted EI of dimensions"""
    df_dimension_EI_weighted = generates_dim_weight(df_indicators_EI)

    """ caculate the EI of each educational stages"""
    df_stage_EI = (
        df_dimension_EI_weighted.groupby(by=["stage", "var_scope"])
        .sum("weighted_EI_dim")
        .drop(["weight_dim"], axis=1)
    )

    """ Rename the recaculated column """
    df_stage_EI.rename(columns={"weighted_EI_dim": "weighted_EI_stage"}, inplace=True)

    """ Transform indexes to variables """
    df_stage_EI.reset_index(inplace=True)

    """ Drop redundant columns """
    df_stage_EI = df_stage_EI.loc[:, ["weighted_EI_stage", "stage"]]

    return df_stage_EI
