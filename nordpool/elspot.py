# pylint: disable=missing-module-docstring
from datetime import date, datetime, timedelta

from pytz import utc
import requests
from dateutil.parser import parse as parse_dt


class UnsupportedResolution(ValueError):
    """
    Raised when the requested resolution is not supported.
    Supported resolutions are 15, 30 and 60 minutes.
    """


class CurrencyMismatch(ValueError):
    """
    Raised when the currency of the data does not match the currency of the request.
    """


class Prices:
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
        "NO5",
        "SE1",
        "SE2",
        "SE3",
        "SE4",
        # Baltic
        "EE",
        "LT",
        "LV",
        # Central Western Europe
        "AT",
        "BE",
        "FR",
        "GER",
        "NL",
        "PL",
        # South East Europe
        "BG",
        "TEL",
        # Nordic system price
        # NOTE: Some API endpoints use "SYSTEM" for "SYS",
        # this is handled internally and area "SYS" should be used by external code
        "SYS",
    ]

    SUPPORTED_RESOLUTIONS = [15, 30, 60]

    def __init__(self, currency="EUR", timeout=None):
        self.currency = currency
        self.timeout = timeout or 2

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
        data_source = ("multiIndexEntries", "entryPerArea")  # Defaults to HOURLY
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
                # Price indices -endpoint uses "SYSTEM" for "SYS"
                # -> replace it when responding
                if area == "SYSTEM":
                    area = "SYS"
                if area not in areas:
                    continue  # pragma: no cover
                if area not in area_prices:
                    area_prices[area] = {"values": []}
                area_prices[area]["values"].append(
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
            raise CurrencyMismatch  # pragma: no cover

        if not area_prices:
            # No data found, behavior changed when moving to using price indices
            return None

        return {
            "start": start_time,
            "end": end_time,
            "updated": updated,
            "currency": currency,
            "areas": area_prices,
        }

    def _get_url_params_areas(
        self,
        data_type,
        end_date=None,
        areas=None,
        resolution=60,
    ):
        # If end_date isn't set, default to tomorrow
        if end_date is None:
            end_date = date.today() + timedelta(days=1)  # pragma: no cover
        # If end_date isn't a date or datetime object, try to parse a string
        if not isinstance(end_date, date) and not isinstance(end_date, datetime):
            end_date = parse_dt(end_date)
        if areas is None:
            areas = self.AREAS  # pragma: no cover
        if resolution not in self.SUPPORTED_RESOLUTIONS:
            raise UnsupportedResolution(
                f"Resolution {resolution} is not supported, "
                f"must be one of {self.SUPPORTED_RESOLUTIONS}"
            )

        endpoint = "DayAheadPriceIndices"  # default to hourly
        if data_type in [self.DAILY, self.WEEKLY, self.MONTHLY]:
            endpoint = "AggregatePrices"
        if data_type == self.YEARLY:
            endpoint = "AggregatePrices/GetAnnuals"

        api_url = f"{self.API_URL}/{endpoint}"
        params = {
            "currency": self.currency,
            "market": "DayAhead",
        }

        if data_type == self.HOURLY:
            params["date"] = end_date.strftime("%Y-%m-%d")
            params["resolutionInMinutes"] = resolution
            params["indexNames"] = ",".join(
                # Price indices -endpoint uses "SYSTEM" for "SYS"
                # -> replace it when requesting
                "SYSTEM" if area == "SYS" else area
                for area in areas
            )
        else:
            params["deliveryArea"] = ",".join(areas)
        if data_type in [self.DAILY, self.WEEKLY, self.MONTHLY]:
            params["year"] = end_date.strftime("%Y")
        return api_url, params, areas

    def _fetch_json(self, data_type, end_date=None, areas=None, resolution=60):
        """Fetch JSON from API"""
        api_url, params, areas = self._get_url_params_areas(
            data_type, end_date, areas, resolution
        )
        response = requests.get(
            api_url,
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        if response.status_code == 204:
            # "Old" API returns 204 for no data
            return None  # pragma: no cover
        return self._parse_json(response.json(), data_type, areas)

    def fetch(self, data_type=None, end_date=None, areas=None, resolution=60):
        """
        Fetch data from API.
        Inputs:
            - data_type
                one of Prices.HOURLY, Prices.DAILY etc
                defaults to Prices.HOURLY (used for hourly and sub-hourly data)
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

        if data_type is None:
            data_type = self.HOURLY

        return self._fetch_json(data_type, end_date, areas, resolution)

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


class AioPrices(Prices):  # pragma: no cover
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

    async def _fetch_json(self, data_type, end_date=None, areas=None, resolution=60):
        """Fetch JSON from API"""
        api_url, params, areas = self._get_url_params_areas(
            data_type, end_date, areas, resolution
        )
        return await self._io(
            api_url,
            params,
        )

    async def fetch(self, data_type=None, end_date=None, areas=None, resolution=60):
        """
        Fetch data from API.
        Inputs:
            - data_type
                API page id, one of Prices.HOURLY, Prices.DAILY etc
                defaults to Prices.HOURLY, used for hourly and sub-hourly data
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
        if areas is None:  # If no areas are provided, inherit from the parent class
            areas = self.AREAS
        if data_type is None:
            data_type = self.HOURLY

        data = await self._fetch_json(
            data_type,
            end_date,
            areas=areas,
            resolution=resolution,
        )
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
