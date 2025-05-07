import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_single_area_monthly(self):
        with vcr.use_cassette("single_area_monthly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.MONTHLY, end_date="2025-05-07", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.monthly("2025-05-07", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                                    "start": datetime.datetime(2025, 5, 1, 0, 0),
                                    "value": 21.28,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 30, 0, 0),
                                    "start": datetime.datetime(2025, 4, 1, 0, 0),
                                    "value": 47.75,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 31, 0, 0),
                                    "start": datetime.datetime(2025, 3, 1, 0, 0),
                                    "value": 47.52,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 28, 0, 0),
                                    "start": datetime.datetime(2025, 2, 1, 0, 0),
                                    "value": 47.29,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 31, 0, 0),
                                    "start": datetime.datetime(2025, 1, 1, 0, 0),
                                    "value": 52.82,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                    "start": datetime.datetime(2025, 1, 1, 0, 0),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 30, 47, 285765, tzinfo=utc
                    ),
                },
            )
