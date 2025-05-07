import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_single_area_hourly(self):
        with vcr.use_cassette("single_area_hourly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.HOURLY, end_date="2024-10-15", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.hourly("2024-10-15", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 22, 0, tzinfo=utc
                                    ),
                                    "value": 45.13,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 27.31,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 25.68,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 16.71,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 12.04,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 26.56,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "value": 48.5,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "value": 129.35,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "value": 122.86,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "value": 106.38,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "value": 59.51,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "value": 48.38,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "value": 35.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "value": 27.24,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "value": 28.13,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "value": 35.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "value": 45.52,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "value": 30.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 38.66,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 27.73,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 20.24,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "value": 20.05,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "value": 14.07,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 21, 0, tzinfo=utc
                                    ),
                                    "value": 10.16,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2024, 10, 15, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2024, 10, 14, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2024, 10, 14, 11, 17, 1, 454046, tzinfo=utc
                    ),
                },
            )
