# nordpool

![Test Status](https://github.com/kipe/nordpool/actions/workflows/python-test.yml/badge.svg?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/kipe/nordpool/badge.svg?branch=main)](https://coveralls.io/github/kipe/nordpool?branch=main)

Python library for fetching Nord Pool Elspot and Elbas prices.

## Python version

The minimum supported Python version is 3.9, which receives security updates until [2025-10](https://devguide.python.org/versions/).
The library won't install without trickery on older versions, so update your Python.

## Installing

To install from [PyPi](https://pypi.org/project/nordpool/), use

`pip install nordpool`

### To upgrade

To upgrade installation from PyPi, use

`pip install -U nordpool`

#### Example

```python
# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices()

# Fetch hourly Elspot prices for Finland and print the resulting dictionary
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.hourly(areas=['FI']))
```

###### Output

```python
{u'areas': {
    u'FI': {
        u'values': [
            {u'end': datetime.datetime(2014, 10, 3, 23, 0, tzinfo=<UTC>),
             u'start': datetime.datetime(2014, 10, 3, 22, 0, tzinfo=<UTC>),
             u'value': 31.2},
            {u'end': datetime.datetime(2014, 10, 4, 0, 0, tzinfo=<UTC>),
             u'start': datetime.datetime(2014, 10, 3, 23, 0, tzinfo=<UTC>),
             u'value': 30.68},
            ... SNIP ...
            {u'end': datetime.datetime(2014, 10, 4, 22, 0, tzinfo=<UTC>),
             u'start': datetime.datetime(2014, 10, 4, 21, 0, tzinfo=<UTC>),
             u'value': 30.82}]}},
 u'currency': u'EUR',
 u'end': datetime.datetime(2014, 10, 4, 22, 0, tzinfo=<UTC>),
 u'start': datetime.datetime(2014, 10, 3, 22, 0, tzinfo=<UTC>),
 u'updated': datetime.datetime(2014, 10, 3, 10, 42, 42, 110000, tzinfo=<UTC>)}
 ...
```
