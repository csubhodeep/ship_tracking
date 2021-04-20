

import unittest
from utils.page_parser import parse_tech_specs, parse_links


class TestPageParser(unittest.TestCase):

    def setUp(self) -> None:

        with open('test.html', 'r') as f:
            self.page = f.read()

        with open('test2.html', 'r') as f:
            self.page2 = f.read()

    def test_parse_tech_specs(self):

        true_output = {
            "Engine Model": "C32 TA, V-12, 4-Stroke Water-Cooled Diesel",
            "Minimum Rating": "830 ekW (910 kVA)",
            "Maximum Rating": "1000 ekW (1250 kVA)",
            "Voltage": "220 to 4160",
            "Frequency": "50 or 60 Hz",
            "Speed": "1500 or 1800 rpm"
	    }

        self.assertDictContainsSubset(true_output, parse_tech_specs(self.page))

    def test_parse_links(self):

        true_output = "en_CA/products/new/power-systems/electric-power-generation/diesel-generator-sets/1000033110.html"

        self.assertIn(true_output, parse_links(self.page2))


if __name__ == "__main__":
    unittest.main()