#!/usr/bin/env python

__author__ = 'Bethany Folino'

import requests


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    print(r.json())


def station_location():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    print(r.text)


def over_indy():
    r = requests.get('http://api.open-notify.org/iss-pass.json')
    print(r.text)


if __name__ == '__main__':
    astronauts()
    station_location()
    over_indy()
