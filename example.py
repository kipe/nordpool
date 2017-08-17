#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot, elbas
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Initialize class for fetching Elsbas prices
prices_bas = elbas.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary
pprint(prices_spot.hourly(areas=['FI']))

# Fetch hourly Elbas prices for Finland and print the resulting dictionary
pprint(prices_bas.hourly(areas=['FI']))
