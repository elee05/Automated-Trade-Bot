from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

from alpaca.data.live import CryptoDataStream

async def quote_data_handler(data):
    print("Received data:", data)

def main():
    # Get API keys with verification
    api_key = os.getenv('ALPACAKEY')
    secret_key = os.getenv('SECRETKEY')
    
    print("Attempting to connect with API key:", api_key[:4] + "..." + api_key[-4:])  # Partial print for security
    
    try:
        wss_client = CryptoDataStream(api_key, secret_key)
        wss_client.subscribe_quotes(quote_data_handler, "BTC/USD")
        
        print("Starting WebSocket connection...")
        wss_client.run()
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Please verify:")
        print("1. Your API keys are correct")
        print("2. Your account has crypto permissions")
        print("3. You're using the correct environment (paper/live)")

if __name__ == "__main__":
    main()