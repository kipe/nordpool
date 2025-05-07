import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_single_area_yearly(self):
        with vcr.use_cassette("single_area_yearly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.YEARLY, end_date="2024-10-15", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.yearly("2024-10-15", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                                    "start": datetime.datetime(2024, 1, 1, 0, 0),
                                    "value": 47.97,
                                },
                                {
                                    "end": datetime.datetime(2023, 12, 31, 0, 0),
                                    "start": datetime.datetime(2023, 1, 1, 0, 0),
                                    "value": 56.47,
                                },
                                {
                                    "end": datetime.datetime(2022, 12, 31, 0, 0),
                                    "start": datetime.datetime(2022, 1, 1, 0, 0),
                                    "value": 154.04,
                                },
                                {
                                    "end": datetime.datetime(2021, 12, 31, 0, 0),
                                    "start": datetime.datetime(2021, 1, 1, 0, 0),
                                    "value": 72.34,
                                },
                                {
                                    "end": datetime.datetime(2020, 12, 31, 0, 0),
                                    "start": datetime.datetime(2020, 1, 1, 0, 0),
                                    "value": 28.02,
                                },
                                {
                                    "end": datetime.datetime(2019, 12, 31, 0, 0),
                                    "start": datetime.datetime(2019, 1, 1, 0, 0),
                                    "value": 44.04,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                    "start": datetime.datetime(2019, 1, 1, 0, 0),
                    "updated": datetime.datetime(
                        2024, 3, 26, 13, 18, 33, 301921, tzinfo=utc
                    ),
                },
            )
