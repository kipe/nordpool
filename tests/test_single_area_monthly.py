import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_single_area_monthly(self):
        with vcr.use_cassette("single_area_monthly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.MONTHLY, end_date="2024-10-15", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.monthly("2024-10-15", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                                    "start": datetime.datetime(2024, 10, 1, 0, 0),
                                    "value": 65.98,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 30, 0, 0),
                                    "start": datetime.datetime(2024, 9, 1, 0, 0),
                                    "value": 56.02,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 31, 0, 0),
                                    "start": datetime.datetime(2024, 8, 1, 0, 0),
                                    "value": 12.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 31, 0, 0),
                                    "start": datetime.datetime(2024, 7, 1, 0, 0),
                                    "value": 16.74,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 30, 0, 0),
                                    "start": datetime.datetime(2024, 6, 1, 0, 0),
                                    "value": 36.09,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 31, 0, 0),
                                    "start": datetime.datetime(2024, 5, 1, 0, 0),
                                    "value": 35.13,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 30, 0, 0),
                                    "start": datetime.datetime(2024, 4, 1, 0, 0),
                                    "value": 48.92,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 31, 0, 0),
                                    "start": datetime.datetime(2024, 3, 1, 0, 0),
                                    "value": 59.38,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 29, 0, 0),
                                    "start": datetime.datetime(2024, 2, 1, 0, 0),
                                    "value": 51.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 31, 0, 0),
                                    "start": datetime.datetime(2024, 1, 1, 0, 0),
                                    "value": 106.22,
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
