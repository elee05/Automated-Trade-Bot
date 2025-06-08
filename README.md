# Trading Bot
This is a simple bot which buys an sells equities(crypto bc the market is alway open) based on rules to maintain certain portfolio allocations.
No real strategy just proof of concept.  
- rules.py holds list of rules  
- strat1.py implements as buy and sell orders  
- ignore main.py

## API
uses alpaca-py to stream real time price quotes, displays market activites and decides whether or not to take action
