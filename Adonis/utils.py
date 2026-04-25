import math
from . import Ansi
from . import utils

def convert_colour(colourChoice:str) -> str:
	colourPicked :str = colourChoice[0].upper()+colourChoice[1:]
	if not utils._checkColourInList(colourPicked):
		try:
			utils._unacceptableColour(colourChoice)
		except Exception as e:
			raise ValueError(e)

	return colourPicked


def _checkColourInList(colourchoice:str) -> bool :
	acceptableColours = [colour for colour in Ansi.colour.keys()]
	acceptableColours.extend(["Empty", "Rainbow"])
	return colourchoice in acceptableColours

def _unacceptableColour(color: str) -> None :
	keys = [color[k] for k in range(len(color))]	
	options= ', '.join(keys)
	raise ValueError(f"{color} isn't avaliable from the list {options} ")

def _rainbow(i: int) -> list[float] :
	f = 0.1

	# temp = int(math.Sin(f * float64(i)))
	# suffix = 127 + 128 // 255

	return [math.sin(f*i+0)*127 + 128, math.sin(f*i+2*math.pi/3)*127 + 128,	math.sin(f*i+4*math.pi/3)*127 + 128]

