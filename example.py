#!/usr/bin/env python
from nordpool import elspot
from pprint import pprint

prices = elspot.Prices()
pprint(prices.hourly(areas=['FI']))
