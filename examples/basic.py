#!/usr/bin/env python

from pprint import pprint
from nordpool import elspot

# Initialize class for fetching the prices.
# An optional currency parameter can be provided, default is EUR.
prices_spot = elspot.Prices()

# Fetch tomorrow's prices for Finland and print the resulting dictionary.
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.fetch(areas=["FI"]))
