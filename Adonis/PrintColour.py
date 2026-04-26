import math, random
from typing import Any

from . import utils
from . import Ansi
from Adonis.ReturnColour import ReturnColour

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
def PrintColour(colour:str, message: str) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    colourChoice: str = colour[0].upper() + colour[1:]

    match colourChoice:
        case "Rainbow":
            messageLength = len(message)
            for i in range(messageLength):
                r, g, b = utils._rainbow(i)
                print(f"\033[38;2;{r};{g};{b}m{message[i]}\033[0m{Ansi.reset}")
            
        case "Empty":
            print(message)
        case _:
            colourPicked:str = Ansi.colour[colourChoice]
            print(f"{colourPicked}{message}{Ansi.reset}")
	


def Print(message :str ) :
	"""
    Randomly choose a colour for you from: Black, Red, Green, Yellow, Blue, Purple, Cyan, White and prints it
    """
	randomIndex = random.randint(0, len(Ansi.colour))

	keys = Ansi.colour.keys()
	
	colourChoice:str = Ansi.colour[keys[randomIndex]] # type: ignore

	PrintColour(colourChoice, message)


def PrintError(message: str) :
	"""
    Uses the default colour of red - if you would like to determin you PrintError Colour use the function PrintColour instead
    """
	PrintColour("Red", message)


def PrintInfo(message :str ) :
	"""
    Uses the default colour of Green- if you would like to determin you PrintError Colour use the function PrintColour instead
    """
	
	PrintColour("Green", message)


def PrintWarning(message :str ) :
    """
    This ignores warnings from a malformed message, to be used quickly when the message will be known prior to use to be safe!
    """

    PrintColour("Yellow", message)

def PrintTable(m: dict[Any, Any], keyColour: str="Blue", itemColour: str="Green") :
    """
    Prints any table that is passed into it - currently underdevelopment looking into how this could be more safely implimented
    Pass in a map of any values and returns a printed table of the key / values
    """

    if keyColour not in Ansi.colour.keys():
         keyColour = "Blue"
        
    if itemColour not in Ansi.colour.keys():
         itemColour = "Green"

    for k, v in m.items():
         print(f"{ReturnColour(keyColour, k)}: {ReturnColour(itemColour, v)}")
	
@utils.alias_spelling
def PrintRGBColour(r:int , g:int , b: int, message:str ) :
    """
    Options: r, g, b have to be 0 or bigger and under 255
    Can error if the values are not the right size
    """

    print(f"\033[38;2;{r};{g};{b}m{message}\033[0m{Ansi.reset}")


def PrintBold(colourChoice:str, message:str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    
    colourPicked :str = Ansi.bold[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
        utils._unacceptableColour(colourChoice)

    print(f"{colourPicked}{message}{Ansi.reset}")


def PrintUnderline(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    
    colourPicked :str = Ansi.underline[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
          utils._unacceptableColour(colourChoice)


    print(f"{colourPicked}{message}{Ansi.reset}")


def PrintBackground(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.background[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
        utils._unacceptableColour(colourChoice)

    print(f"{colourPicked}{message}{Ansi.reset}{Ansi.reset}")

def PrintHighIntensity(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.high_Intensity[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
        utils._unacceptableColour(colourChoice)

    print(f"{colourPicked}{message}{Ansi.reset}")


def PrintBoldHighIntensity(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """
    colourPicked :str = Ansi.bold_High_Intensity[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
        utils._unacceptableColour(colourChoice)

    print(f"{colourPicked}{message}{Ansi.reset}")

def PrintHighIntensityBackgrounds(colourChoice:str, message :str ) :
    """
    Options: Black, Red, Green, Yellow, Blue, Purple, Cyan, White
    Can error if colour not found
    """

    colourPicked :str = Ansi.bold_High_Intensity[colourChoice[0].upper()+colourChoice[1:]]
    if not utils._checkColourInList(colourPicked): 
        utils._unacceptableColour(colourChoice)

    print(f"{colourPicked}{message}{Ansi.reset}")
	