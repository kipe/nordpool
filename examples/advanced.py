#! /usr/bin/env python3

# Import library for fetching Elspot data
from datetime import date
from nordpool import elspot

# Initialize class for fetching Elspot prices.
# An optional currency parameter can be provided, default is EUR.
prices_spot = elspot.Prices("SEK")  # Fetch prices in Swedish kronor

# Fetch prices for today in Swedish pricing areas 2 and 4 with 15 minute resolution.
price = prices_spot.fetch(
    # Need to specify end_date to fetch prices for today,
    # as otherwise the library defaults to tomorrow.
    end_date=date.today(),
    # Set areas to fetch the prices for, library defaults to all areas.
    areas=["SE2", "SE4"],
    # Set resolution to 15 minutes, library defaults to 60 minutes.
    resolution=15,
)

# Get basic info about the price data.
# Note: The timestamps are timezone-aware.
start = price["start"].strftime("%Y-%m-%d %H:%M %Z")
end = price["end"].strftime("%Y-%m-%d %H:%M %Z")
updated = price["updated"].strftime("%Y-%m-%d %H:%M %Z")
currency = price["currency"]

print(f"Energy prices for the period {start} to {end}.")
print(f"Last updated: {updated}.")
print(f"Currency: {currency}.")
print()

# Loop through each area and print the prices.
for area, area_data in price["areas"].items():
    print(f"Area: {area}")
    print("-" * 40)
    for entry in area_data["values"]:
        start = entry["start"].strftime("%H:%M %Z")
        end = entry["end"].strftime("%H:%M %Z")
        value = entry["value"]
        print(f"{start} - {end}: {value:.2f} {currency}/MWh")
    print()
