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

## Example 1 code

``` python
# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices() # fetch data in Euro

# Fetch Elspot prices and print the resulting dictionary
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.fetch(end_date=datetime.now().date(),areas=['FI'])) # todays hourly prices for Finland
```

#### Example 1 output

```
{'areas': {'FI': {'values': [{'end': datetime.datetime(2025, 5, 10, 23, 0, tzinfo=tzutc()),
                              'start': datetime.datetime(2025, 5, 10, 22, 0, tzinfo=tzutc()),
                              'value': 18.68},
                             {'end': datetime.datetime(2025, 5, 11, 0, 0, tzinfo=tzutc()),
                              'start': datetime.datetime(2025, 5, 10, 23, 0, tzinfo=tzutc()),
                              'value': 25.89},
                             {'end': datetime.datetime(2025, 5, 11, 1, 0, tzinfo=tzutc()),
                              'start': datetime.datetime(2025, 5, 11, 0, 0, tzinfo=tzutc()),
                              'value': 34.04},
                                ... SNIP ...
                             {'end': datetime.datetime(2025, 5, 11, 22, 0, tzinfo=tzutc()),
                              'start': datetime.datetime(2025, 5, 11, 21, 0, tzinfo=tzutc()),
                              'value': 26.35}]}},
 'currency': 'EUR',
 'end': datetime.datetime(2025, 5, 11, 22, 0, tzinfo=tzutc()),
 'start': datetime.datetime(2025, 5, 10, 22, 0, tzinfo=tzutc()),
 'updated': datetime.datetime(2025, 5, 10, 10, 56, 19, 807909, tzinfo=tzutc())}
```

## Example 2 code

``` python
# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint

# Initialize class for fetching Elspot prices
prices_spot = elspot.Prices("SEK") # fetch data in Swedish kronor

# Fetch Elspot prices and print the resulting dictionary
# If the prices are reported as None, it means that the prices fetched aren't yet available.
# The library by default tries to fetch prices for tomorrow and they're released ~13:00 Swedish time.
pprint(prices_spot.fetch(end_date=datetime.now().date(),areas=['SE4']),resolution=15) # todays 15 minutes prices for Sweden area 4

# Get basic info
start = price['start'].strftime('%Y-%m-%d %H:%M')
end = price['end'].strftime('%Y-%m-%d %H:%M')
updated = price['updated'].strftime('%Y-%m-%d %H:%M')
currency = price['currency']

print(f"Energy prices for the period {start} to {end}")
print(f"Last updated: {updated}")
print(f"Currency: {currency}")
print()
# Loop through each area
for area, area_data in price['areas'].items():
    print(f"Area: {area}")
    print("-" * 40)
    for entry in area_data['values']:
        start = entry['start'].strftime('%H:%M')
        end = entry['end'].strftime('%H:%M')
        value = entry['value']
        print(f"{start} - {end}: {value:.2f} {currency}/MWh")
    print()
```

#### Example 2 output

```
Energy prices for the period 2025-05-10 22:00 to 2025-05-11 22:00
Last updated: 2025-05-10 10:56
Currency: SEK

Area: SE4
----------------------------------------
22:00 - 22:15: 1047.69 SEK/MWh
22:15 - 22:30: 1047.69 SEK/MWh
22:30 - 22:45: 1047.69 SEK/MWh
22:45 - 23:00: 1047.69 SEK/MWh
23:00 - 23:15: 1004.63 SEK/MWh
23:15 - 23:30: 1004.63 SEK/MWh
23:30 - 23:45: 1004.63 SEK/MWh
23:45 - 00:00: 1004.63 SEK/MWh
00:00 - 00:15: 1013.16 SEK/MWh
00:15 - 00:30: 1013.16 SEK/MWh
00:30 - 00:45: 1013.16 SEK/MWh
00:45 - 01:00: 1013.16 SEK/MWh
```
