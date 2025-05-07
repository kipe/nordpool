import unittest
from nordpool.elspot import Prices
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_prices_not_available(self):
        with vcr.use_cassette("prices_not_available.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.HOURLY, end_date="2025-05-10", areas=["FI"])
            self.assertIsNone(prices)
