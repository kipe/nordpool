# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from datetime import date, datetime, timedelta
from dateutil.parser import parse as parse_dt
from .base import Base, CurrencyMismatch


class Prices(Base):
    ''' Class for fetching Nord Pool Elspot prices. '''
    HOURLY = 10
    DAILY = 11
    WEEKLY = 12
    MONTHLY = 13
    YEARLY = 14

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

        area_data = {}
        # Loop through response rows
        for r in data['Rows']:
            row_start_time = self._parse_dt(r['StartTime'])
            row_end_time = self._parse_dt(r['EndTime'])

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
                if r['IsExtraRow']:
                    # Update extra data to dictionary
                    area_data[name][r['Name']] = self._conv_to_float(c['Value'])
                else:
                    # Append dictionary to value list
                    area_data[name]['values'].append({
                        'start': row_start_time,
                        'end': row_end_time,
                        'value': self._conv_to_float(c['Value']),
                    })

        return {
            'start': start_time,
            'end': end_time,
            'updated': updated,
            'currency': currency,
            'areas': area_data
        }

    def _fetch_json(self, data_type, end_date=None):
        ''' Fetch JSON from API '''
        # If end_date isn't set, default to tomorrow
        if end_date is None:
            end_date = date.today() + timedelta(days=1)
        # If end_date isn't a date or datetime object, try to parse a string
        if not isinstance(end_date, date) and not isinstance(end_date, datetime):
            end_date = parse_dt(end_date)

        # Create request to API
        r = requests.get(self.API_URL % data_type, params={
            'currency': self.currency,
            'endDate': end_date.strftime('%d-%m-%Y'),
        }, timeout=self.timeout)
        # Return JSON response
        return r.json()

    def fetch(self, data_type, end_date=None, areas=[]):
        '''
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
        '''
        return self._parse_json(self._fetch_json(data_type, end_date), areas)

    def hourly(self, end_date=None, areas=[]):
        ''' Helper to fetch hourly data, see Prices.fetch() '''
        return self.fetch(self.HOURLY, end_date, areas)

    def daily(self, end_date=None, areas=[]):
        ''' Helper to fetch daily data, see Prices.fetch() '''
        return self.fetch(self.DAILY, end_date, areas)

    def weekly(self, end_date=None, areas=[]):
        ''' Helper to fetch weekly data, see Prices.fetch() '''
        return self.fetch(self.WEEKLY, end_date, areas)

    def monthly(self, end_date=None, areas=[]):
        ''' Helper to fetch monthly data, see Prices.fetch() '''
        return self.fetch(self.MONTHLY, end_date, areas)

    def yearly(self, end_date=None, areas=[]):
        ''' Helper to fetch yearly data, see Prices.fetch() '''
        return self.fetch(self.YEARLY, end_date, areas)


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
