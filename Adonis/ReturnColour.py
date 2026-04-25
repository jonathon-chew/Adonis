import math, random
from typing import Any

from . import utils
from . import Ansi

def ReturnColour(color:str, message: str) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    colourChoice: str = color[0].upper() + color[1:]

    match colourChoice:
        case "Rainbow":
            messageLength = len(message)
            for i in range(messageLength):
                r, g, b = utils._rainbow(i)
                return f"\033[38;2;{r};{g};{b}m{message[i]}\033[0m{Ansi.reset}"
            
        case "Empty":
            return message
        case _:
            colourPicked:str = Ansi.colour[colourChoice]
            return f"{colourPicked}{message}{Ansi.reset}"
	


def ReturnMessage ( message :str  ):
	"""
    Randomly choose a colour for you from: Black, Red, Green, Yellow, Blue, Purple, Cyan, White and prints it
    """
	randomIndex = random.randint(0, len(Ansi.colour))

	keys = Ansi.colour.keys()
	
	colourChoice:str = Ansi.colour[keys[randomIndex]] # type: ignore

	ReturnColour(colourChoice, message)


def ReturnError(message: str) :
	"""
    Uses the default colour of red - if you would like to determin you ReturnError Colour use the function ReturnColour instead
    """
	ReturnColour("Red", message)


def ReturnInfo(message :str ) :
	"""
    Uses the default colour of Green- if you would like to determin you ReturnError Colour use the function ReturnColour instead
    """
	
	ReturnColour("Green", message)


def ReturnWarning(message :str ) :
    """
    This ignores warnings from a malformed message, to be used quickly when the message will be known prior to use to be safe!
    """

    ReturnColour("Yellow", message)

def ReturnTable(m: dict[Any, Any], keyColour: str="Blue", itemColour: str="Green") :
    """
    Returns any table that is passed into it - currently underdevelopment looking into how this could be more safely implimented
    Pass in a map of any values and returns a printed table of the key / values
    """

    if keyColour not in Ansi.colour.keys():
         keyColour = "Blue"
        
    if itemColour not in Ansi.colour.keys():
         itemColour = "Green"

    returnString = ""
    for k, v in m.items():
         returnString += f"{ReturnColour(keyColour, k)}: {ReturnColour(itemColour, v)}\n"
    
    return returnString
	

def ReturnRGBColour(r:int , g:int , b: int, message:str ) :
    """
    Options: r, g, b have to be 0 or bigger and under 255
    Can error if the values are not the right size
    """

    return f"\033[38;2;{r};{g};{b}m{message}\033[0m{Ansi.reset}"


def ReturnBold(colourChoice:str, message:str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    
    colourPicked :str = Ansi.bold[colourChoice[0].upper()+colourChoice[1:]]

    return f"{colourPicked}{message}{Ansi.reset}"


def ReturnUnderline(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourConverted = utils.convert_colour(colourChoice)
    colourPicked :str = Ansi.underline[colourConverted]

    return f"{colourPicked}{message}{Ansi.reset}"


def ReturnBackground(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.background[colourChoice[0].upper()+colourChoice[1:]]

    return f"{colourPicked}{message}{Ansi.reset}{Ansi.reset}"

def ReturnHighIntensity(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.high_Intensity[colourChoice[0].upper()+colourChoice[1:]]

    return f"{colourPicked}{message}{Ansi.reset}"


def ReturnBoldHighIntensity(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    colourPicked :str = Ansi.bold_High_Intensity[colourChoice[0].upper()+colourChoice[1:]]

    return f"{colourPicked}{message}{Ansi.reset}"

def ReturnHighIntensityBackgrounds(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.high_Intensity_backgrounds[colourChoice[0].upper()+colourChoice[1:]]

    return f"{colourPicked}{message}{Ansi.reset}"
	

