# pylint: disable=missing-module-docstring
from datetime import date, datetime, timedelta

from pytz import utc
import requests
from dateutil.parser import parse as parse_dt

from .base import Base, CurrencyMismatch


class Prices(Base):
    """Class for fetching Nord Pool Elspot prices."""

    HOURLY = 10
    DAILY = 11
    WEEKLY = 12
    MONTHLY = 13
    YEARLY = 14

    API_URL = "https://dataportal-api.nordpoolgroup.com/api"

    AREAS = [
        # Nordics
        "DK1",
        "DK2",
        "FI",
        "NO1",
        "NO2",
        "NO3",
        "NO4",
        "SE1",
        "SE2",
        "SE3",
        "SE4",
        # Baltic
        "EE",
        "LT",
        "LV",
        # CWE
        "AT",
        "BE",
        "FR",
        "GER",
        "NL",
        "PL",
        # Nordic system price
        "SYS",
    ]

    def _parse_json(self, data, data_type, areas):
        """
        Parse json response from fetcher.
        Returns dictionary with
            - start time
            - end time
            - update time
            - currency
            - dictionary of areas, based on selection
                - list of values (dictionary with start and endtime and value)
                - possible other values, such as min, max, average for hourly

        """

        start_time = datetime(
            2100,
            1,
            1,
            tzinfo=utc if data_type == self.HOURLY else None,
        )
        end_time = datetime(
            1970,
            1,
            1,
            tzinfo=utc if data_type == self.HOURLY else None,
        )
        updated = parse_dt(data.get("updatedAt", "1970-01-01"))
        currency = data.get("currency", self.currency)

        area_prices = {}
        data_source = ("multiAreaEntries", "entryPerArea")  # Defaults to HOURLY
        if data_type == self.DAILY:
            data_source = ("multiAreaDailyAggregates", "averagePerArea")
        if data_type == self.WEEKLY:
            data_source = ("multiAreaWeeklyAggregates", "averagePerArea")
        if data_type == self.MONTHLY:
            data_source = ("multiAreaMonthlyAggregates", "averagePerArea")
        if data_type == self.YEARLY:
            data_source = ("prices", "averagePerArea")

        for entry in data.get(data_source[0], []):
            start = parse_dt(entry["deliveryStart"])
            end = parse_dt(entry["deliveryEnd"])
            for area, price in entry.get(data_source[1], {}).items():
                if area not in areas:
                    continue
                if area not in area_prices:
                    area_prices[area] = []
                area_prices[area].append(
                    {
                        "start": start,
                        "end": end,
                        "value": price,
                    }
                )
                start_time = min(start_time, start)
                end_time = max(end_time, end)

        # Ensure that the provided currency match the requested one
        if currency != self.currency:
            raise CurrencyMismatch

        return {
            "start": start_time,
            "end": end_time,
            "updated": updated,
            "currency": currency,
            "areas": area_prices,
        }

    def _get_url_params_areas(self, data_type, end_date=None, areas=None):
        # If end_date isn't set, default to tomorrow
        if end_date is None:
            end_date = date.today() + timedelta(days=1)
        # If end_date isn't a date or datetime object, try to parse a string
        if not isinstance(end_date, date) and not isinstance(end_date, datetime):
            end_date = parse_dt(end_date)
        if areas is None:
            areas = self.AREAS

        endpoint = "DayAheadPrices"  # default to hourly
        if data_type in [self.DAILY, self.WEEKLY, self.MONTHLY]:
            endpoint = "AggregatePrices"
        if data_type == self.YEARLY:
            endpoint = "AggregatePrices/GetAnnuals"

        api_url = f"{self.API_URL}/{endpoint}"
        params = {
            "currency": "EUR",
            "market": "DayAhead",
            "deliveryArea": ",".join(areas),
        }

        if data_type == self.HOURLY:
            params["date"] = end_date.strftime("%Y-%m-%d")
        if data_type in [self.DAILY, self.WEEKLY, self.MONTHLY]:
            params["year"] = end_date.strftime("%Y")
        return api_url, params, areas

    def _fetch_json(self, data_type, end_date=None, areas=None):
        """Fetch JSON from API"""
        api_url, params, areas = self._get_url_params_areas(data_type, end_date, areas)
        response = requests.get(
            api_url,
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return self._parse_json(response.json(), data_type, areas)

    def fetch(self, data_type, end_date=None, areas=None):
        """
        Fetch data from API.
        Inputs:
            - data_type
                one of Prices.HOURLY, Prices.DAILY etc
            - end_date
                datetime to end the data fetching
                defaults to tomorrow
            - areas
                list of areas to fetch, such as ['SE1', 'SE2', 'FI']
                defaults to all areas

        Returns dictionary with
            - start time
            - end time
            - update time
            - currency
            - dictionary of areas, based on selection
                - list of values (dictionary with start and endtime and value)
                - possible other values, such as min, max, average for hourly
        """

        return self._fetch_json(data_type, end_date, areas)

    def hourly(self, end_date=None, areas=None):
        """Helper to fetch hourly data, see Prices.fetch()"""
        return self.fetch(self.HOURLY, end_date, areas)

    def daily(self, end_date=None, areas=None):
        """Helper to fetch daily data, see Prices.fetch()"""
        return self.fetch(self.DAILY, end_date, areas)

    def weekly(self, end_date=None, areas=None):
        """Helper to fetch weekly data, see Prices.fetch()"""
        return self.fetch(self.WEEKLY, end_date, areas)

    def monthly(self, end_date=None, areas=None):
        """Helper to fetch monthly data, see Prices.fetch()"""
        return self.fetch(self.MONTHLY, end_date, areas)

    def yearly(self, end_date=None, areas=None):
        """Helper to fetch yearly data, see Prices.fetch()"""
        return self.fetch(self.YEARLY, end_date, areas)


class AioPrices(Prices):
    """Class for fetching Nord Pool Elspot prices."""

    # pylint: disable=invalid-overridden-method

    def __init__(self, currency, client):

        super().__init__(currency)
        self.client = client

    async def _io(self, url, params):
        import inspect  # pylint: disable=import-outside-toplevel

        resp = await self.client.get(url, params=params)
        # aiohttp
        if inspect.isawaitable(resp.json()):
            return await resp.json()
        # Httpx and asks
        return resp.json()

    async def _fetch_json(self, data_type, end_date=None, areas=None):
        """Fetch JSON from API"""
        api_url, params, areas = self._get_url_params_areas(data_type, end_date, areas)
        return await self._io(
            api_url,
            params,
        )

    async def fetch(self, data_type, end_date=None, areas=None):
        """
        Fetch data from API.
        Inputs:
            - data_type
                API page id, one of Prices.HOURLY, Prices.DAILY etc
            - end_date
                datetime to end the data fetching
                defaults to tomorrow
            - areas
                list of areas to fetch, such as ['SE1', 'SE2', 'FI']
                defaults to all areas
        Returns dictionary with
            - start time
            - end time
            - update time
            - currency
            - dictionary of areas, based on selection
                - list of values (dictionary with start and endtime and value)
                - possible other values, such as min, max, average for hourly
        """
        data = await self._fetch_json(data_type, end_date, areas=areas)
        return self._parse_json(data, data_type, areas)

    async def hourly(self, end_date=None, areas=None):
        """Helper to fetch hourly data, see Prices.fetch()"""
        return await self.fetch(self.HOURLY, end_date, areas)

    async def daily(self, end_date=None, areas=None):
        """Helper to fetch daily data, see Prices.fetch()"""
        return await self.fetch(self.DAILY, end_date, areas)

    async def weekly(self, end_date=None, areas=None):
        """Helper to fetch weekly data, see Prices.fetch()"""
        return await self.fetch(self.WEEKLY, end_date, areas)

    async def monthly(self, end_date=None, areas=None):
        """Helper to fetch monthly data, see Prices.fetch()"""
        return await self.fetch(self.MONTHLY, end_date, areas)

    async def yearly(self, end_date=None, areas=None):
        """Helper to fetch yearly data, see Prices.fetch()"""
        return await self.fetch(self.YEARLY, end_date, areas)
