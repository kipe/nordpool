import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_single_area_15min(self):
        with vcr.use_cassette("single_area_15min.yaml"):
            elspot = Prices()
            prices = elspot.fetch(end_date="2025-05-07", areas=["FI"], resolution=15)
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 22, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 22.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 22, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 15, tzinfo=utc
                                    ),
                                    "value": 22.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 22, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 30, tzinfo=utc
                                    ),
                                    "value": 22.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 45, tzinfo=utc
                                    ),
                                    "value": 22.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 14.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 15, tzinfo=utc
                                    ),
                                    "value": 14.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 30, tzinfo=utc
                                    ),
                                    "value": 14.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 45, tzinfo=utc
                                    ),
                                    "value": 14.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 12.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 15, tzinfo=utc
                                    ),
                                    "value": 12.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 30, tzinfo=utc
                                    ),
                                    "value": 12.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 45, tzinfo=utc
                                    ),
                                    "value": 12.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 13.69,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 15, tzinfo=utc
                                    ),
                                    "value": 13.69,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 30, tzinfo=utc
                                    ),
                                    "value": 13.69,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 45, tzinfo=utc
                                    ),
                                    "value": 13.69,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 19.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 15, tzinfo=utc
                                    ),
                                    "value": 19.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 30, tzinfo=utc
                                    ),
                                    "value": 19.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 45, tzinfo=utc
                                    ),
                                    "value": 19.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 55.31,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 15, tzinfo=utc
                                    ),
                                    "value": 55.31,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 30, tzinfo=utc
                                    ),
                                    "value": 55.31,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 45, tzinfo=utc
                                    ),
                                    "value": 55.31,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 111.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 15, tzinfo=utc
                                    ),
                                    "value": 111.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 30, tzinfo=utc
                                    ),
                                    "value": 111.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 45, tzinfo=utc
                                    ),
                                    "value": 111.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 15, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 30, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 45, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 15, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 30, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 45, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 92.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 15, tzinfo=utc
                                    ),
                                    "value": 92.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 30, tzinfo=utc
                                    ),
                                    "value": 92.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 45, tzinfo=utc
                                    ),
                                    "value": 92.48,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 62.72,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 15, tzinfo=utc
                                    ),
                                    "value": 62.72,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 30, tzinfo=utc
                                    ),
                                    "value": 62.72,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 45, tzinfo=utc
                                    ),
                                    "value": 62.72,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 66.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 15, tzinfo=utc
                                    ),
                                    "value": 66.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 30, tzinfo=utc
                                    ),
                                    "value": 66.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 45, tzinfo=utc
                                    ),
                                    "value": 66.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 57.84,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 15, tzinfo=utc
                                    ),
                                    "value": 57.84,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 30, tzinfo=utc
                                    ),
                                    "value": 57.84,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 45, tzinfo=utc
                                    ),
                                    "value": 57.84,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 31.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 15, tzinfo=utc
                                    ),
                                    "value": 31.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 30, tzinfo=utc
                                    ),
                                    "value": 31.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 45, tzinfo=utc
                                    ),
                                    "value": 31.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 27.14,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 15, tzinfo=utc
                                    ),
                                    "value": 27.14,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 30, tzinfo=utc
                                    ),
                                    "value": 27.14,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 45, tzinfo=utc
                                    ),
                                    "value": 27.14,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 25.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 15, tzinfo=utc
                                    ),
                                    "value": 25.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 30, tzinfo=utc
                                    ),
                                    "value": 25.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 45, tzinfo=utc
                                    ),
                                    "value": 25.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 30.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 15, tzinfo=utc
                                    ),
                                    "value": 30.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 30, tzinfo=utc
                                    ),
                                    "value": 30.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 45, tzinfo=utc
                                    ),
                                    "value": 30.77,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 83.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 15, tzinfo=utc
                                    ),
                                    "value": 83.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 30, tzinfo=utc
                                    ),
                                    "value": 83.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 45, tzinfo=utc
                                    ),
                                    "value": 83.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 110.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 15, tzinfo=utc
                                    ),
                                    "value": 110.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 30, tzinfo=utc
                                    ),
                                    "value": 110.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 45, tzinfo=utc
                                    ),
                                    "value": 110.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 150.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 15, tzinfo=utc
                                    ),
                                    "value": 150.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 30, tzinfo=utc
                                    ),
                                    "value": 150.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 45, tzinfo=utc
                                    ),
                                    "value": 150.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 158.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 15, tzinfo=utc
                                    ),
                                    "value": 158.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 30, tzinfo=utc
                                    ),
                                    "value": 158.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 45, tzinfo=utc
                                    ),
                                    "value": 158.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 138.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 15, tzinfo=utc
                                    ),
                                    "value": 138.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 30, tzinfo=utc
                                    ),
                                    "value": 138.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 45, tzinfo=utc
                                    ),
                                    "value": 138.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 109.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 15, tzinfo=utc
                                    ),
                                    "value": 109.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 30, tzinfo=utc
                                    ),
                                    "value": 109.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 45, tzinfo=utc
                                    ),
                                    "value": 109.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 15, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 94.16,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 30, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 15, tzinfo=utc
                                    ),
                                    "value": 94.16,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 45, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 30, tzinfo=utc
                                    ),
                                    "value": 94.16,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 45, tzinfo=utc
                                    ),
                                    "value": 94.16,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2025, 5, 6, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 22, 9, 220574, tzinfo=utc
                    ),
                },
            )
