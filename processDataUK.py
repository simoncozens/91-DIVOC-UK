# coding=utf-8

import os
from urllib.request import urlopen
import pandas as pd
from datetime import datetime
now = datetime.now()

cases_url = "https://c19downloads.azureedge.net/downloads/csv/coronavirus-cases_latest.csv"
deaths_url = "https://c19downloads.azureedge.net/downloads/csv/coronavirus-deaths_latest.csv"

with urlopen(cases_url) as c:
  df1 = pd.read_csv(c)

df1 = df1.drop(columns=["Previously reported daily cases",
  'Change in daily cases',
     'Previously reported cumulative cases', 'Change in cumulative cases',
     'Cumulative lab-confirmed cases rate'])
df1 = df1.rename(columns={'Specimen date':"Date",
  'Cumulative lab-confirmed cases':"Confirmed",
  'Area name': "Province_State"})

# Reverse it for date order
df1 = df1[::-1]
df1.to_csv('uk-data.csv', index=False)

human_dt_str = now.strftime("%m/%d") + " at " + now.strftime("%I") + ":" + now.strftime("%M%p")
human_dt_str = human_dt_str.lower()
date_str = now.strftime("%m/%d/%Y")
req_str = now.strftime("%Y%m%d")

# Write js
js = f'_dateUpdated = "{date_str}";\n' +\
     f'_reqStr = "{req_str}";\n' +\
     f'\n' +\
     f'$("#uk-updated").html("(Updated: {human_dt_str})");\n'

with open("uk-updated.js", "w") as out:
  out.write(js)
