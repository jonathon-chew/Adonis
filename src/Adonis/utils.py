import math
from . import Ansi
from . import utils

def alias_spelling(func):
    name = func.__name__
    replacements = {
        "colour": "color",
        "Colour": "Color",
    }

    for old, new in replacements.items():
        if old in name:
            alias = name.replace(old, new)
            globals()[alias] = func

    return func

@alias_spelling
def convert_colour(colourChoice:str) -> str:
	colourPicked :str = colourChoice[0].upper()+colourChoice[1:]
	if not utils._checkColourInList(colourPicked):
		try:
			utils._unacceptableColour(colourChoice)
		except Exception as e:
			raise ValueError(e)

	return colourPicked

@alias_spelling
def _checkColourInList(colourchoice:str) -> bool :
	acceptableColours = [colour for colour in Ansi.colour.keys()]
	acceptableColours.extend(["Empty", "Rainbow"])
	return colourchoice in acceptableColours

def _unacceptableColour(colour: str) -> None :
	keys = [colour[k] for k in range(len(colour))]	
	options= ', '.join(keys)
	raise ValueError(f"{colour} isn't avaliable from the list {options} ")

def _rainbow(i: int) -> list[float] :
	f = 0.1

	# temp = int(math.Sin(f * float64(i)))
	# suffix = 127 + 128 // 255

	return [math.sin(f*i+0)*127 + 128, math.sin(f*i+2*math.pi/3)*127 + 128,	math.sin(f*i+4*math.pi/3)*127 + 128]

