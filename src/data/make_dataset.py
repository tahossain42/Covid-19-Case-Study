# -*- coding: utf-8 -*-
# libraries
import click
import logging
from pathlib import Path
import pandas as pd

# importing dataset from github
df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

df_covid19 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")

df_table = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_time.csv",parse_dates=['Last_Update'])

# saving dataset as csv format in /data/raw directory 
df_confirmed.to_csv('../../data/raw/df_confirmed.csv' , index = False)
df_deaths.to_csv('../../data/raw/df_deaths.csv' , index = False)
df_covid19.to_csv('../../data/raw/df_covid19.csv', index = False)
df_table.to_csv('../../data/raw/df_table.csv', index = False)
