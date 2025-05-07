import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_system_hourly(self):
        with vcr.use_cassette("system_hourly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.HOURLY, end_date="2025-05-07", areas=["SYS"])
            self.assertEqual(
                prices,
                elspot.hourly("2025-05-07", areas=["SYS"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "SYS": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 74.2,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 68.4,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 67.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 68.04,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 70.3,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 87.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 116.11,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.89,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 94.98,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 79.98,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 74.28,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 64.68,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 60.92,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 62.85,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 67.29,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 67.69,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 86.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 105.3,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 121.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 132.21,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 110.74,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 99.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 86.46,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2025, 5, 6, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2025, 5, 6, 10, 56, 31, 12006, tzinfo=utc
                    ),
                },
            )
