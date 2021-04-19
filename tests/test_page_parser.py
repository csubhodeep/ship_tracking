

import unittest
from utils.page_parser import parse_page


class TestPageParser(unittest.TestCase):

    def setUp(self) -> None:

        with open('test.html', 'r') as f:
            self.page = f.read()


    def test_parse_page(self):

        true_output = {
            "Engine Model": "C32 TA, V-12, 4-Stroke Water-Cooled Diesel",
            "Min. Rating": "830 ekW (910 kVA)",
            "Max. Rating": "1000 ekW (1250 kVA)",
            "Voltage": "220 to 4160",
            "Frequency": "50 or 60 Hz",
            "Speed": "1500 or 1800 rpm"
	    }

        self.assertDictEqual(parse_page(self.page), true_output)


if __name__ == "__main__":
    unittest.main()