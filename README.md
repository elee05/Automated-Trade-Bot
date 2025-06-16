# Trading Bot
This is a simple bot which buys an sells equities(crypto bc the market is alway open) based on rules to maintain certain portfolio allocations.
No real strategy just proof of concept.  
- rules.py holds list of rules  
- strat1.py implements as buy and sell orders  
- ignore main.py

## ema_test.ipynb and folders
- notebook for backtesting a common strategy, Exponetial Moving Averages. By comparing when the price averaged over 20 days rises over the price averaged over 50 days, a bullish trend can be predicted.
- this script backtests a simple strategy of buying when the 20 ema crosses over the 50 ema and selling in the reverse. Folders for different types of equities show the paths and the results folder holds json files which show the average returns per indvidual trade(buy and sell instance) over multiple equities.

## API
uses alpaca-py to stream real time price quotes, displays market activites and decides whether or not to take action
