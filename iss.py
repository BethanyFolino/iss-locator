#!/usr/bin/env python

__author__ = '''Bethany Folino and
              https://www.dataquest.io/blog/python-api-tutorial/,
              https://realpython.com/python-time-module/'''

import requests
from time import ctime
import json


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = json.dumps(r.json(), sort_keys=True, indent=4)
    print(astros)


def station_location():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    station = json.dumps(r.json(), sort_keys=True, indent=4)
    print(station)


def over_indy():
    params = {
        "lat": 39.791000,
        "lon": -86.148003
    }
    r = requests.get('http://api.open-notify.org/iss-pass.json', params)
    pass_times = r.json()['response']

    risetimes = []
    for d in pass_times:
        if len(risetimes) < 1:
            risetime = d['risetime']
            hr_time = ctime(risetime)
            risetimes.append(hr_time)
    print(risetimes)


if __name__ == '__main__':
    astronauts()
    station_location()
    over_indy()
