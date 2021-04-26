import datetime
import platform

import pandas as pd
import json
from urllib.request import urlopen


def usa_counties():
    """[summary]: Returns live cases of USA at county-level
    
    source:
        ³ nytimes
    Returns:
        [pd.DataFrame]
    """
    populations = pd.read_csv('https://raw.githubusercontent.com/balsama/us_counties_data/master/data/counties.csv')[['FIPS Code', 'Population']]
    populations.rename(columns={'FIPS Code': 'fips'}, inplace=True)
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv', dtype={"fips": str}).iloc[:,:6]
    df = pd.merge(df, populations, on='fips')
    df['cases/capita'] = (df.cases / df.Population)*100000 # per 100k residents

    return df
usa_counties()