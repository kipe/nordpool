# -*- encoding: utf-8 -*-

import requests
from datetime import date, datetime, timedelta
from dateutil.parser import parse as parse_dt
from pytz import timezone, utc


class Prices(object):
    HOURLY = 10
    DAILY = 11
    WEEKLY = 12
    MONTHLY = 13
    YEARLY = 14

    API_URL = 'http://www.nordpoolspot.com/api/marketdata/page/%i'

    def __init__(self, currency='EUR'):
        self.currency = currency

    def __parse_dt(self, time_str, summer_time=False):
        time = parse_dt(time_str)
        return timezone('Europe/Stockholm').localize(time).astimezone(utc)

    def __conv_to_float(self, s):
        try:
            return float(s.replace(',', '.'))
        except ValueError:
            return float('inf')

    def _parse_json(self, data, areas=[]):
        if not isinstance(areas, list):
            areas = list(areas)

        currency = data['currency']
        data = data['data']
        start_time = self.__parse_dt(data['DataStartdate'], data['IsDSTDay'])
        end_time = self.__parse_dt(data['DataEnddate'], data['IsDSTDay'])
        updated = self.__parse_dt(data['DateUpdated'], data['IsDSTDay'])

        area_data = {}
        for r in data['Rows']:
            row_start_time = self.__parse_dt(r['StartTime'])
            row_end_time = self.__parse_dt(r['EndTime'])

            for c in r['Columns']:
                name = c['Name']
                if areas and name not in areas:
                    continue

                if name not in area_data:
                    area_data[name] = {
                        'values': [],
                    }

                if not r['IsExtraRow']:
                    area_data[name]['values'].append({
                        'start': row_start_time,
                        'end': row_end_time,
                        'value': self.__conv_to_float(c['Value']),
                    })
                else:
                    area_data[name][r['Name']] = self.__conv_to_float(c['Value'])

        return {
            'start': start_time,
            'end': end_time,
            'updated': updated,
            'currency': currency,
            'areas': area_data
        }

    def _fetch_json(self, page_code, end_date=None):
        if end_date is None:
            end_date = date.today() + timedelta(days=1)
        if not isinstance(end_date, datetime) and not isinstance(end_date, date):
            end_date = parse_dt(end_date)

        r = requests.get(self.API_URL % page_code, params={
            'currency': self.currency,
            'endDate': end_date.strftime('%d-%m-%Y'),
        })
        return r.json()

    def fetch(self, data_type, end_date=None, areas=[]):
        return self._parse_json(self._fetch_json(data_type, end_date), areas)

    def hourly(self, end_date=None, areas=[]):
        return self.fetch(self.HOURLY, end_date, areas)

    def daily(self, end_date=None, areas=[]):
        return self.fetch(self.DAILY, end_date, areas)

    def weekly(self, end_date=None, areas=[]):
        return self.fetch(self.WEEKLY, end_date, areas)

    def monthly(self, end_date=None, areas=[]):
        return self.fetch(self.MONTHLY, end_date, areas)

    def yearly(self, end_date=None, areas=[]):
        return self.fetch(self.YEARLY, end_date, areas)
