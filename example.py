#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary.
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.hourly(areas=["FI"]))
