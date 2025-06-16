from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from dotenv import load_dotenv
import os
import asyncio
import pandas as pd



load_dotenv()

api_key = os.getenv('ALPACAKEY')
secret_key = os.getenv('SECRETKEY')

# no keys required for crypto data
client = StockHistoricalDataClient(api_key,secret_key)

request_params = StockBarsRequest(
                        symbol_or_symbols=["AAPL", "MSFT"],
                        timeframe=TimeFrame.Day,
                        start=datetime(2022, 7, 1),
                        end=datetime(2022, 9, 1)
                 )

bars = client.get_stock_bars(request_params)

# convert to dataframe
bars.df

# access bars as list - important to note that you must access by symbol key
# even for a single symbol request - models are agnostic to number of symbols
print(bars)