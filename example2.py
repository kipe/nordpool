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
