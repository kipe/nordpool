import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    maxDiff = None

    def test_single_area_daily(self):
        with vcr.use_cassette("single_area_daily.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.DAILY, end_date="2025-05-07", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.daily("2025-05-07", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                                    "start": datetime.datetime(2025, 5, 7, 0, 0),
                                    "value": 73.21,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 6, 0, 0),
                                    "start": datetime.datetime(2025, 5, 6, 0, 0),
                                    "value": 30.73,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 5, 0, 0),
                                    "start": datetime.datetime(2025, 5, 5, 0, 0),
                                    "value": 27.94,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 4, 0, 0),
                                    "start": datetime.datetime(2025, 5, 4, 0, 0),
                                    "value": 1.53,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 3, 0, 0),
                                    "start": datetime.datetime(2025, 5, 3, 0, 0),
                                    "value": 0.99,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 2, 0, 0),
                                    "start": datetime.datetime(2025, 5, 2, 0, 0),
                                    "value": 1.19,
                                },
                                {
                                    "end": datetime.datetime(2025, 5, 1, 0, 0),
                                    "start": datetime.datetime(2025, 5, 1, 0, 0),
                                    "value": 13.37,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 30, 0, 0),
                                    "start": datetime.datetime(2025, 4, 30, 0, 0),
                                    "value": 155.06,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 29, 0, 0),
                                    "start": datetime.datetime(2025, 4, 29, 0, 0),
                                    "value": 51.61,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 28, 0, 0),
                                    "start": datetime.datetime(2025, 4, 28, 0, 0),
                                    "value": 49.47,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 27, 0, 0),
                                    "start": datetime.datetime(2025, 4, 27, 0, 0),
                                    "value": 53.52,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 26, 0, 0),
                                    "start": datetime.datetime(2025, 4, 26, 0, 0),
                                    "value": 29.63,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 25, 0, 0),
                                    "start": datetime.datetime(2025, 4, 25, 0, 0),
                                    "value": 90.25,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 24, 0, 0),
                                    "start": datetime.datetime(2025, 4, 24, 0, 0),
                                    "value": 169.18,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 23, 0, 0),
                                    "start": datetime.datetime(2025, 4, 23, 0, 0),
                                    "value": 88.93,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 22, 0, 0),
                                    "start": datetime.datetime(2025, 4, 22, 0, 0),
                                    "value": 183.05,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 21, 0, 0),
                                    "start": datetime.datetime(2025, 4, 21, 0, 0),
                                    "value": 50.95,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 20, 0, 0),
                                    "start": datetime.datetime(2025, 4, 20, 0, 0),
                                    "value": 13.38,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 19, 0, 0),
                                    "start": datetime.datetime(2025, 4, 19, 0, 0),
                                    "value": 51.08,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 18, 0, 0),
                                    "start": datetime.datetime(2025, 4, 18, 0, 0),
                                    "value": 26.1,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 17, 0, 0),
                                    "start": datetime.datetime(2025, 4, 17, 0, 0),
                                    "value": 79.19,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 16, 0, 0),
                                    "start": datetime.datetime(2025, 4, 16, 0, 0),
                                    "value": 12.84,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 15, 0, 0),
                                    "start": datetime.datetime(2025, 4, 15, 0, 0),
                                    "value": 23.46,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 14, 0, 0),
                                    "start": datetime.datetime(2025, 4, 14, 0, 0),
                                    "value": 4.08,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 13, 0, 0),
                                    "start": datetime.datetime(2025, 4, 13, 0, 0),
                                    "value": 2.24,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 12, 0, 0),
                                    "start": datetime.datetime(2025, 4, 12, 0, 0),
                                    "value": 4.03,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 11, 0, 0),
                                    "start": datetime.datetime(2025, 4, 11, 0, 0),
                                    "value": 46.26,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 10, 0, 0),
                                    "start": datetime.datetime(2025, 4, 10, 0, 0),
                                    "value": 39.33,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 9, 0, 0),
                                    "start": datetime.datetime(2025, 4, 9, 0, 0),
                                    "value": 1.03,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 8, 0, 0),
                                    "start": datetime.datetime(2025, 4, 8, 0, 0),
                                    "value": 45.97,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 7, 0, 0),
                                    "start": datetime.datetime(2025, 4, 7, 0, 0),
                                    "value": 72.79,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 6, 0, 0),
                                    "start": datetime.datetime(2025, 4, 6, 0, 0),
                                    "value": 50.52,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 5, 0, 0),
                                    "start": datetime.datetime(2025, 4, 5, 0, 0),
                                    "value": 17.46,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 4, 0, 0),
                                    "start": datetime.datetime(2025, 4, 4, 0, 0),
                                    "value": -0.49,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 3, 0, 0),
                                    "start": datetime.datetime(2025, 4, 3, 0, 0),
                                    "value": -1.33,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 2, 0, 0),
                                    "start": datetime.datetime(2025, 4, 2, 0, 0),
                                    "value": 0.97,
                                },
                                {
                                    "end": datetime.datetime(2025, 4, 1, 0, 0),
                                    "start": datetime.datetime(2025, 4, 1, 0, 0),
                                    "value": 21.95,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 31, 0, 0),
                                    "start": datetime.datetime(2025, 3, 31, 0, 0),
                                    "value": 119.93,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 30, 0, 0),
                                    "start": datetime.datetime(2025, 3, 30, 0, 0),
                                    "value": 57.9,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 29, 0, 0),
                                    "start": datetime.datetime(2025, 3, 29, 0, 0),
                                    "value": 1.65,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 28, 0, 0),
                                    "start": datetime.datetime(2025, 3, 28, 0, 0),
                                    "value": 3.38,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 27, 0, 0),
                                    "start": datetime.datetime(2025, 3, 27, 0, 0),
                                    "value": 2.97,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 26, 0, 0),
                                    "start": datetime.datetime(2025, 3, 26, 0, 0),
                                    "value": 80.37,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 25, 0, 0),
                                    "start": datetime.datetime(2025, 3, 25, 0, 0),
                                    "value": 32.32,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 24, 0, 0),
                                    "start": datetime.datetime(2025, 3, 24, 0, 0),
                                    "value": 12.96,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 23, 0, 0),
                                    "start": datetime.datetime(2025, 3, 23, 0, 0),
                                    "value": 5.54,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 22, 0, 0),
                                    "start": datetime.datetime(2025, 3, 22, 0, 0),
                                    "value": 0.62,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 21, 0, 0),
                                    "start": datetime.datetime(2025, 3, 21, 0, 0),
                                    "value": 97.53,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 20, 0, 0),
                                    "start": datetime.datetime(2025, 3, 20, 0, 0),
                                    "value": 93.3,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 19, 0, 0),
                                    "start": datetime.datetime(2025, 3, 19, 0, 0),
                                    "value": 21.98,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 18, 0, 0),
                                    "start": datetime.datetime(2025, 3, 18, 0, 0),
                                    "value": 29.36,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 17, 0, 0),
                                    "start": datetime.datetime(2025, 3, 17, 0, 0),
                                    "value": 64.88,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 16, 0, 0),
                                    "start": datetime.datetime(2025, 3, 16, 0, 0),
                                    "value": 8.22,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 15, 0, 0),
                                    "start": datetime.datetime(2025, 3, 15, 0, 0),
                                    "value": 3.28,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 14, 0, 0),
                                    "start": datetime.datetime(2025, 3, 14, 0, 0),
                                    "value": 87.25,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 13, 0, 0),
                                    "start": datetime.datetime(2025, 3, 13, 0, 0),
                                    "value": 172.49,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 12, 0, 0),
                                    "start": datetime.datetime(2025, 3, 12, 0, 0),
                                    "value": 148.08,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 11, 0, 0),
                                    "start": datetime.datetime(2025, 3, 11, 0, 0),
                                    "value": 101.76,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 10, 0, 0),
                                    "start": datetime.datetime(2025, 3, 10, 0, 0),
                                    "value": 100.1,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 9, 0, 0),
                                    "start": datetime.datetime(2025, 3, 9, 0, 0),
                                    "value": 75.21,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 8, 0, 0),
                                    "start": datetime.datetime(2025, 3, 8, 0, 0),
                                    "value": 0.15,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 7, 0, 0),
                                    "start": datetime.datetime(2025, 3, 7, 0, 0),
                                    "value": 48.59,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 6, 0, 0),
                                    "start": datetime.datetime(2025, 3, 6, 0, 0),
                                    "value": 11.67,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 5, 0, 0),
                                    "start": datetime.datetime(2025, 3, 5, 0, 0),
                                    "value": 1.56,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 4, 0, 0),
                                    "start": datetime.datetime(2025, 3, 4, 0, 0),
                                    "value": 5.48,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 3, 0, 0),
                                    "start": datetime.datetime(2025, 3, 3, 0, 0),
                                    "value": 4.39,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 2, 0, 0),
                                    "start": datetime.datetime(2025, 3, 2, 0, 0),
                                    "value": 2.23,
                                },
                                {
                                    "end": datetime.datetime(2025, 3, 1, 0, 0),
                                    "start": datetime.datetime(2025, 3, 1, 0, 0),
                                    "value": 78.48,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 28, 0, 0),
                                    "start": datetime.datetime(2025, 2, 28, 0, 0),
                                    "value": 63.62,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 27, 0, 0),
                                    "start": datetime.datetime(2025, 2, 27, 0, 0),
                                    "value": 34.53,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 26, 0, 0),
                                    "start": datetime.datetime(2025, 2, 26, 0, 0),
                                    "value": 31,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 25, 0, 0),
                                    "start": datetime.datetime(2025, 2, 25, 0, 0),
                                    "value": 4.9,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 24, 0, 0),
                                    "start": datetime.datetime(2025, 2, 24, 0, 0),
                                    "value": 2.37,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 23, 0, 0),
                                    "start": datetime.datetime(2025, 2, 23, 0, 0),
                                    "value": 2.5,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 22, 0, 0),
                                    "start": datetime.datetime(2025, 2, 22, 0, 0),
                                    "value": 1.65,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 21, 0, 0),
                                    "start": datetime.datetime(2025, 2, 21, 0, 0),
                                    "value": 2.17,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 20, 0, 0),
                                    "start": datetime.datetime(2025, 2, 20, 0, 0),
                                    "value": 19.14,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 19, 0, 0),
                                    "start": datetime.datetime(2025, 2, 19, 0, 0),
                                    "value": 75.67,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 18, 0, 0),
                                    "start": datetime.datetime(2025, 2, 18, 0, 0),
                                    "value": 21.69,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 17, 0, 0),
                                    "start": datetime.datetime(2025, 2, 17, 0, 0),
                                    "value": 125.23,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 16, 0, 0),
                                    "start": datetime.datetime(2025, 2, 16, 0, 0),
                                    "value": 120.21,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 15, 0, 0),
                                    "start": datetime.datetime(2025, 2, 15, 0, 0),
                                    "value": 60.17,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 14, 0, 0),
                                    "start": datetime.datetime(2025, 2, 14, 0, 0),
                                    "value": 156.86,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 13, 0, 0),
                                    "start": datetime.datetime(2025, 2, 13, 0, 0),
                                    "value": 79.96,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 12, 0, 0),
                                    "start": datetime.datetime(2025, 2, 12, 0, 0),
                                    "value": 72.07,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 11, 0, 0),
                                    "start": datetime.datetime(2025, 2, 11, 0, 0),
                                    "value": 41.48,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 10, 0, 0),
                                    "start": datetime.datetime(2025, 2, 10, 0, 0),
                                    "value": 72.47,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 9, 0, 0),
                                    "start": datetime.datetime(2025, 2, 9, 0, 0),
                                    "value": 8.83,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 8, 0, 0),
                                    "start": datetime.datetime(2025, 2, 8, 0, 0),
                                    "value": 36.65,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 7, 0, 0),
                                    "start": datetime.datetime(2025, 2, 7, 0, 0),
                                    "value": 9.62,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 6, 0, 0),
                                    "start": datetime.datetime(2025, 2, 6, 0, 0),
                                    "value": 55.95,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 5, 0, 0),
                                    "start": datetime.datetime(2025, 2, 5, 0, 0),
                                    "value": 7.03,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 4, 0, 0),
                                    "start": datetime.datetime(2025, 2, 4, 0, 0),
                                    "value": 84.21,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 3, 0, 0),
                                    "start": datetime.datetime(2025, 2, 3, 0, 0),
                                    "value": 108.11,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 2, 0, 0),
                                    "start": datetime.datetime(2025, 2, 2, 0, 0),
                                    "value": 16,
                                },
                                {
                                    "end": datetime.datetime(2025, 2, 1, 0, 0),
                                    "start": datetime.datetime(2025, 2, 1, 0, 0),
                                    "value": 10.1,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 31, 0, 0),
                                    "start": datetime.datetime(2025, 1, 31, 0, 0),
                                    "value": 52.91,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 30, 0, 0),
                                    "start": datetime.datetime(2025, 1, 30, 0, 0),
                                    "value": 26.39,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 29, 0, 0),
                                    "start": datetime.datetime(2025, 1, 29, 0, 0),
                                    "value": 53.54,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 28, 0, 0),
                                    "start": datetime.datetime(2025, 1, 28, 0, 0),
                                    "value": 61.27,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 27, 0, 0),
                                    "start": datetime.datetime(2025, 1, 27, 0, 0),
                                    "value": 57.24,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 26, 0, 0),
                                    "start": datetime.datetime(2025, 1, 26, 0, 0),
                                    "value": 14.71,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 25, 0, 0),
                                    "start": datetime.datetime(2025, 1, 25, 0, 0),
                                    "value": 2.01,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 24, 0, 0),
                                    "start": datetime.datetime(2025, 1, 24, 0, 0),
                                    "value": 29.16,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 23, 0, 0),
                                    "start": datetime.datetime(2025, 1, 23, 0, 0),
                                    "value": 87.48,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 22, 0, 0),
                                    "start": datetime.datetime(2025, 1, 22, 0, 0),
                                    "value": 120.31,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 21, 0, 0),
                                    "start": datetime.datetime(2025, 1, 21, 0, 0),
                                    "value": 48.5,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 20, 0, 0),
                                    "start": datetime.datetime(2025, 1, 20, 0, 0),
                                    "value": 140.86,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 19, 0, 0),
                                    "start": datetime.datetime(2025, 1, 19, 0, 0),
                                    "value": 4.68,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 18, 0, 0),
                                    "start": datetime.datetime(2025, 1, 18, 0, 0),
                                    "value": 3.39,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 17, 0, 0),
                                    "start": datetime.datetime(2025, 1, 17, 0, 0),
                                    "value": 2.62,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 16, 0, 0),
                                    "start": datetime.datetime(2025, 1, 16, 0, 0),
                                    "value": 1.69,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 15, 0, 0),
                                    "start": datetime.datetime(2025, 1, 15, 0, 0),
                                    "value": 43.44,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 14, 0, 0),
                                    "start": datetime.datetime(2025, 1, 14, 0, 0),
                                    "value": 5.63,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 13, 0, 0),
                                    "start": datetime.datetime(2025, 1, 13, 0, 0),
                                    "value": 11.9,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 12, 0, 0),
                                    "start": datetime.datetime(2025, 1, 12, 0, 0),
                                    "value": 62.96,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 11, 0, 0),
                                    "start": datetime.datetime(2025, 1, 11, 0, 0),
                                    "value": 37.07,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 10, 0, 0),
                                    "start": datetime.datetime(2025, 1, 10, 0, 0),
                                    "value": 92.49,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 9, 0, 0),
                                    "start": datetime.datetime(2025, 1, 9, 0, 0),
                                    "value": 103.74,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 8, 0, 0),
                                    "start": datetime.datetime(2025, 1, 8, 0, 0),
                                    "value": 63.87,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 7, 0, 0),
                                    "start": datetime.datetime(2025, 1, 7, 0, 0),
                                    "value": 19.68,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 6, 0, 0),
                                    "start": datetime.datetime(2025, 1, 6, 0, 0),
                                    "value": 79.23,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 5, 0, 0),
                                    "start": datetime.datetime(2025, 1, 5, 0, 0),
                                    "value": 72.32,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 4, 0, 0),
                                    "start": datetime.datetime(2025, 1, 4, 0, 0),
                                    "value": 95.22,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 3, 0, 0),
                                    "start": datetime.datetime(2025, 1, 3, 0, 0),
                                    "value": 88.98,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 2, 0, 0),
                                    "start": datetime.datetime(2025, 1, 2, 0, 0),
                                    "value": 93.6,
                                },
                                {
                                    "end": datetime.datetime(2025, 1, 1, 0, 0),
                                    "start": datetime.datetime(2025, 1, 1, 0, 0),
                                    "value": 60.57,
                                },
                            ]
                        }
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2025, 5, 7, 0, 0),
                    "start": datetime.datetime(2025, 1, 1, 0, 0),
                    "updated": datetime.datetime(
                        2025, 5, 6, 11, 30, 47, 285765, tzinfo=utc
                    ),
                },
            )
