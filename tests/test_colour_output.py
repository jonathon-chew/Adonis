import io
import unittest
from builtins import print as builtin_print
from contextlib import redirect_stdout
from unittest.mock import patch

from tests import load_adonis_modules


MODULES = load_adonis_modules()
ANSI = MODULES["Ansi"]
PRINT_COLOUR = MODULES["print_colour"]
RETURN_COLOUR = MODULES["return_colour"]

class TestReturnColour(unittest.TestCase):
    def test_return_colour_wraps_message_in_requested_escape_code(self):
        result = RETURN_COLOUR.ReturnColour("red", "Hello")
        self.assertEqual(result, f"{ANSI.colour['Red']}Hello{ANSI.reset}")

    def test_package_root_return_color_alias_matches_return_colour(self):
        self.assertEqual(MODULES["package"].ReturnColor("Blue", "Hello"), RETURN_COLOUR.ReturnColour("Blue", "Hello"))

    def test_return_colour_supports_empty_passthrough(self):
        self.assertEqual(RETURN_COLOUR.ReturnColour("Empty", "Hello"), "Hello")

    def test_return_rgb_colour_uses_true_colour_escape_sequence(self):
        result = RETURN_COLOUR.ReturnRGBColour(12, 34, 56, "RGB")
        self.assertEqual(result, f"\033[38;2;12;34;56mRGB\033[0m{ANSI.reset}")

    def test_return_table_concatenates_key_value_pairs(self):
        result = RETURN_COLOUR.ReturnTable({"name": "Adonis", "lang": "Python"})
        self.assertEqual(result, f"{RETURN_COLOUR.ReturnColour('Blue', 'name')}: {RETURN_COLOUR.ReturnColour('Green', 'Adonis')}\n{RETURN_COLOUR.ReturnColour('Blue', 'lang')}: {RETURN_COLOUR.ReturnColour('Green', 'Python')}\n")

    def test_return_bold_uses_bold_palette(self):
        result = RETURN_COLOUR.ReturnBold("Blue", "Focus")
        self.assertEqual(result, f"{ANSI.bold['Blue']}Focus{ANSI.reset}")


class TestPrintColour(unittest.TestCase):
    def capture_output(self, func, *args):
        stream = io.StringIO()
        with patch.object(PRINT_COLOUR, "print", builtin_print):
            with redirect_stdout(stream):
                func(*args)
        return stream.getvalue()

    def test_print_colour_writes_coloured_message(self):
        output = self.capture_output(PRINT_COLOUR.PrintColour, "Green", "Hello")
        self.assertEqual(output, f"{ANSI.colour['Green']}Hello{ANSI.reset}\n")

    def test_package_root_print_color_alias_matches_print_colour(self):
        output = self.capture_output(MODULES["package"].PrintColor, "Green", "Hello")
        self.assertEqual(output, f"{ANSI.colour['Green']}Hello{ANSI.reset}\n")

    def test_print_colour_supports_empty_passthrough(self):
        output = self.capture_output(PRINT_COLOUR.PrintColour, "Empty", "Plain")
        self.assertEqual(output, "Plain\n")

    def test_print_colour_respects_custom_end(self):
        output = self.capture_output(PRINT_COLOUR.PrintColour, "Green", "Hello", "")
        self.assertEqual(output, f"{ANSI.colour['Green']}Hello{ANSI.reset}")

    def test_print_error_uses_red_output(self):
        output = self.capture_output(PRINT_COLOUR.PrintError, "Problem")
        self.assertEqual(output, f"{ANSI.colour['Red']}Problem{ANSI.reset}\n")

    def test_print_info_uses_green_output(self):
        output = self.capture_output(PRINT_COLOUR.PrintInfo, "Ready")
        self.assertEqual(output, f"{ANSI.colour['Green']}Ready{ANSI.reset}\n")

    def test_print_warning_uses_yellow_output(self):
        output = self.capture_output(PRINT_COLOUR.PrintWarning, "Careful")
        self.assertEqual(output, f"{ANSI.colour['Yellow']}Careful{ANSI.reset}\n")


    ## American
    def test_print_color_writes_colored_message(self):
        output = self.capture_output(MODULES["package"].PrintColor, "Green", "Hello")
        self.assertEqual(output, f"{ANSI.colour['Green']}Hello{ANSI.reset}\n")

    def test_print_color_supports_empty_passthrough(self):
        output = self.capture_output(MODULES["package"].PrintColor, "Empty", "Plain")
        self.assertEqual(output, "Plain\n")

    def test_print_table_uses_current_padded_coloured_layout(self):
        output = self.capture_output(PRINT_COLOUR.PrintTable, {"id": "7", "name": "Adonis"})
        expected = (
            f"{RETURN_COLOUR.ReturnColour('Blue', 'id  ')}: {RETURN_COLOUR.ReturnColour('Green', '7')}\n"
            f"{RETURN_COLOUR.ReturnColour('Blue', 'name')}: {RETURN_COLOUR.ReturnColour('Green', 'Adonis')}\n"
        )
        self.assertEqual(output, expected)
