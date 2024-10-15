# pylint: disable=missing-module-docstring
from dateutil.parser import parse as parse_dt
from pytz import timezone, utc


class CurrencyMismatch(ValueError):  # pylint: disable=missing-class-docstring
    pass


class Base:  # pylint: disable=too-few-public-methods
    """Class for fetching Nord Pool Elspot prices."""

    def __init__(self, currency="EUR", timeout=None):
        self.currency = currency
        self.timeout = timeout or 2

    def _parse_dt(self, time_str):
        """Parse datetimes to UTC from Stockholm time, which Nord Pool uses."""
        time = parse_dt(time_str)
        if time.tzinfo is None:
            return timezone("Europe/Stockholm").localize(time).astimezone(utc)
        return time

    def _conv_to_float(self, s):
        """Convert numbers to float. Return infinity, if conversion fails."""
        try:
            return float(s.replace(",", ".").replace(" ", ""))
        except ValueError:
            return float("inf")
