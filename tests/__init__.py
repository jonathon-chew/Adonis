import importlib
import sys


def load_adonis_modules():
    """Import the package in the order expected by the current codebase."""
    ansii = importlib.import_module("Adonis.Ansii")

    # The library uses absolute imports internally, so the tests provide the
    # aliases it expects without modifying the package code.
    sys.modules["Ansii"] = ansii
    main = importlib.import_module("Adonis.__main__")
    sys.modules["__main__"].rainbow = main.rainbow

    return {
        "ansii": ansii,
        "main": main,
        "print_colour": importlib.import_module("Adonis.PrintColour"),
        "return_colour": importlib.import_module("Adonis.ReturnColour"),
    }
