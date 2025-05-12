# nordpool

![Test Status](https://github.com/kipe/nordpool/actions/workflows/python-test.yml/badge.svg?branch=main)

Python library for fetching Nord Pool Elspot prices.

## Python version

The minimum supported Python version is 3.9, which receives security updates until [2025-10](https://devguide.python.org/versions/).
The library won't install without trickery on older versions, so update your Python.

## Installing

To install from [PyPi](https://pypi.org/project/nordpool/), use

`pip install nordpool`

## To upgrade

To upgrade installation from [PyPi](https://pypi.org/project/nordpool/), use

`pip install -U nordpool`

## Usage example

Below is a very basic example of the library usage. More advanced example(s) can be found in `examples` -directory.

```python
from pprint import pprint
from nordpool import elspot

# Initialize class for fetching the prices.
# An optional currency parameter can be provided, default is EUR.
prices_spot = elspot.Prices()

# Fetch tomorrow's prices for Finland and print the resulting dictionary.
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.fetch(areas=["FI"]))
```

Output:
```python
{
  "areas": {
    "FI": {
      "values": [
        {
          "end": datetime.datetime(2025, 5, 12, 23, 0, tzinfo=tzutc()),
          "start": datetime.datetime(2025, 5, 12, 22, 0, tzinfo=tzutc()),
          "value": 5.11,
        },
        {
          "end": datetime.datetime(2025, 5, 13, 0, 0, tzinfo=tzutc()),
          "start": datetime.datetime(2025, 5, 12, 23, 0, tzinfo=tzutc()),
          "value": 5.8,
        },
        {
          "end": datetime.datetime(2025, 5, 13, 1, 0, tzinfo=tzutc()),
          "start": datetime.datetime(2025, 5, 13, 0, 0, tzinfo=tzutc()),
          "value": 4.51,
        },
# ... SNIP ...
        {
          "end": datetime.datetime(2025, 5, 13, 22, 0, tzinfo=tzutc()),
          "start": datetime.datetime(2025, 5, 13, 21, 0, tzinfo=tzutc()),
          "value": -10.24,
        },
      ]
    }
  },
  "currency": "EUR",
  "end": datetime.datetime(2025, 5, 13, 22, 0, tzinfo=tzutc()),
  "start": datetime.datetime(2025, 5, 12, 22, 0, tzinfo=tzutc()),
  "updated": datetime.datetime(2025, 5, 12, 11, 26, 3, 811220, tzinfo=tzutc()),
}
```
