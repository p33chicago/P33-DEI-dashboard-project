import glob
import importlib
import inspect
import os

from pandas import DataFrame

from p33py.domain import lifestages

data = []
base_dir = os.path.dirname(__file__)
package_prefix = __name__.split(".")[0:-1]
package_prefix = ".".join(package_prefix)

for lifestage in lifestages:
    path = f"{base_dir}/{lifestage.name}/*.py"
    files = glob.glob(path)
    for module_path in files:
        datum_name = inspect.getmodulename(module_path)
        module_name = f"{package_prefix}.{lifestage.name}.{datum_name}"
        module = importlib.import_module(module_name)
        data += [[lifestage.name, datum_name, module_name, module.__doc__]]
index = DataFrame(data, columns=["lifestage", "datum_name", "module", "description"])
