# Adonis

## Summary
`Adonis` is a small Python project for working with ANSI terminal colours. I built it as a lightweight utility so I could print or return coloured strings without rewriting escape sequences by hand, and it also gave me a compact space to explore simple library design, terminal formatting, and test coverage around a small public API.

## What This Project Demonstrates
- Python utility-library design around a small focused API
- separating print-based helpers from return-based helpers
- storing ANSI escape sequences in reusable palettes
- generating RGB rainbow output with a sine-wave function
- handling small formatting variants such as bold, underline, and backgrounds
- building tests around the current behavior of an existing codebase

## Current Features
- print coloured text directly with `PrintColour(...)`
- return coloured text with `ReturnColour(...)`
- support standard ANSI colours including black, red, green, yellow, blue, purple, cyan, and white
- support an `Empty` mode that returns or prints plain text
- support a `Rainbow` mode for per-character RGB colouring
- support bold, underline, background, high-intensity, and bold high-intensity variants
- support direct RGB colour formatting through `PrintRGBColour(...)` and `ReturnRGBColour(...)`
- include convenience helpers such as `PrintError(...)`, `PrintInfo(...)`, `PrintWarning(...)`, `ReturnError(...)`, `ReturnInfo(...)`, and `ReturnWarning(...)`
- include basic table-style formatting helpers with `PrintTable(...)` and `ReturnTable(...)`
- expose the main print and return helpers through the package `__init__.py`

## Behavior Notes (Current)
- **Two API styles:** `PrintColour.py` writes directly to stdout, while `ReturnColour.py` returns the ANSI-formatted string.
- **Shared helpers:** `utils.py` now holds the shared helper functions, including `Colour(...)`, `checkColourInList(...)`, `unacceptableColour(...)`, and `rainbow(...)`.
- **Colour normalization:** most colour-based functions normalize the first letter, so `"red"` and `"Red"` both resolve to `Red`.
- **Rainbow mode:** rainbow output is generated per character using the `rainbow()` helper in `utils.py`.
- **Package root imports:** `import Adonis` works, and the package root exposes the main print and return helpers. Utility helpers such as `rainbow(...)` are still imported from `Adonis.utils`.
- **Table helpers:** the table helpers currently concatenate keys and values directly rather than rendering padded columns.
- **Current implementation quirks:** the module layout is cleaner now, but there are still a few rough edges such as table formatting, partial package-root exports, and some inconsistent naming.

## How To Run

You can experiment with the library from a Python session or script by importing from either the package root or the individual modules:

```python
from Adonis import PrintInfo, ReturnColour

from Adonis.PrintColour import PrintInfo
from Adonis.ReturnColour import ReturnColour
from Adonis.utils import rainbow
```

## Examples

### Return A Formatted String

```python
from Adonis.ReturnColour import ReturnColour, ReturnBold

status = ReturnColour("Blue", "status: running")
headline = ReturnBold("Yellow", "Important")

print(status)
print(headline)
```

### Print Directly To The Terminal

```python
from Adonis.PrintColour import PrintInfo, PrintWarning, PrintRGBColour

PrintInfo("Everything is healthy")
PrintWarning("Disk usage is climbing")
PrintRGBColour(255, 120, 0, "Custom RGB message")
```

### Build A Simple Table String

```python
from Adonis.ReturnColour import ReturnTable

summary = {
    "project": "Adonis",
    "language": "Python",
}

print(ReturnTable(summary))
```

Example output:

```python
project: Adonis 
language: Python
```

## Why This Is Different

Many terminal-colour helpers are either extremely minimal or wrapped into much larger CLI frameworks. I kept this project intentionally small and direct:
- one module for printing and one for returning strings
- explicit helper functions instead of a larger abstraction layer
- support for both standard ANSI styles and direct RGB output
- a compact codebase that is easy to read through in one sitting

That makes it useful both as a practical helper and as a small example of how I approach utility-library design.

## Testing

This project uses Python's built-in `unittest` module. The tests currently cover:
- coloured string output for the return-based API
- stdout behavior for the print-based API
- convenience helpers such as error, info, and warning output
- RGB formatting helpers
- table-return behavior
- shared helper coverage for `checkColourInList(...)` and `rainbow(...)`
- direct package-import coverage for the current package layout

Run the full test suite with:

```bash
python3 -m unittest discover -s tests
```

## What I Learned

This project helped me get more comfortable with:
- keeping a utility library small without making it vague
- separating side-effecting functions from pure return-value helpers
- splitting shared helper logic into a dedicated utility module
- working with ANSI escape sequences directly
- generating simple colour effects from math rather than hard-coded values
- using tests to pin down existing behavior before refactoring

## Next Improvements

- improve validation and error messages for unsupported inputs
- make the table helpers render more clearly formatted output
- decide whether utility helpers such as `rainbow(...)` and `Print(...)` should also be exported from the package root
