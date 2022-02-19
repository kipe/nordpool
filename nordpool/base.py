# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from dateutil.parser import parse as parse_dt
from pytz import timezone, utc


class CurrencyMismatch(ValueError):
    pass


class Base(object):
    ''' Class for fetching Nord Pool Elspot prices. '''
    def __init__(self, currency='EUR', timeout=None):
        self.currency = currency
        self.timeout = timeout

    def _parse_dt(self, time_str):
        ''' Parse datetimes to UTC from Stockholm time, which Nord Pool uses. '''
        time = parse_dt(time_str)
        if time.tzinfo is None:
            return timezone('Europe/Stockholm').localize(time).astimezone(utc)
        return time

    def _conv_to_float(self, s):
        ''' Convert numbers to float. Return infinity, if conversion fails. '''
        try:
            return float(s.replace(',', '.').replace(" ", ""))
        except ValueError:
            return float('inf')
