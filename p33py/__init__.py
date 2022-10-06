import os
from .theme import set_default_theme

_dirname = os.path.dirname(__file__)
csv_path = os.path.join(_dirname, "../data/df_DEI_tidy_final.csv")
set_default_theme()
