#!/usr/bin/env python

# Import library for fetching Elspot data
from nordpool import elspot, elbas
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Initialize class for fetching Elsbas prices
# prices_bas = elbas.Prices()

# Fetch hourly Elspot prices for SE3 and print the resulting dictionary
pprint(prices_spot.fetch(country='SE', areas=['SE3']))
pprint(prices_spot.fetch(areas=['FI']))

# Fetch hourly Elbas prices for Finland and print the resulting dictionary
# pprint(prices_bas.hourly(areas=['FI']))
