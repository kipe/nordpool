#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices = elspot.Prices()
# Fetch hourly prices for Finland and print the resulting dictionary
pprint(prices.hourly(areas=['FI']))
