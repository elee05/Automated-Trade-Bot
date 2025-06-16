from dotenv import load_dotenv
import os

load_dotenv()
from alpaca.data.live import CryptoDataStream, OptionDataStream, StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest



# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

api_key = os.getenv('ALPACAKEY')
secret_key = os.getenv('SECRETKEY')

def main():
    wss_client = CryptoDataStream(api_key, secret_key)
    wss_client.subscribe_quotes(quote_data_handler, 'BTC/USD')

    wss_client.run()


if __name__ == '__main__':
    main()



# trading_client = TradingClient(api_key, secret_key)

# # Get our account information.
# account = trading_client.get_account()
# balance_change = float(account.equity) 
# print(f'Today\'s portfolio balance: ${balance_change}')