import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_single_area_weekly(self):
        with vcr.use_cassette("single_area_weekly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.WEEKLY, end_date="2025-05-07", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.weekly("2025-05-07", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                                    "start": datetime.datetime(2025, 5, 5, 0, 0),
                                    "value": 43.96,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 4, 0, 0),
                                    "start": datetime.datetime(2025, 4, 28, 0, 0),
                                    "value": 39.03,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 27, 0, 0),
                                    "start": datetime.datetime(2025, 4, 21, 0, 0),
                                    "value": 95.07,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 20, 0, 0),
                                    "start": datetime.datetime(2025, 4, 14, 0, 0),
                                    "value": 30.02,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 13, 0, 0),
                                    "start": datetime.datetime(2025, 4, 7, 0, 0),
                                    "value": 30.24,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 6, 0, 0),
                                    "start": datetime.datetime(2025, 3, 31, 0, 0),
                                    "value": 29.86,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 30, 0, 0),
                                    "start": datetime.datetime(2025, 3, 24, 0, 0),
                                    "value": 27.18,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 23, 0, 0),
                                    "start": datetime.datetime(2025, 3, 17, 0, 0),
                                    "value": 44.74,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 16, 0, 0),
                                    "start": datetime.datetime(2025, 3, 10, 0, 0),
                                    "value": 88.74,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 9, 0, 0),
                                    "start": datetime.datetime(2025, 3, 3, 0, 0),
                                    "value": 21.01,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 2, 0, 0),
                                    "start": datetime.datetime(2025, 2, 24, 0, 0),
                                    "value": 31.02,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 23, 0, 0),
                                    "start": datetime.datetime(2025, 2, 17, 0, 0),
                                    "value": 35.44,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 16, 0, 0),
                                    "start": datetime.datetime(2025, 2, 10, 0, 0),
                                    "value": 86.17,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 9, 0, 0),
                                    "start": datetime.datetime(2025, 2, 3, 0, 0),
                                    "value": 44.34,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 2, 0, 0),
                                    "start": datetime.datetime(2025, 1, 27, 0, 0),
                                    "value": 39.64,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 26, 0, 0),
                                    "start": datetime.datetime(2025, 1, 20, 0, 0),
                                    "value": 63.29,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 19, 0, 0),
                                    "start": datetime.datetime(2025, 1, 13, 0, 0),
                                    "value": 10.48,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 12, 0, 0),
                                    "start": datetime.datetime(2025, 1, 6, 0, 0),
                                    "value": 65.58,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 5, 0, 0),
                                    "start": datetime.datetime(2024, 12, 30, 0, 0),
                                    "value": 60.28,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                    "start": datetime.datetime(2024, 12, 30, 0, 0),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 30, 47, 285765, tzinfo=utc
                    ),
                },
            )
