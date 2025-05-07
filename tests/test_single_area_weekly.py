import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_single_area_weekly(self):
        with vcr.use_cassette("single_area_weekly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.WEEKLY, end_date="2024-10-15", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.weekly("2024-10-15", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                                    "start": datetime.datetime(2024, 10, 14, 0, 0),
                                    "value": 60.88,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 13, 0, 0),
                                    "start": datetime.datetime(2024, 10, 7, 0, 0),
                                    "value": 26.52,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 6, 0, 0),
                                    "start": datetime.datetime(2024, 9, 30, 0, 0),
                                    "value": 109,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 29, 0, 0),
                                    "start": datetime.datetime(2024, 9, 23, 0, 0),
                                    "value": 24.86,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 22, 0, 0),
                                    "start": datetime.datetime(2024, 9, 16, 0, 0),
                                    "value": 85.8,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 15, 0, 0),
                                    "start": datetime.datetime(2024, 9, 9, 0, 0),
                                    "value": 72.77,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 8, 0, 0),
                                    "start": datetime.datetime(2024, 9, 2, 0, 0),
                                    "value": 44.67,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 1, 0, 0),
                                    "start": datetime.datetime(2024, 8, 26, 0, 0),
                                    "value": 6.6,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 25, 0, 0),
                                    "start": datetime.datetime(2024, 8, 19, 0, 0),
                                    "value": 5.8,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 18, 0, 0),
                                    "start": datetime.datetime(2024, 8, 12, 0, 0),
                                    "value": 23.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 11, 0, 0),
                                    "start": datetime.datetime(2024, 8, 5, 0, 0),
                                    "value": 10.57,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 4, 0, 0),
                                    "start": datetime.datetime(2024, 7, 29, 0, 0),
                                    "value": 16.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 28, 0, 0),
                                    "start": datetime.datetime(2024, 7, 22, 0, 0),
                                    "value": 22.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 21, 0, 0),
                                    "start": datetime.datetime(2024, 7, 15, 0, 0),
                                    "value": 16.82,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 14, 0, 0),
                                    "start": datetime.datetime(2024, 7, 8, 0, 0),
                                    "value": 12.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 7, 0, 0),
                                    "start": datetime.datetime(2024, 7, 1, 0, 0),
                                    "value": 16.51,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 30, 0, 0),
                                    "start": datetime.datetime(2024, 6, 24, 0, 0),
                                    "value": 19.26,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 23, 0, 0),
                                    "start": datetime.datetime(2024, 6, 17, 0, 0),
                                    "value": 24.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 16, 0, 0),
                                    "start": datetime.datetime(2024, 6, 10, 0, 0),
                                    "value": 60.21,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 9, 0, 0),
                                    "start": datetime.datetime(2024, 6, 3, 0, 0),
                                    "value": 44.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 2, 0, 0),
                                    "start": datetime.datetime(2024, 5, 27, 0, 0),
                                    "value": 37.08,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 26, 0, 0),
                                    "start": datetime.datetime(2024, 5, 20, 0, 0),
                                    "value": 11.49,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 19, 0, 0),
                                    "start": datetime.datetime(2024, 5, 13, 0, 0),
                                    "value": 30.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 12, 0, 0),
                                    "start": datetime.datetime(2024, 5, 6, 0, 0),
                                    "value": 46.57,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 5, 0, 0),
                                    "start": datetime.datetime(2024, 4, 29, 0, 0),
                                    "value": 51.08,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 28, 0, 0),
                                    "start": datetime.datetime(2024, 4, 22, 0, 0),
                                    "value": 76.44,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 21, 0, 0),
                                    "start": datetime.datetime(2024, 4, 15, 0, 0),
                                    "value": 58.82,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 14, 0, 0),
                                    "start": datetime.datetime(2024, 4, 8, 0, 0),
                                    "value": 20.3,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 7, 0, 0),
                                    "start": datetime.datetime(2024, 4, 1, 0, 0),
                                    "value": 39.86,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 31, 0, 0),
                                    "start": datetime.datetime(2024, 3, 25, 0, 0),
                                    "value": 53.65,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 24, 0, 0),
                                    "start": datetime.datetime(2024, 3, 18, 0, 0),
                                    "value": 55.97,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 17, 0, 0),
                                    "start": datetime.datetime(2024, 3, 11, 0, 0),
                                    "value": 49.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 10, 0, 0),
                                    "start": datetime.datetime(2024, 3, 4, 0, 0),
                                    "value": 84.34,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 3, 0, 0),
                                    "start": datetime.datetime(2024, 2, 26, 0, 0),
                                    "value": 40.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 25, 0, 0),
                                    "start": datetime.datetime(2024, 2, 19, 0, 0),
                                    "value": 39.56,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 18, 0, 0),
                                    "start": datetime.datetime(2024, 2, 12, 0, 0),
                                    "value": 45.38,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 11, 0, 0),
                                    "start": datetime.datetime(2024, 2, 5, 0, 0),
                                    "value": 103.97,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 4, 0, 0),
                                    "start": datetime.datetime(2024, 1, 29, 0, 0),
                                    "value": 11.07,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 28, 0, 0),
                                    "start": datetime.datetime(2024, 1, 22, 0, 0),
                                    "value": 46.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 21, 0, 0),
                                    "start": datetime.datetime(2024, 1, 15, 0, 0),
                                    "value": 91.89,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 14, 0, 0),
                                    "start": datetime.datetime(2024, 1, 8, 0, 0),
                                    "value": 82.81,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 7, 0, 0),
                                    "start": datetime.datetime(2024, 1, 1, 0, 0),
                                    "value": 242.73,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                    "start": datetime.datetime(2024, 1, 1, 0, 0),
                    "updated": datetime.datetime(
                        2024, 10, 15, 11, 26, 23, 648334, tzinfo=utc
                    ),
                },
            )
