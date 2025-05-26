from dotenv import load_dotenv
import os

load_dotenv()
from alpaca.data.live import CryptoDataStream, OptionDataStream, StockDataStream



# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)



def main():
    wss_client = CryptoDataStream('ALPACAKEY', 'SECRETKEY')
    wss_client.subscribe_quotes(quote_data_handler, 'BTC/USD')

    wss_client.run()


if __name__ == '__main__':
    main()