import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_multiple_area_hourly(self):
        with vcr.use_cassette("multiple_area_hourly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(
                elspot.HOURLY,
                end_date="2025-05-07",
                areas=["SE1", "SE2", "SE3", "SE4"],
            )
            self.assertEqual(
                prices,
                elspot.hourly("2025-05-07", areas=["SE1", "SE2", "SE3", "SE4"]),
            )
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
                                    "value": 22.34,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 14.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 12.58,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 12.89,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 19.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 55.3,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 111.76,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 92.25,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 60.67,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 65.51,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 57.06,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 31.17,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 26.61,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 24.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 30.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 83.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 93.38,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 91.65,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 89.04,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 93.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 107.04,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 94.17,
                                },
                            ]
                        },
                        "SE2": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 21.24,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 14.33,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 12.63,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 11.44,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 16.9,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 55.11,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 109.1,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 92.03,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 58.83,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 64.91,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 56.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 52.66,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 53.91,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 53.04,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 29.96,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 83.89,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 95.58,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 97.17,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 96.91,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 99.59,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 104.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 91.68,
                                },
                            ]
                        },
                        "SE3": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 56.85,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 50.11,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 48.66,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 49.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 55.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 80.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 119.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.37,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 93.33,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 70.33,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 69.01,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 60.46,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 56.66,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 59.37,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 61.51,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 55.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 88.81,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 107.75,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 133.88,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 144.53,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 126.89,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 106.96,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 93.8,
                                },
                            ]
                        },
                        "SE4": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 22, 0, tzinfo=utc
                                    ),
                                    "value": 90.32,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 6, 23, 0, tzinfo=utc
                                    ),
                                    "value": 84.73,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 0, 0, tzinfo=utc
                                    ),
                                    "value": 83.35,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 1, 0, tzinfo=utc
                                    ),
                                    "value": 86.24,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 2, 0, tzinfo=utc
                                    ),
                                    "value": 92.72,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 3, 0, tzinfo=utc
                                    ),
                                    "value": 105.96,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 4, 0, tzinfo=utc
                                    ),
                                    "value": 128.53,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 5, 0, tzinfo=utc
                                    ),
                                    "value": 143.95,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 6, 0, tzinfo=utc
                                    ),
                                    "value": 123.37,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 7, 0, tzinfo=utc
                                    ),
                                    "value": 94.03,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 8, 0, tzinfo=utc
                                    ),
                                    "value": 76.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 9, 0, tzinfo=utc
                                    ),
                                    "value": 71.28,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 10, 0, tzinfo=utc
                                    ),
                                    "value": 62.63,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 11, 0, tzinfo=utc
                                    ),
                                    "value": 61.75,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 12, 0, tzinfo=utc
                                    ),
                                    "value": 66.08,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 13, 0, tzinfo=utc
                                    ),
                                    "value": 70.1,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 14, 0, tzinfo=utc
                                    ),
                                    "value": 79.63,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 15, 0, tzinfo=utc
                                    ),
                                    "value": 93.94,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 16, 0, tzinfo=utc
                                    ),
                                    "value": 108.96,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 17, 0, tzinfo=utc
                                    ),
                                    "value": 129.36,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 18, 0, tzinfo=utc
                                    ),
                                    "value": 149.02,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 19, 0, tzinfo=utc
                                    ),
                                    "value": 124.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 20, 0, tzinfo=utc
                                    ),
                                    "value": 105.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2025, 5, 7, 22, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2025, 5, 7, 21, 0, tzinfo=utc
                                    ),
                                    "value": 94.29,
                                },
                            ]
                        },
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2025, 5, 6, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 22, 13, 816075, tzinfo=utc
                    ),
                },
            )
