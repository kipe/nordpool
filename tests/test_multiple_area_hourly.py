import datetime
import unittest
from nordpool.elspot import Prices
from pytz import utc
from ._utils import vcr


class ElspotTestCase(unittest.TestCase):
    def test_multiple_area_hourly(self):
        with vcr.use_cassette("multiple_area_hourly.yaml"):
            elspot = Prices()
            prices = elspot.fetch(
                elspot.HOURLY,
                end_date="2024-10-15",
                areas=["SE1", "SE2", "SE3", "SE4"],
            )
            self.assertEqual(
                prices,
                elspot.hourly("2024-10-15", areas=["SE1", "SE2", "SE3", "SE4"]),
            )
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
                                    "value": 8.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 6.62,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 7.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 6.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 10.5,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 14.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "value": 15.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "value": 16.08,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "value": 17.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "value": 19.99,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "value": 21.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "value": 22.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "value": 23.98,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "value": 24.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "value": 24.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "value": 23.19,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "value": 22.17,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "value": 19.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 16.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 15.4,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 15.03,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "value": 14.95,
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
                        },
                        "SE2": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 22, 0, tzinfo=utc
                                    ),
                                    "value": 8.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 6.62,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 7.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 6.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 10.5,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 14.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "value": 15.26,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "value": 16.08,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "value": 17.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "value": 19.99,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "value": 21.78,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "value": 22.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 10, 0, tzinfo=utc
                                    ),
                                    "value": 23.98,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 11, 0, tzinfo=utc
                                    ),
                                    "value": 24.57,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 12, 0, tzinfo=utc
                                    ),
                                    "value": 24.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 13, 0, tzinfo=utc
                                    ),
                                    "value": 23.19,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 14, 0, tzinfo=utc
                                    ),
                                    "value": 22.17,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "value": 19.93,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 16.47,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 15.4,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 15.03,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "value": 14.95,
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
                        },
                        "SE3": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 22, 0, tzinfo=utc
                                    ),
                                    "value": 8.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 6.62,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 7.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 6.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 10.5,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 14.54,
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
                                    "value": 165.65,
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
                                    "value": 48.46,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 60.62,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 61.56,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 48.47,
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
                        },
                        "SE4": {
                            "values": [
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 22, 0, tzinfo=utc
                                    ),
                                    "value": 8.42,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 14, 23, 0, tzinfo=utc
                                    ),
                                    "value": 6.62,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 0, 0, tzinfo=utc
                                    ),
                                    "value": 7.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 1, 0, tzinfo=utc
                                    ),
                                    "value": 6.82,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 2, 0, tzinfo=utc
                                    ),
                                    "value": 10.5,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 3, 0, tzinfo=utc
                                    ),
                                    "value": 14.54,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 4, 0, tzinfo=utc
                                    ),
                                    "value": 50.0,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 5, 0, tzinfo=utc
                                    ),
                                    "value": 180.94,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 6, 0, tzinfo=utc
                                    ),
                                    "value": 172.37,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 7, 0, tzinfo=utc
                                    ),
                                    "value": 107.89,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 9, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 8, 0, tzinfo=utc
                                    ),
                                    "value": 79.89,
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
                                    "value": 76.41,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 15, 0, tzinfo=utc
                                    ),
                                    "value": 117.79,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 16, 0, tzinfo=utc
                                    ),
                                    "value": 133.51,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 17, 0, tzinfo=utc
                                    ),
                                    "value": 94.97,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 18, 0, tzinfo=utc
                                    ),
                                    "value": 74.43,
                                },
                                {
                                    "end": datetime.datetime(
                                        2024, 10, 15, 20, 0, tzinfo=utc
                                    ),
                                    "start": datetime.datetime(
                                        2024, 10, 15, 19, 0, tzinfo=utc
                                    ),
                                    "value": 65.06,
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
                        },
                    },
                    "currency": "EUR",
                    "end": datetime.datetime(2024, 10, 15, 22, 0, tzinfo=utc),
                    "start": datetime.datetime(2024, 10, 14, 22, 0, tzinfo=utc),
                    "updated": datetime.datetime(
                        2024, 10, 14, 11, 17, 2, 811290, tzinfo=utc
                    ),
                },
            )
