# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:57:40 2020

@author: Nikhil Bhargava
TimeZones uiong Python
"""

from datetime import datetime as dt
import pytz

timezones=pytz.all_timezones

for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("Current Time at zone",zone, "is", dt .now())

