#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot

# Initialize class for fetching Elspot prices
prices = elspot.Prices()
# Fetch hourly prices for Finland and print the resulting dictionary
print(prices.hourly(areas=['FI']))
