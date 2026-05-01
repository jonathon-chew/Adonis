from .PrintColour import *
from .ReturnColour import *
from . import utils
from . import Ansi

from Adonis import PrintColour, PrintColor # type: ignore
from Adonis import ReturnColour, ReturnColor # type: ignore

from Adonis.PrintColour import PrintColour, PrintColor # type: ignore
from Adonis.ReturnColour import ReturnColour, ReturnColor # type: ignore


__all__ = ["PrintError","PrintInfo","PrintWarning","PrintTable","PrintRGBColour","PrintBold","PrintUnderline","PrintBackground","PrintHighIntensity","PrintBoldHighIntensity","PrintHighIntensityBackgrounds", "ReturnError","ReturnInfo","ReturnWarning","ReturnTable","ReturnRGBColour","ReturnBold","ReturnUnderline","ReturnBackground","ReturnHighIntensity","ReturnBoldHighIntensity","ReturnHighIntensityBackgrounds", "PrintColor", "ReturnColor"]