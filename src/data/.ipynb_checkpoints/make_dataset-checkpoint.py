# -*- coding: utf-8 -*-
# libraries
import click
import logging
from pathlib import Path
import pandas as pd

# importing dataset from github
df_confirmed = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/df_confirmed.csv')

df_deaths = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/df_deaths.csv')

df_covid19 = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/df_covid19.csv')

df_table = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/df_table.csv')

covid19 = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/covid_19_data.csv')

mitigation = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/mitigation.csv')

population = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/mitigation.csv')

weather = pd.read_csv('https://github.com/tahossain42/covid-19-data/blob/master/world_weather.csv')

# saving dataset as csv format in /data/raw directory 
df_confirmed.to_csv('../../data/raw/df_confirmed.csv' , index = False)
df_deaths.to_csv('../../data/raw/df_deaths.csv' , index = False)
df_covid19.to_csv('../../data/raw/df_covid19.csv', index = False)
df_table.to_csv('../../data/raw/df_table.csv', index = False)
covid19.to_csv('../../data/raw/covid_19_data.csv', index = False)
mitigation.to_csv('../../data/raw/mitigation.csv', index = False)
population.to_csv('../../data/raw/population.csv', index = False)
weather.to_csv('../../data/raw/world_weather.csv', index = False)
