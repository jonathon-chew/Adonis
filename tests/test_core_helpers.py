import math
import unittest

from tests import load_adonis_modules

MODULES = load_adonis_modules()
PACKAGE = MODULES["package"]
UTILS = MODULES["utils"]

class TestCoreHelpers(unittest.TestCase):
    def test_package_import_exposes_primary_helpers(self):
        self.assertTrue(hasattr(PACKAGE, "PrintInfo"))
        self.assertTrue(hasattr(PACKAGE, "ReturnColour"))
        self.assertTrue(hasattr(PACKAGE, "PrintColor"))
        self.assertTrue(hasattr(PACKAGE, "ReturnColor"))

    def test_check_colour_in_list_accepts_supported_values(self):
        self.assertTrue(UTILS._checkColourInList("Rainbow"))
        self.assertTrue(UTILS._checkColourInList("Empty"))

    def test_check_colour_in_list_rejects_unknown_values(self):
        self.assertFalse(UTILS._checkColourInList("Orange"))

    def test_rainbow_returns_three_channels(self):
        channels = UTILS._rainbow(0)
        self.assertEqual(len(channels), 3)

    def test_rainbow_channels_stay_in_expected_range(self):
        channels = UTILS._rainbow(25)
        for channel in channels:
            self.assertGreaterEqual(channel, 1.0)
            self.assertLessEqual(channel, 255.0)

    def test_rainbow_uses_sine_wave_offsets(self):
        channels = UTILS._rainbow(3)
        expected = [
            math.sin(0.1 * 3 + 0) * 127 + 128,
            math.sin(0.1 * 3 + 2 * math.pi / 3) * 127 + 128,
            math.sin(0.1 * 3 + 4 * math.pi / 3) * 127 + 128,
        ]
        self.assertEqual(channels, expected)

    def test_utils_exposes_american_spelling_aliases(self):
        self.assertTrue(hasattr(UTILS, "convert_color"))
        self.assertTrue(hasattr(UTILS, "_checkColorInList"))
