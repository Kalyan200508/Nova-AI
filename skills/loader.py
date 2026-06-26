import importlib
import pkgutil
import skills


def load_skills():

    for _, module_name, _ in pkgutil.iter_modules(skills.__path__):

        if module_name in (
            "__init__",
            "base",
            "registry",
            "loader",
        ):
            continue

        importlib.import_module(f"skills.{module_name}")