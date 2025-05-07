import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_different_currency(self):
        with vcr.use_cassette("different_currency.yaml"):
            elspot = Prices(currency="SEK")
            prices = elspot.fetch(elspot.HOURLY, end_date="2024-10-15", areas=["SE1"])
            # pprint(prices)
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "SE1": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 22, 0, tzinfo=utc
                                    ),
                                    "value": 95.81,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 75.33,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 84.55,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 77.6,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 119.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 165.45,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "value": 173.64,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "value": 182.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "value": 204.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "value": 227.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "value": 247.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "value": 260.92,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "value": 272.87,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "value": 279.58,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "value": 277.87,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "value": 263.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "value": 252.27,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "value": 226.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 187.41,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 175.24,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 171.03,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "value": 170.12,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "value": 160.1,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 21, 0, tzinfo=utc
                                    ),
                                    "value": 115.61,
                                },
                            ]
                        }
                    },
                    "currency": "SEK",
                    "end": datetime.datetime(2024, 10, 15, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2024, 10, 14, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2024, 10, 14, 11, 17, 2, 702631, tzinfo=utc
                    ),
                },
            )
