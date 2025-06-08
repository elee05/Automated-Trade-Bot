from dotenv import load_dotenv
import os
import asyncio
import datetime
import time
from matplotlib import pyplot as plt
from strat1 import buy_strat1,sell_strat1

load_dotenv()

from alpaca.data.live import CryptoDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


trade_count = 0
max_trades = 40

api_key = os.getenv('ALPACAKEY')
secret_key = os.getenv('SECRETKEY')

trading_client = TradingClient(api_key, secret_key, paper=True)

def makeHandler(store,wss_client):
    async def quote_data_handler(data):
        data_struct = {
            'symbol': data.symbol,
            'bid price': data.bid_price,
            'bid size': data.bid_size,
            'ask price': data.ask_price,
            'ask size': data.ask_size
        }

        # print(f"Received data: {data.timestamp.astimezone()}, {data.bid_price}, {data.symbol}")
        print(data_struct)
        store[data.symbol].append(data.bid_price)
        global trade_count
        trade_count += 1
        # if trade_count >= max_trades:
        #     print("Max trades received. Stopping stream...")
        #     await wss_client.stop()
        trade_result = buy_strat1(trading_client,data_struct)
        trade_result2 = sell_strat1(trading_client)
        if trade_result:
            print(f"buy result: {trade_result}")
        if trade_result2:
            print(f"sell result: {trade_result2}")
    return quote_data_handler



def main():
    # Get API keys with verification
    api_key = os.getenv('ALPACAKEY')
    secret_key = os.getenv('SECRETKEY')
    
    symbols = ["BTC/USD","ETH/USD","USDT/USD","BNB/USD","SOL/USD","XRP/USD","DOGE/USD","TRX/USD","ADA/USD"]
    changes = {symbol: [] for symbol in symbols}

    print("Attempting to connect with API key:", api_key[:4] + "..." + api_key[-4:])  # Partial print for security
    try:
        wss_client = CryptoDataStream(api_key, secret_key)
        handler = makeHandler(changes,wss_client)
        wss_client.subscribe_quotes(handler, *symbols)
        print("Starting WebSocket connection...")
        wss_client.run()
        print(f"changes: {changes}")
        print(min(list(changes.values())))
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Please verify:")
        print("1. Your API keys are correct")
        print("2. Your account has crypto permissions")
        print("3. You're using the correct environment (paper/live)")

if __name__ == "__main__":
    main()



