import eikon as ek
import pandas as pd
import numpy as np
import datetime

ek.set_app_key('78672ced61d24c9c9c9c57798b28bdc62070476d')

def etf_prem(etf_ticker, sdate, edate):
    '''
    date format should be YYYY-MM-DD
    '''
    df, err = ek.get_data(
    instruments = [etf_ticker],
    fields = [
        'TR.NETASSETVAL.date',
        'TR.NETASSETVAL',
        'TR.PriceClose'],
    parameters = {
        'SDate': sdate,
        'EDate': edate,
        'Frq':'D'})
    
    df['Date'] = df['Date'].str[0:10]
    df['Premium'] = 100 * ((df['Price Close'] - df['Net Asset Value']) / df['Net Asset Value'])

    return df
