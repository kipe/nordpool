# pylint: disable=missing-module-docstring


class CurrencyMismatch(ValueError):  # pylint: disable=missing-class-docstring
    pass


class Base:  # pylint: disable=too-few-public-methods
    """Class for fetching Nord Pool Elspot prices."""

    def __init__(self, currency="EUR", timeout=None):
        self.currency = currency
        self.timeout = timeout or 2
