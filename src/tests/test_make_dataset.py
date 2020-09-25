"""
Introduction
--------------
This python file contains the source code used to test the data preparation
process
Code
------
"""

import pandas as pd
from src.data import make_dataset as md
import pytest

BASE_RAW_DATA_DIR = 'data/raw'
"""
str: Base raw data directory
"""
BASE_PROCESSED_DATA_DIR = 'data/processed'
"""
str: Base processed data directory
"""

df_covid19_file = 'data/raw/df_covid19.csv'
"""

"""

df_confirmed_file = BASE_RAW_DATA_DIR + '/df_confirmed.csv'
"""

"""

df_deaths_file = BASE_RAW_DATA_DIR + '/df_deaths.csv'

@pytest.fixture
def global_meta():
    """
    
    Returns
    -------
    pandas.core.frame.DataFrame
       
    """
    
    META_DF = pd.read_csv(df_covid19_file)
    return(META_DF.copy())

@pytest.fixture
def global_df_confirmed():
    """
    
    Returns
    -------
    pandas.core.frame.DataFrame
        
    """

    df_confirmed = pd.read_csv(df_confirmed_file)
    return(df_confirmed.copy())

@pytest.fixture
def global_df_deaths():
    """
    
    Returns
    -------
    pandas.core.frame.DataFrame
       
    """
    df_deaths = pd.read_csv(df_deaths_file)
    return(df_deaths.copy())
