import importlib

from p33py.equity_indices import combiner_CHIAndIL, EI_metric_FourG_geomean, EI_indicators_FourG_geomean, \
    EI_stages_FourG_geomean
from p33py.data.index import index

all_metrics = []
for module_name in list(index['module']):
    module = importlib.import_module(module_name)
    all_metrics.append(module.calculate())

# print(all_metrics)

metrics_CHI = combiner_CHIAndIL(*all_metrics)
EI_metric_CHI = EI_metric_FourG_geomean(metrics_CHI)
EI_indicators_CHI = EI_indicators_FourG_geomean(metrics_CHI)
EI_lifestages_CHI = EI_stages_FourG_geomean(metrics_CHI)
