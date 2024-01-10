# Market Data Analysis functionality
# author: Matheus Pedro

from alpha_vantage.timeseries import TimeSeries
import time
import main

api_key = '7P0IOH3LDW52HMLH'

def realTimeAnalyis():
    symbol = input("Enter the code of the stock you want to analyze: ")
    main.clearPrompt()
    print("Wait a few seconds before making the next request")

    # TimeSeries class instance with API key
    ts = TimeSeries(key=api_key, output_format='pandas')

    while True:
        try:
            # Get real-time data for action
            data, meta_data = ts.get_quote_endpoint(symbol=symbol)

            # Display price and price change
            price = data['05. price'].iloc[0]
            change = data['09. change'].iloc[0]

            print(f'Symbol: {symbol}, Price: {price}, Change Percentual: {change}')
        except Exception as e:
            print(f"Error getting real-time data: {e}")
        
        # Wait a few seconds before making the next request
        time.sleep(5)