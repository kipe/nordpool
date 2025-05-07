import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_different_currency(self):
        with vcr.use_cassette("different_currency.yaml"):
            elspot = Prices(currency="SEK")
            prices = elspot.fetch(elspot.HOURLY, end_date="2025-05-07", areas=["SE1"])
            # pprint(prices)
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "SE1": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 243.58,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 155.37,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 137.16,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 140.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 211.08,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 602.94,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 1218.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 1569.51,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 1345.01,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 1005.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 661.49,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 714.27,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 622.13,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 339.85,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 290.13,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 266.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 335.6,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 914.56,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 1018.14,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 999.27,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 970.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 1024.13,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 1167.07,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 1026.75,
                                },
                            ]
                        }
                    },
                    "currency": "SEK",
                    "end": datetime.datetime(2025, 5, 7, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2025, 5, 6, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 22, 13, 683352, tzinfo=utc
                    ),
                },
            )
