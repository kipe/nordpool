nordpool 
========

Python library for Nordpool fetching spot prices.


#### Installing bleeding edge version from GitHub

##### Installation
`pip install git+https://github.com/kipe/nordpool.git`

##### Upgrading
`pip install -U git+https://github.com/kipe/nordpool.git`


#### Example
```
# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices = elspot.Prices()
# Fetch hourly prices for Finland and print the resulting dictionary
pprint(prices.hourly(areas=['FI']))
```
