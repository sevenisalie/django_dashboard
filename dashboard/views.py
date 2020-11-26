from django.shortcuts import render

#for financial data api
import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import datetime

# Create your views here.

def homeView(request):
    api_key = 'YX9741BHQFXIYA0B'

    stock = 'NIO'

    api_key = 'YX9741BHQFXIYA0B'
    period= 60

    ts = TimeSeries(key=api_key, output_format='pandas',)
    data_ts, meta_data_ts = ts.get_intraday(stock, interval='1min', outputsize='compact')

    ti = TechIndicators(key=api_key, output_format='pandas')
    data_ti, meta_data_ti  = ti.get_rsi(stock, interval='1min', time_period=period, series_type='close')

    ts_df = data_ts
    ti_df = data_ti

    timeseries = ts_df.to_json(index=True, orient='records')    

    day = datetime.datetime.now()
    day = day.strftime("%A")
    

    context = {
        'timeseries': timeseries,
        'stock': stock,
        'day': day, 
    }
    return render(request, 'dashboard/index.html', context)