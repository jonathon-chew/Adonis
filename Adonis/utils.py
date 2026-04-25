import math
from . import Ansii

def Colour(option: str, color: str, message:str ):
	"""
	Options: "Colour", "Color", "Bold", "Underline", "Background", "High_intensity", "Bold_high_intesity", "High_Intensity_backgrounds"
    Colours: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    """

	acceptableOptions = ["Colour", "Color", "Bold", "Underline", "Background", "High_intensity", "Bold_high_intesity", "High_Intensity_backgrounds"]
	acceptableColours = ["Black", "Red", "Green", "Yellow", "Blue", "Purple", "Cyan", "White", "Rainbow"]

	optionChoice = option.replace(" ", "_")
	colourChoice = color[0].upper() + color[1:]

	allAcceptableOptions = ', '.join(acceptableOptions)
	allAcceptableColours = ', '.join(acceptableColours)

	if option not in acceptableOptions :
		raise ValueError(f"unable to recognise option: {optionChoice}  the options are: {allAcceptableOptions} ")
	

	if colourChoice not in acceptableColours :
		raise ValueError(f"unfortunately {colourChoice}  isn't a useable colour the options are: {allAcceptableColours} ")
	

	command= optionChoice.lower()

	if command == "color" or command == "colour" or command == "text" or command == "rune" :
		if colourChoice == "Rainbow" :
			messageLength = len(message)
			for i in range(messageLength):
				r, g, b = rainbow(i)
				print(f"\033[38;2;{r};{g};{b} m{message[i]}\033[0m{Ansii.reset}")
			
		else:
			colourOfOptionPicked = Ansii.colour[colourChoice]
			print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		
		return
	

	if command == "bold" :
		colourOfOptionPicked = Ansii.bold[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	

	if command == "underline" :
		colourOfOptionPicked = Ansii.underline[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	

	if command == "background" :
		colourOfOptionPicked = Ansii.background[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	

	if command == "high_intensity" :
		colourOfOptionPicked = Ansii.high_Intensity[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	

	if command == "bold_high_intensity" :
		colourOfOptionPicked = Ansii.bold_High_Intensity[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	

	if command == "high_intensity_backgrounds" :
		colourOfOptionPicked = Ansii.high_Intensity_backgrounds[colourChoice]
		print(f"{colourOfOptionPicked} {message} {Ansii.reset}")
		return
	
	return


def checkColourInList(colourchoice:str) -> bool :
	acceptableColours = ["Black", "Red", "Green", "Yellow", "Blue", "Purple", "Cyan", "White", "Rainbow", "Empty"]
	return colourchoice in acceptableColours


def unacceptableColour(color: str) -> None :
	keys = [color[k] for k in range(len(color))]	
	options= ', '.join(keys)
	raise ValueError("{}  isn't avaliable from the list {} ", color, options)

def rainbow(i: int) -> list[float] :
	f = 0.1

	# temp = int(math.Sin(f * float64(i)))
	# suffix = 127 + 128 // 255

	return [math.sin(f*i+0)*127 + 128, math.sin(f*i+2*math.pi/3)*127 + 128,	math.sin(f*i+4*math.pi/3)*127 + 128]

