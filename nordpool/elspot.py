# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from datetime import date, datetime, timedelta
from dateutil.parser import parse as parse_dt
from .base import Base, CurrencyMismatch
from math import isinf


class Prices(Base):
    ''' Class for fetching Nord Pool Elspot prices. '''
    page_id = {
                "ALL": {
                    "HOURLY": 10,
                    "DAILY": 11,
                    "WEEKLY": 12,
                    "MONTHLY": 13,
                    "YEARLY": 14,
                    "TENDAYS": 15
                },
                "SYS": {
                    "HOURLY": 17,
                    "DAILY": 18,
                    "WEEKLY": 19,
                    "MONTHLY": 20,
                    "YEARLY": 21
                },
                "NO": {
                    "HOURLY": 23,
                    "DAILY": 24,
                    "WEEKLY": 25,
                    "MONTHLY": 26,
                    "YEARLY": 27
                },
                "SE": {
                    "HOURLY": 29,
                    "DAILY": 30,
                    "WEEKLY": 31,
                    "MONTHLY": 32,
                    "YEARLY": 33
                },
                "FI": {
                    "HOURLY": 35,
                    "DAILY": 36,
                    "WEEKLY": 37,
                    "MONTHLY": 38,
                    "YEARLY": 39
                },
                "DK": {
                    "HOURLY": 41,
                    "DAILY": 42,
                    "WEEKLY": 43,
                    "MONTHLY": 44,
                    "YEARLY": 45
                },
                "EE": {
                    "HOURLY": 47,
                    "DAILY": 48,
                    "WEEKLY": 49,
                    "MONTHLY": 50,
                    "YEARLY": 51
                },
                "LT": {
                    "HOURLY": 53,
                    "DAILY": 54,
                    "WEEKLY": 55,
                    "MONTHLY": 56,
                    "YEARLY": 57
                },
                "LV": {
                    "HOURLY": 59,
                    "DAILY": 60,
                    "WEEKLY": 61,
                    "MONTHLY": 62,
                    "YEARLY": 63
                }
            }

    API_URL = 'https://www.nordpoolgroup.com/api/marketdata/page/%i'

    def _parse_json(self, data, areas=[]):
        '''
        Parse json response from fetcher.
        Returns dictionary with
            - start time
            - end time
            - update time
            - currency
            - dictionary of areas, based on selection
                - list of values (dictionary with start and endtime and value)
                - possible other values, such as min, max, average for hourly
        '''

        # If areas isn't a list, make it one
        if not isinstance(areas, list):
            areas = list(areas)

        # Update currency from data
        currency = data['currency']

        # Ensure that the provided currency match the requested one
        if currency != self.currency:
            raise CurrencyMismatch

        # All relevant data is in data['data']
        data = data['data']
        start_time = self._parse_dt(data['DataStartdate'])
        end_time = self._parse_dt(data['DataEnddate'])
        updated = self._parse_dt(data['DateUpdated'])
        units = data['Units']

        area_data = {}
        daylight_saving_adjust = False
        # Loop through response rows
        for r in data['Rows']:
            row_start_time = self._parse_dt(r['StartTime'])
            row_end_time = self._parse_dt(r['EndTime'])
            if daylight_saving_adjust:
                # After daylight saving is detected then adjust the following hour
                # and then reset the daylight saving flag
                row_start_time -= timedelta(hours=1)
                row_end_time -= timedelta(hours=1)
                daylight_saving_adjust = False
            else:
                # When daylight saving occur there will be a 2 hour difference between
                # start and end times
                daylight_saving_adjust = timedelta(hours=1.5) < row_end_time - row_start_time
                if daylight_saving_adjust:
                    row_end_time -= timedelta(hours=1)

            # Loop through columns
            for c in r['Columns']:
                name = c['Name']
                # If areas is defined and name isn't in areas, skip column
                if areas and name not in areas:
                    continue

                # If name isn't in area_data, initialize dictionary
                if name not in area_data:
                    area_data[name] = {
                        'values': [],
                    }

                # Time based and average, max, min etc rows are separated
                # with 'IsExtraRow' -marking
                value = self._conv_to_float(c['Value'])
                if not isinf(value):
                    if r['IsExtraRow']:
                        # Update extra data to dictionary
                        area_data[name][r['Name']] = value
                    else:
                        # Append dictionary to value list
                        area_data[name]['values'].append({
                            'start': row_start_time,
                            'end': row_end_time,
                            'value': value,
                        })

        return {
            'start': start_time,
            'end': end_time,
            'updated': updated,
            'currency': currency,
            'areas': area_data,
            'units': units
        }

    def _fetch_json(self, country, type, end_date=None):
        ''' Fetch JSON from API '''
        params = {'currency': self.currency}
        # If end_date isn't a date or datetime object, try to parse a string
        if end_date is not None:
            if not isinstance(end_date, date) and not isinstance(end_date, datetime):
                end_date = parse_dt(end_date)
            params['endDate'] = end_date.strftime('%d-%m-%Y')

        # Create request to API
        r = requests.get(self.API_URL % self.page_id[country][type], 
                         params=params, timeout=self.timeout)
        # Return JSON response
        return r.json()

    def fetch(self, country='ALL', type='HOURLY', end_date=None, areas=[]):
        '''
        Fetch data from API.
        Inputs:
            - country
                Country for area code(s), use 'ALL' if area codes of 
                multiple countries are requested or else use either
                SYS, NO, SE, FI, DK, EE, LT or LV
            - type
                API page id 'HOURLY', 'DAILY' etc
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
        '''
        country = country.upper()
        type = type.upper()
        return self._parse_json(self._fetch_json(country, type, end_date), areas)

    def hourly(self, end_date=None, areas=[]):
        ''' Helper to fetch hourly data, see Prices.fetch() '''
        return self.fetch(end_date=end_date, areas=areas)

    def daily(self, end_date=None, areas=[]):
        ''' Helper to fetch daily data, see Prices.fetch() '''
        return self.fetch(type='DAILY', end_date=end_date, areas=areas)

    def weekly(self, end_date=None, areas=[]):
        ''' Helper to fetch weekly data, see Prices.fetch() '''
        return self.fetch(type='WEEKLY', end_date=end_date, areas=areas)

    def monthly(self, end_date=None, areas=[]):
        ''' Helper to fetch monthly data, see Prices.fetch() '''
        return self.fetch(type='MONTHLY', end_date=end_date, areas=areas)

    def yearly(self, end_date=None, areas=[]):
        ''' Helper to fetch yearly data, see Prices.fetch() '''
        return self.fetch(type='YEARLY', end_date=end_date, areas=areas)


class AioPrices(Prices):
    def __init__(self, currency, client):

        super().__init__(currency)
        self.client = client

    async def _io(self, url, **kwargs):
        import inspect
        resp = await self.client.get(url, params=kwargs)
        # aiohttp
        if inspect.isawaitable(resp.json()):
            return await resp.json()
        else:
            # Httpx and asks
            return resp.json()

    async def _fetch_json(self, data_type, end_date=None):
        """ Fetch JSON from API """
        # If end_date isn't set, default to tomorrow
        if end_date is None:
            end_date = date.today() + timedelta(days=1)
        # If end_date isn't a date or datetime object, try to parse a string
        if not isinstance(end_date, date) and not isinstance(end_date, datetime):
            end_date = parse_dt(end_date)

        return await self._io(
            self.API_URL % data_type,
            currency=self.currency,
            endDate=end_date.strftime("%d-%m-%Y"),
        )

    async def fetch(self, data_type, end_date=None, areas=[]):
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
        data = await self._fetch_json(data_type, end_date)
        return self._parse_json(data, areas)

    async def hourly(self, end_date=None, areas=[]):
        """ Helper to fetch hourly data, see Prices.fetch() """
        return await self.fetch(self.HOURLY, end_date, areas)

    async def daily(self, end_date=None, areas=[]):
        """ Helper to fetch daily data, see Prices.fetch() """
        return await self.fetch(self.DAILY, end_date, areas)

    async def weekly(self, end_date=None, areas=[]):
        """ Helper to fetch weekly data, see Prices.fetch() """
        return await self.fetch(self.WEEKLY, end_date, areas)

    async def monthly(self, end_date=None, areas=[]):
        """ Helper to fetch monthly data, see Prices.fetch() """
        return await self.fetch(self.MONTHLY, end_date, areas)

    async def yearly(self, end_date=None, areas=[]):
        """ Helper to fetch yearly data, see Prices.fetch() """
        return await self.fetch(self.YEARLY, end_date, areas)
