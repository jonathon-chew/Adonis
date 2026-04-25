import importlib
import sys
from pathlib import Path


def load_adonis_modules():
    """Import the package using the current package-relative layout."""
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    package = importlib.import_module("Adonis")
    ansi = importlib.import_module("Adonis.Ansi")
    utils = importlib.import_module("Adonis.utils")

    return {
        "package": package,
        "Ansi": ansi,
        "utils": utils,
        "print_colour": importlib.import_module("Adonis.PrintColour"),
        "return_colour": importlib.import_module("Adonis.ReturnColour"),
    }
