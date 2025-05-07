import unittest
from nordpool.elspot import Prices, UnsupportedResolution


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_unsupported_resolution(self):
        elspot = Prices()
        with self.assertRaises(UnsupportedResolution):
            elspot.fetch(end_date="2025-05-07", areas=["FI"], resolution=10)
