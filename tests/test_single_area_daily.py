import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_single_area_daily(self):
        with vcr.use_cassette("single_area_daily.yaml"):
            elspot = Prices()
            prices = elspot.fetch(elspot.DAILY, end_date="2024-10-15", areas=["FI"])
            self.assertEqual(
                prices,
                elspot.daily("2024-10-15", areas=["FI"]),
            )
            self.assertEqual(
                prices,
                {
                    "areas": {
                        "FI": {
                            "values": [
                                {
                                    "end": datetime.datetime(2024, 10, 16, 0, 0),
                                    "start": datetime.datetime(2024, 10, 16, 0, 0),
                                    "value": 12.19,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 15, 0, 0),
                                    "start": datetime.datetime(2024, 10, 15, 0, 0),
                                    "value": 41.68,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 14, 0, 0),
                                    "start": datetime.datetime(2024, 10, 14, 0, 0),
                                    "value": 128.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 13, 0, 0),
                                    "start": datetime.datetime(2024, 10, 13, 0, 0),
                                    "value": 12.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 12, 0, 0),
                                    "start": datetime.datetime(2024, 10, 12, 0, 0),
                                    "value": 12.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 11, 0, 0),
                                    "start": datetime.datetime(2024, 10, 11, 0, 0),
                                    "value": 10.1,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 10, 0, 0),
                                    "start": datetime.datetime(2024, 10, 10, 0, 0),
                                    "value": 10.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 9, 0, 0),
                                    "start": datetime.datetime(2024, 10, 9, 0, 0),
                                    "value": 5.3,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 8, 0, 0),
                                    "start": datetime.datetime(2024, 10, 8, 0, 0),
                                    "value": 29.19,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 7, 0, 0),
                                    "start": datetime.datetime(2024, 10, 7, 0, 0),
                                    "value": 106.67,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 6, 0, 0),
                                    "start": datetime.datetime(2024, 10, 6, 0, 0),
                                    "value": 34.38,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 5, 0, 0),
                                    "start": datetime.datetime(2024, 10, 5, 0, 0),
                                    "value": 91.97,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 4, 0, 0),
                                    "start": datetime.datetime(2024, 10, 4, 0, 0),
                                    "value": 77.16,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 3, 0, 0),
                                    "start": datetime.datetime(2024, 10, 3, 0, 0),
                                    "value": 183.38,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 2, 0, 0),
                                    "start": datetime.datetime(2024, 10, 2, 0, 0),
                                    "value": 241.37,
                                },
                                {
                                    "end": datetime.datetime(2024, 10, 1, 0, 0),
                                    "start": datetime.datetime(2024, 10, 1, 0, 0),
                                    "value": 59.21,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 30, 0, 0),
                                    "start": datetime.datetime(2024, 9, 30, 0, 0),
                                    "value": 75.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 29, 0, 0),
                                    "start": datetime.datetime(2024, 9, 29, 0, 0),
                                    "value": 5.29,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 28, 0, 0),
                                    "start": datetime.datetime(2024, 9, 28, 0, 0),
                                    "value": 42.1,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 27, 0, 0),
                                    "start": datetime.datetime(2024, 9, 27, 0, 0),
                                    "value": 12.26,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 26, 0, 0),
                                    "start": datetime.datetime(2024, 9, 26, 0, 0),
                                    "value": 24.16,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 25, 0, 0),
                                    "start": datetime.datetime(2024, 9, 25, 0, 0),
                                    "value": 8.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 24, 0, 0),
                                    "start": datetime.datetime(2024, 9, 24, 0, 0),
                                    "value": 23.57,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 23, 0, 0),
                                    "start": datetime.datetime(2024, 9, 23, 0, 0),
                                    "value": 58.49,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 22, 0, 0),
                                    "start": datetime.datetime(2024, 9, 22, 0, 0),
                                    "value": 97.48,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 21, 0, 0),
                                    "start": datetime.datetime(2024, 9, 21, 0, 0),
                                    "value": 21.39,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 20, 0, 0),
                                    "start": datetime.datetime(2024, 9, 20, 0, 0),
                                    "value": 72.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 19, 0, 0),
                                    "start": datetime.datetime(2024, 9, 19, 0, 0),
                                    "value": 56.7,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 18, 0, 0),
                                    "start": datetime.datetime(2024, 9, 18, 0, 0),
                                    "value": 52.55,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 17, 0, 0),
                                    "start": datetime.datetime(2024, 9, 17, 0, 0),
                                    "value": 125.37,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 16, 0, 0),
                                    "start": datetime.datetime(2024, 9, 16, 0, 0),
                                    "value": 174.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 15, 0, 0),
                                    "start": datetime.datetime(2024, 9, 15, 0, 0),
                                    "value": 92.76,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 14, 0, 0),
                                    "start": datetime.datetime(2024, 9, 14, 0, 0),
                                    "value": 60.81,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 13, 0, 0),
                                    "start": datetime.datetime(2024, 9, 13, 0, 0),
                                    "value": 196.48,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 12, 0, 0),
                                    "start": datetime.datetime(2024, 9, 12, 0, 0),
                                    "value": 115.83,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 11, 0, 0),
                                    "start": datetime.datetime(2024, 9, 11, 0, 0),
                                    "value": 41.49,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 10, 0, 0),
                                    "start": datetime.datetime(2024, 9, 10, 0, 0),
                                    "value": 0.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 9, 0, 0),
                                    "start": datetime.datetime(2024, 9, 9, 0, 0),
                                    "value": 1.42,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 8, 0, 0),
                                    "start": datetime.datetime(2024, 9, 8, 0, 0),
                                    "value": 14.26,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 7, 0, 0),
                                    "start": datetime.datetime(2024, 9, 7, 0, 0),
                                    "value": 18.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 6, 0, 0),
                                    "start": datetime.datetime(2024, 9, 6, 0, 0),
                                    "value": 36.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 5, 0, 0),
                                    "start": datetime.datetime(2024, 9, 5, 0, 0),
                                    "value": 74.71,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 4, 0, 0),
                                    "start": datetime.datetime(2024, 9, 4, 0, 0),
                                    "value": 77.24,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 3, 0, 0),
                                    "start": datetime.datetime(2024, 9, 3, 0, 0),
                                    "value": 67.86,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 2, 0, 0),
                                    "start": datetime.datetime(2024, 9, 2, 0, 0),
                                    "value": 23.9,
                                },
                                {
                                    "end": datetime.datetime(2024, 9, 1, 0, 0),
                                    "start": datetime.datetime(2024, 9, 1, 0, 0),
                                    "value": 8.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 31, 0, 0),
                                    "start": datetime.datetime(2024, 8, 31, 0, 0),
                                    "value": 8.32,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 30, 0, 0),
                                    "start": datetime.datetime(2024, 8, 30, 0, 0),
                                    "value": 2.2,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 29, 0, 0),
                                    "start": datetime.datetime(2024, 8, 29, 0, 0),
                                    "value": 21.94,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 28, 0, 0),
                                    "start": datetime.datetime(2024, 8, 28, 0, 0),
                                    "value": 3.45,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 27, 0, 0),
                                    "start": datetime.datetime(2024, 8, 27, 0, 0),
                                    "value": 2.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 26, 0, 0),
                                    "start": datetime.datetime(2024, 8, 26, 0, 0),
                                    "value": -0.48,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 25, 0, 0),
                                    "start": datetime.datetime(2024, 8, 25, 0, 0),
                                    "value": -4.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 24, 0, 0),
                                    "start": datetime.datetime(2024, 8, 24, 0, 0),
                                    "value": -5.24,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 23, 0, 0),
                                    "start": datetime.datetime(2024, 8, 23, 0, 0),
                                    "value": 23.4,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 22, 0, 0),
                                    "start": datetime.datetime(2024, 8, 22, 0, 0),
                                    "value": 4.33,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 21, 0, 0),
                                    "start": datetime.datetime(2024, 8, 21, 0, 0),
                                    "value": 2.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 20, 0, 0),
                                    "start": datetime.datetime(2024, 8, 20, 0, 0),
                                    "value": 12.01,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 19, 0, 0),
                                    "start": datetime.datetime(2024, 8, 19, 0, 0),
                                    "value": 7.96,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 18, 0, 0),
                                    "start": datetime.datetime(2024, 8, 18, 0, 0),
                                    "value": 19.64,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 17, 0, 0),
                                    "start": datetime.datetime(2024, 8, 17, 0, 0),
                                    "value": 35.99,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 16, 0, 0),
                                    "start": datetime.datetime(2024, 8, 16, 0, 0),
                                    "value": 7.93,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 15, 0, 0),
                                    "start": datetime.datetime(2024, 8, 15, 0, 0),
                                    "value": 8.71,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 14, 0, 0),
                                    "start": datetime.datetime(2024, 8, 14, 0, 0),
                                    "value": 54.26,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 13, 0, 0),
                                    "start": datetime.datetime(2024, 8, 13, 0, 0),
                                    "value": 21.4,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 12, 0, 0),
                                    "start": datetime.datetime(2024, 8, 12, 0, 0),
                                    "value": 13.89,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 11, 0, 0),
                                    "start": datetime.datetime(2024, 8, 11, 0, 0),
                                    "value": -1.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 10, 0, 0),
                                    "start": datetime.datetime(2024, 8, 10, 0, 0),
                                    "value": -2.71,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 9, 0, 0),
                                    "start": datetime.datetime(2024, 8, 9, 0, 0),
                                    "value": 4.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 8, 0, 0),
                                    "start": datetime.datetime(2024, 8, 8, 0, 0),
                                    "value": 9.24,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 7, 0, 0),
                                    "start": datetime.datetime(2024, 8, 7, 0, 0),
                                    "value": 17.06,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 6, 0, 0),
                                    "start": datetime.datetime(2024, 8, 6, 0, 0),
                                    "value": 22.15,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 5, 0, 0),
                                    "start": datetime.datetime(2024, 8, 5, 0, 0),
                                    "value": 25.03,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 4, 0, 0),
                                    "start": datetime.datetime(2024, 8, 4, 0, 0),
                                    "value": 17.07,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 3, 0, 0),
                                    "start": datetime.datetime(2024, 8, 3, 0, 0),
                                    "value": 17.18,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 2, 0, 0),
                                    "start": datetime.datetime(2024, 8, 2, 0, 0),
                                    "value": 14.48,
                                },
                                {
                                    "end": datetime.datetime(2024, 8, 1, 0, 0),
                                    "start": datetime.datetime(2024, 8, 1, 0, 0),
                                    "value": 25.6,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 31, 0, 0),
                                    "start": datetime.datetime(2024, 7, 31, 0, 0),
                                    "value": 19.25,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 30, 0, 0),
                                    "start": datetime.datetime(2024, 7, 30, 0, 0),
                                    "value": 13.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 29, 0, 0),
                                    "start": datetime.datetime(2024, 7, 29, 0, 0),
                                    "value": 10.47,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 28, 0, 0),
                                    "start": datetime.datetime(2024, 7, 28, 0, 0),
                                    "value": 19.11,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 27, 0, 0),
                                    "start": datetime.datetime(2024, 7, 27, 0, 0),
                                    "value": 20.63,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 26, 0, 0),
                                    "start": datetime.datetime(2024, 7, 26, 0, 0),
                                    "value": 21.08,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 25, 0, 0),
                                    "start": datetime.datetime(2024, 7, 25, 0, 0),
                                    "value": 23.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 24, 0, 0),
                                    "start": datetime.datetime(2024, 7, 24, 0, 0),
                                    "value": 30.76,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 23, 0, 0),
                                    "start": datetime.datetime(2024, 7, 23, 0, 0),
                                    "value": 19.74,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 22, 0, 0),
                                    "start": datetime.datetime(2024, 7, 22, 0, 0),
                                    "value": 23.63,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 21, 0, 0),
                                    "start": datetime.datetime(2024, 7, 21, 0, 0),
                                    "value": 15.56,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 20, 0, 0),
                                    "start": datetime.datetime(2024, 7, 20, 0, 0),
                                    "value": 16.02,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 19, 0, 0),
                                    "start": datetime.datetime(2024, 7, 19, 0, 0),
                                    "value": 17.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 18, 0, 0),
                                    "start": datetime.datetime(2024, 7, 18, 0, 0),
                                    "value": 12.52,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 17, 0, 0),
                                    "start": datetime.datetime(2024, 7, 17, 0, 0),
                                    "value": 9.57,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 16, 0, 0),
                                    "start": datetime.datetime(2024, 7, 16, 0, 0),
                                    "value": 24.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 15, 0, 0),
                                    "start": datetime.datetime(2024, 7, 15, 0, 0),
                                    "value": 22.23,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 14, 0, 0),
                                    "start": datetime.datetime(2024, 7, 14, 0, 0),
                                    "value": 3.29,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 13, 0, 0),
                                    "start": datetime.datetime(2024, 7, 13, 0, 0),
                                    "value": 11.16,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 12, 0, 0),
                                    "start": datetime.datetime(2024, 7, 12, 0, 0),
                                    "value": 24.33,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 11, 0, 0),
                                    "start": datetime.datetime(2024, 7, 11, 0, 0),
                                    "value": -1.46,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 10, 0, 0),
                                    "start": datetime.datetime(2024, 7, 10, 0, 0),
                                    "value": 21.7,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 9, 0, 0),
                                    "start": datetime.datetime(2024, 7, 9, 0, 0),
                                    "value": 24.64,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 8, 0, 0),
                                    "start": datetime.datetime(2024, 7, 8, 0, 0),
                                    "value": 1.19,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 7, 0, 0),
                                    "start": datetime.datetime(2024, 7, 7, 0, 0),
                                    "value": -5.03,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 6, 0, 0),
                                    "start": datetime.datetime(2024, 7, 6, 0, 0),
                                    "value": 1.34,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 5, 0, 0),
                                    "start": datetime.datetime(2024, 7, 5, 0, 0),
                                    "value": 11.06,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 4, 0, 0),
                                    "start": datetime.datetime(2024, 7, 4, 0, 0),
                                    "value": 15.95,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 3, 0, 0),
                                    "start": datetime.datetime(2024, 7, 3, 0, 0),
                                    "value": 32.32,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 2, 0, 0),
                                    "start": datetime.datetime(2024, 7, 2, 0, 0),
                                    "value": 27.55,
                                },
                                {
                                    "end": datetime.datetime(2024, 7, 1, 0, 0),
                                    "start": datetime.datetime(2024, 7, 1, 0, 0),
                                    "value": 32.35,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 30, 0, 0),
                                    "start": datetime.datetime(2024, 6, 30, 0, 0),
                                    "value": 12.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 29, 0, 0),
                                    "start": datetime.datetime(2024, 6, 29, 0, 0),
                                    "value": -0.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 28, 0, 0),
                                    "start": datetime.datetime(2024, 6, 28, 0, 0),
                                    "value": 7.9,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 27, 0, 0),
                                    "start": datetime.datetime(2024, 6, 27, 0, 0),
                                    "value": 26.85,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 26, 0, 0),
                                    "start": datetime.datetime(2024, 6, 26, 0, 0),
                                    "value": 26.17,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 25, 0, 0),
                                    "start": datetime.datetime(2024, 6, 25, 0, 0),
                                    "value": 31.16,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 24, 0, 0),
                                    "start": datetime.datetime(2024, 6, 24, 0, 0),
                                    "value": 30.92,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 23, 0, 0),
                                    "start": datetime.datetime(2024, 6, 23, 0, 0),
                                    "value": 13.55,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 22, 0, 0),
                                    "start": datetime.datetime(2024, 6, 22, 0, 0),
                                    "value": 16.54,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 21, 0, 0),
                                    "start": datetime.datetime(2024, 6, 21, 0, 0),
                                    "value": -0.98,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 20, 0, 0),
                                    "start": datetime.datetime(2024, 6, 20, 0, 0),
                                    "value": 2.93,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 19, 0, 0),
                                    "start": datetime.datetime(2024, 6, 19, 0, 0),
                                    "value": 26.3,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 18, 0, 0),
                                    "start": datetime.datetime(2024, 6, 18, 0, 0),
                                    "value": 47.38,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 17, 0, 0),
                                    "start": datetime.datetime(2024, 6, 17, 0, 0),
                                    "value": 64.21,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 16, 0, 0),
                                    "start": datetime.datetime(2024, 6, 16, 0, 0),
                                    "value": 12.33,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 15, 0, 0),
                                    "start": datetime.datetime(2024, 6, 15, 0, 0),
                                    "value": 18.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 14, 0, 0),
                                    "start": datetime.datetime(2024, 6, 14, 0, 0),
                                    "value": 84.86,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 13, 0, 0),
                                    "start": datetime.datetime(2024, 6, 13, 0, 0),
                                    "value": 122.68,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 12, 0, 0),
                                    "start": datetime.datetime(2024, 6, 12, 0, 0),
                                    "value": 82.28,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 11, 0, 0),
                                    "start": datetime.datetime(2024, 6, 11, 0, 0),
                                    "value": 62.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 10, 0, 0),
                                    "start": datetime.datetime(2024, 6, 10, 0, 0),
                                    "value": 38.45,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 9, 0, 0),
                                    "start": datetime.datetime(2024, 6, 9, 0, 0),
                                    "value": 3.96,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 8, 0, 0),
                                    "start": datetime.datetime(2024, 6, 8, 0, 0),
                                    "value": 22.49,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 7, 0, 0),
                                    "start": datetime.datetime(2024, 6, 7, 0, 0),
                                    "value": 64.64,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 6, 0, 0),
                                    "start": datetime.datetime(2024, 6, 6, 0, 0),
                                    "value": 18.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 5, 0, 0),
                                    "start": datetime.datetime(2024, 6, 5, 0, 0),
                                    "value": 22.45,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 4, 0, 0),
                                    "start": datetime.datetime(2024, 6, 4, 0, 0),
                                    "value": 94.89,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 3, 0, 0),
                                    "start": datetime.datetime(2024, 6, 3, 0, 0),
                                    "value": 82.47,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 2, 0, 0),
                                    "start": datetime.datetime(2024, 6, 2, 0, 0),
                                    "value": 25.94,
                                },
                                {
                                    "end": datetime.datetime(2024, 6, 1, 0, 0),
                                    "start": datetime.datetime(2024, 6, 1, 0, 0),
                                    "value": 20.9,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 31, 0, 0),
                                    "start": datetime.datetime(2024, 5, 31, 0, 0),
                                    "value": 55.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 30, 0, 0),
                                    "start": datetime.datetime(2024, 5, 30, 0, 0),
                                    "value": 92.69,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 29, 0, 0),
                                    "start": datetime.datetime(2024, 5, 29, 0, 0),
                                    "value": 57.17,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 28, 0, 0),
                                    "start": datetime.datetime(2024, 5, 28, 0, 0),
                                    "value": 4.81,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 27, 0, 0),
                                    "start": datetime.datetime(2024, 5, 27, 0, 0),
                                    "value": 2.47,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 26, 0, 0),
                                    "start": datetime.datetime(2024, 5, 26, 0, 0),
                                    "value": 2.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 25, 0, 0),
                                    "start": datetime.datetime(2024, 5, 25, 0, 0),
                                    "value": 9.1,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 24, 0, 0),
                                    "start": datetime.datetime(2024, 5, 24, 0, 0),
                                    "value": 17.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 23, 0, 0),
                                    "start": datetime.datetime(2024, 5, 23, 0, 0),
                                    "value": 3.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 22, 0, 0),
                                    "start": datetime.datetime(2024, 5, 22, 0, 0),
                                    "value": 10.08,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 21, 0, 0),
                                    "start": datetime.datetime(2024, 5, 21, 0, 0),
                                    "value": 23.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 20, 0, 0),
                                    "start": datetime.datetime(2024, 5, 20, 0, 0),
                                    "value": 13.85,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 19, 0, 0),
                                    "start": datetime.datetime(2024, 5, 19, 0, 0),
                                    "value": -2.4,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 18, 0, 0),
                                    "start": datetime.datetime(2024, 5, 18, 0, 0),
                                    "value": -1.66,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 17, 0, 0),
                                    "start": datetime.datetime(2024, 5, 17, 0, 0),
                                    "value": 11.65,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 16, 0, 0),
                                    "start": datetime.datetime(2024, 5, 16, 0, 0),
                                    "value": 51.85,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 15, 0, 0),
                                    "start": datetime.datetime(2024, 5, 15, 0, 0),
                                    "value": 6.41,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 14, 0, 0),
                                    "start": datetime.datetime(2024, 5, 14, 0, 0),
                                    "value": 25.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 13, 0, 0),
                                    "start": datetime.datetime(2024, 5, 13, 0, 0),
                                    "value": 121.18,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 12, 0, 0),
                                    "start": datetime.datetime(2024, 5, 12, 0, 0),
                                    "value": 18.98,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 11, 0, 0),
                                    "start": datetime.datetime(2024, 5, 11, 0, 0),
                                    "value": 13.67,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 10, 0, 0),
                                    "start": datetime.datetime(2024, 5, 10, 0, 0),
                                    "value": 5.7,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 9, 0, 0),
                                    "start": datetime.datetime(2024, 5, 9, 0, 0),
                                    "value": 26.53,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 8, 0, 0),
                                    "start": datetime.datetime(2024, 5, 8, 0, 0),
                                    "value": 136.24,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 7, 0, 0),
                                    "start": datetime.datetime(2024, 5, 7, 0, 0),
                                    "value": 67.13,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 6, 0, 0),
                                    "start": datetime.datetime(2024, 5, 6, 0, 0),
                                    "value": 57.71,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 5, 0, 0),
                                    "start": datetime.datetime(2024, 5, 5, 0, 0),
                                    "value": 23.16,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 4, 0, 0),
                                    "start": datetime.datetime(2024, 5, 4, 0, 0),
                                    "value": 26.21,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 3, 0, 0),
                                    "start": datetime.datetime(2024, 5, 3, 0, 0),
                                    "value": 48.87,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 2, 0, 0),
                                    "start": datetime.datetime(2024, 5, 2, 0, 0),
                                    "value": 125.87,
                                },
                                {
                                    "end": datetime.datetime(2024, 5, 1, 0, 0),
                                    "start": datetime.datetime(2024, 5, 1, 0, 0),
                                    "value": 33.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 30, 0, 0),
                                    "start": datetime.datetime(2024, 4, 30, 0, 0),
                                    "value": 55.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 29, 0, 0),
                                    "start": datetime.datetime(2024, 4, 29, 0, 0),
                                    "value": 44.04,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 28, 0, 0),
                                    "start": datetime.datetime(2024, 4, 28, 0, 0),
                                    "value": 45.1,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 27, 0, 0),
                                    "start": datetime.datetime(2024, 4, 27, 0, 0),
                                    "value": 66.86,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 26, 0, 0),
                                    "start": datetime.datetime(2024, 4, 26, 0, 0),
                                    "value": 97.11,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 25, 0, 0),
                                    "start": datetime.datetime(2024, 4, 25, 0, 0),
                                    "value": 86.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 24, 0, 0),
                                    "start": datetime.datetime(2024, 4, 24, 0, 0),
                                    "value": 98.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 23, 0, 0),
                                    "start": datetime.datetime(2024, 4, 23, 0, 0),
                                    "value": 69.39,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 22, 0, 0),
                                    "start": datetime.datetime(2024, 4, 22, 0, 0),
                                    "value": 71.24,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 21, 0, 0),
                                    "start": datetime.datetime(2024, 4, 21, 0, 0),
                                    "value": 60.74,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 20, 0, 0),
                                    "start": datetime.datetime(2024, 4, 20, 0, 0),
                                    "value": 38.76,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 19, 0, 0),
                                    "start": datetime.datetime(2024, 4, 19, 0, 0),
                                    "value": 57.2,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 18, 0, 0),
                                    "start": datetime.datetime(2024, 4, 18, 0, 0),
                                    "value": 88.56,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 17, 0, 0),
                                    "start": datetime.datetime(2024, 4, 17, 0, 0),
                                    "value": 78.74,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 16, 0, 0),
                                    "start": datetime.datetime(2024, 4, 16, 0, 0),
                                    "value": 52.92,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 15, 0, 0),
                                    "start": datetime.datetime(2024, 4, 15, 0, 0),
                                    "value": 34.81,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 14, 0, 0),
                                    "start": datetime.datetime(2024, 4, 14, 0, 0),
                                    "value": 12.95,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 13, 0, 0),
                                    "start": datetime.datetime(2024, 4, 13, 0, 0),
                                    "value": 8.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 12, 0, 0),
                                    "start": datetime.datetime(2024, 4, 12, 0, 0),
                                    "value": 29.84,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 11, 0, 0),
                                    "start": datetime.datetime(2024, 4, 11, 0, 0),
                                    "value": 5.01,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 10, 0, 0),
                                    "start": datetime.datetime(2024, 4, 10, 0, 0),
                                    "value": 1.3,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 9, 0, 0),
                                    "start": datetime.datetime(2024, 4, 9, 0, 0),
                                    "value": 47.29,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 8, 0, 0),
                                    "start": datetime.datetime(2024, 4, 8, 0, 0),
                                    "value": 37.1,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 7, 0, 0),
                                    "start": datetime.datetime(2024, 4, 7, 0, 0),
                                    "value": 4.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 6, 0, 0),
                                    "start": datetime.datetime(2024, 4, 6, 0, 0),
                                    "value": 46.28,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 5, 0, 0),
                                    "start": datetime.datetime(2024, 4, 5, 0, 0),
                                    "value": 47.58,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 4, 0, 0),
                                    "start": datetime.datetime(2024, 4, 4, 0, 0),
                                    "value": 80.18,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 3, 0, 0),
                                    "start": datetime.datetime(2024, 4, 3, 0, 0),
                                    "value": 44.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 2, 0, 0),
                                    "start": datetime.datetime(2024, 4, 2, 0, 0),
                                    "value": 28.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 4, 1, 0, 0),
                                    "start": datetime.datetime(2024, 4, 1, 0, 0),
                                    "value": 27.69,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 31, 0, 0),
                                    "start": datetime.datetime(2024, 3, 31, 0, 0),
                                    "value": 44.3,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 30, 0, 0),
                                    "start": datetime.datetime(2024, 3, 30, 0, 0),
                                    "value": 40.71,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 29, 0, 0),
                                    "start": datetime.datetime(2024, 3, 29, 0, 0),
                                    "value": 24.06,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 28, 0, 0),
                                    "start": datetime.datetime(2024, 3, 28, 0, 0),
                                    "value": 38.36,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 27, 0, 0),
                                    "start": datetime.datetime(2024, 3, 27, 0, 0),
                                    "value": 47.89,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 26, 0, 0),
                                    "start": datetime.datetime(2024, 3, 26, 0, 0),
                                    "value": 88.43,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 25, 0, 0),
                                    "start": datetime.datetime(2024, 3, 25, 0, 0),
                                    "value": 91.4,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 24, 0, 0),
                                    "start": datetime.datetime(2024, 3, 24, 0, 0),
                                    "value": 49.27,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 23, 0, 0),
                                    "start": datetime.datetime(2024, 3, 23, 0, 0),
                                    "value": 35.11,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 22, 0, 0),
                                    "start": datetime.datetime(2024, 3, 22, 0, 0),
                                    "value": 47.06,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 21, 0, 0),
                                    "start": datetime.datetime(2024, 3, 21, 0, 0),
                                    "value": 82.63,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 20, 0, 0),
                                    "start": datetime.datetime(2024, 3, 20, 0, 0),
                                    "value": 64.73,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 19, 0, 0),
                                    "start": datetime.datetime(2024, 3, 19, 0, 0),
                                    "value": 57.6,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 18, 0, 0),
                                    "start": datetime.datetime(2024, 3, 18, 0, 0),
                                    "value": 55.41,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 17, 0, 0),
                                    "start": datetime.datetime(2024, 3, 17, 0, 0),
                                    "value": 49.01,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 16, 0, 0),
                                    "start": datetime.datetime(2024, 3, 16, 0, 0),
                                    "value": 32.74,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 15, 0, 0),
                                    "start": datetime.datetime(2024, 3, 15, 0, 0),
                                    "value": 33.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 14, 0, 0),
                                    "start": datetime.datetime(2024, 3, 14, 0, 0),
                                    "value": 21.14,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 13, 0, 0),
                                    "start": datetime.datetime(2024, 3, 13, 0, 0),
                                    "value": 69.44,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 12, 0, 0),
                                    "start": datetime.datetime(2024, 3, 12, 0, 0),
                                    "value": 74.83,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 11, 0, 0),
                                    "start": datetime.datetime(2024, 3, 11, 0, 0),
                                    "value": 66.26,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 10, 0, 0),
                                    "start": datetime.datetime(2024, 3, 10, 0, 0),
                                    "value": 66.05,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 9, 0, 0),
                                    "start": datetime.datetime(2024, 3, 9, 0, 0),
                                    "value": 78.63,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 8, 0, 0),
                                    "start": datetime.datetime(2024, 3, 8, 0, 0),
                                    "value": 85.55,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 7, 0, 0),
                                    "start": datetime.datetime(2024, 3, 7, 0, 0),
                                    "value": 93.09,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 6, 0, 0),
                                    "start": datetime.datetime(2024, 3, 6, 0, 0),
                                    "value": 85.37,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 5, 0, 0),
                                    "start": datetime.datetime(2024, 3, 5, 0, 0),
                                    "value": 88.23,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 4, 0, 0),
                                    "start": datetime.datetime(2024, 3, 4, 0, 0),
                                    "value": 93.5,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 3, 0, 0),
                                    "start": datetime.datetime(2024, 3, 3, 0, 0),
                                    "value": 69,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 2, 0, 0),
                                    "start": datetime.datetime(2024, 3, 2, 0, 0),
                                    "value": 45.41,
                                },
                                {
                                    "end": datetime.datetime(2024, 3, 1, 0, 0),
                                    "start": datetime.datetime(2024, 3, 1, 0, 0),
                                    "value": 21.82,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 29, 0, 0),
                                    "start": datetime.datetime(2024, 2, 29, 0, 0),
                                    "value": 13.28,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 28, 0, 0),
                                    "start": datetime.datetime(2024, 2, 28, 0, 0),
                                    "value": 21.22,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 27, 0, 0),
                                    "start": datetime.datetime(2024, 2, 27, 0, 0),
                                    "value": 61.95,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 26, 0, 0),
                                    "start": datetime.datetime(2024, 2, 26, 0, 0),
                                    "value": 48.11,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 25, 0, 0),
                                    "start": datetime.datetime(2024, 2, 25, 0, 0),
                                    "value": 31.64,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 24, 0, 0),
                                    "start": datetime.datetime(2024, 2, 24, 0, 0),
                                    "value": 24.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 23, 0, 0),
                                    "start": datetime.datetime(2024, 2, 23, 0, 0),
                                    "value": 3.41,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 22, 0, 0),
                                    "start": datetime.datetime(2024, 2, 22, 0, 0),
                                    "value": 38.43,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 21, 0, 0),
                                    "start": datetime.datetime(2024, 2, 21, 0, 0),
                                    "value": 46.85,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 20, 0, 0),
                                    "start": datetime.datetime(2024, 2, 20, 0, 0),
                                    "value": 67.49,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 19, 0, 0),
                                    "start": datetime.datetime(2024, 2, 19, 0, 0),
                                    "value": 64.36,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 18, 0, 0),
                                    "start": datetime.datetime(2024, 2, 18, 0, 0),
                                    "value": 38.18,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 17, 0, 0),
                                    "start": datetime.datetime(2024, 2, 17, 0, 0),
                                    "value": 19.17,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 16, 0, 0),
                                    "start": datetime.datetime(2024, 2, 16, 0, 0),
                                    "value": 32.43,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 15, 0, 0),
                                    "start": datetime.datetime(2024, 2, 15, 0, 0),
                                    "value": 62.21,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 14, 0, 0),
                                    "start": datetime.datetime(2024, 2, 14, 0, 0),
                                    "value": 43.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 13, 0, 0),
                                    "start": datetime.datetime(2024, 2, 13, 0, 0),
                                    "value": 47.91,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 12, 0, 0),
                                    "start": datetime.datetime(2024, 2, 12, 0, 0),
                                    "value": 74.13,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 11, 0, 0),
                                    "start": datetime.datetime(2024, 2, 11, 0, 0),
                                    "value": 64.8,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 10, 0, 0),
                                    "start": datetime.datetime(2024, 2, 10, 0, 0),
                                    "value": 116.91,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 9, 0, 0),
                                    "start": datetime.datetime(2024, 2, 9, 0, 0),
                                    "value": 152.17,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 8, 0, 0),
                                    "start": datetime.datetime(2024, 2, 8, 0, 0),
                                    "value": 112.39,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 7, 0, 0),
                                    "start": datetime.datetime(2024, 2, 7, 0, 0),
                                    "value": 111.62,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 6, 0, 0),
                                    "start": datetime.datetime(2024, 2, 6, 0, 0),
                                    "value": 122.47,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 5, 0, 0),
                                    "start": datetime.datetime(2024, 2, 5, 0, 0),
                                    "value": 47.43,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 4, 0, 0),
                                    "start": datetime.datetime(2024, 2, 4, 0, 0),
                                    "value": 13.5,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 3, 0, 0),
                                    "start": datetime.datetime(2024, 2, 3, 0, 0),
                                    "value": 0.97,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 2, 0, 0),
                                    "start": datetime.datetime(2024, 2, 2, 0, 0),
                                    "value": 13.59,
                                },
                                {
                                    "end": datetime.datetime(2024, 2, 1, 0, 0),
                                    "start": datetime.datetime(2024, 2, 1, 0, 0),
                                    "value": 0.94,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 31, 0, 0),
                                    "start": datetime.datetime(2024, 1, 31, 0, 0),
                                    "value": 16.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 30, 0, 0),
                                    "start": datetime.datetime(2024, 1, 30, 0, 0),
                                    "value": 19.17,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 29, 0, 0),
                                    "start": datetime.datetime(2024, 1, 29, 0, 0),
                                    "value": 12.57,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 28, 0, 0),
                                    "start": datetime.datetime(2024, 1, 28, 0, 0),
                                    "value": 12.35,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 27, 0, 0),
                                    "start": datetime.datetime(2024, 1, 27, 0, 0),
                                    "value": 17.8,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 26, 0, 0),
                                    "start": datetime.datetime(2024, 1, 26, 0, 0),
                                    "value": 78.84,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 25, 0, 0),
                                    "start": datetime.datetime(2024, 1, 25, 0, 0),
                                    "value": 78.08,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 24, 0, 0),
                                    "start": datetime.datetime(2024, 1, 24, 0, 0),
                                    "value": 74.77,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 23, 0, 0),
                                    "start": datetime.datetime(2024, 1, 23, 0, 0),
                                    "value": 33.65,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 22, 0, 0),
                                    "start": datetime.datetime(2024, 1, 22, 0, 0),
                                    "value": 26.78,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 21, 0, 0),
                                    "start": datetime.datetime(2024, 1, 21, 0, 0),
                                    "value": 35.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 20, 0, 0),
                                    "start": datetime.datetime(2024, 1, 20, 0, 0),
                                    "value": 83.5,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 19, 0, 0),
                                    "start": datetime.datetime(2024, 1, 19, 0, 0),
                                    "value": 84.33,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 18, 0, 0),
                                    "start": datetime.datetime(2024, 1, 18, 0, 0),
                                    "value": 82.37,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 17, 0, 0),
                                    "start": datetime.datetime(2024, 1, 17, 0, 0),
                                    "value": 110.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 16, 0, 0),
                                    "start": datetime.datetime(2024, 1, 16, 0, 0),
                                    "value": 148.55,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 15, 0, 0),
                                    "start": datetime.datetime(2024, 1, 15, 0, 0),
                                    "value": 98.88,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 14, 0, 0),
                                    "start": datetime.datetime(2024, 1, 14, 0, 0),
                                    "value": 75.95,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 13, 0, 0),
                                    "start": datetime.datetime(2024, 1, 13, 0, 0),
                                    "value": 59.07,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 12, 0, 0),
                                    "start": datetime.datetime(2024, 1, 12, 0, 0),
                                    "value": 130.51,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 11, 0, 0),
                                    "start": datetime.datetime(2024, 1, 11, 0, 0),
                                    "value": 88.4,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 10, 0, 0),
                                    "start": datetime.datetime(2024, 1, 10, 0, 0),
                                    "value": 41.76,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 9, 0, 0),
                                    "start": datetime.datetime(2024, 1, 9, 0, 0),
                                    "value": 72.67,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 8, 0, 0),
                                    "start": datetime.datetime(2024, 1, 8, 0, 0),
                                    "value": 111.32,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 7, 0, 0),
                                    "start": datetime.datetime(2024, 1, 7, 0, 0),
                                    "value": 95.31,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 6, 0, 0),
                                    "start": datetime.datetime(2024, 1, 6, 0, 0),
                                    "value": 167.33,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 5, 0, 0),
                                    "start": datetime.datetime(2024, 1, 5, 0, 0),
                                    "value": 890.54,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 4, 0, 0),
                                    "start": datetime.datetime(2024, 1, 4, 0, 0),
                                    "value": 228.12,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 3, 0, 0),
                                    "start": datetime.datetime(2024, 1, 3, 0, 0),
                                    "value": 98.97,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 2, 0, 0),
                                    "start": datetime.datetime(2024, 1, 2, 0, 0),
                                    "value": 173.56,
                                },
                                {
                                    "end": datetime.datetime(2024, 1, 1, 0, 0),
                                    "start": datetime.datetime(2024, 1, 1, 0, 0),
                                    "value": 45.25,
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
