from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from rules1 import trading_rules

def get_all_positions(trading_client):
    all_positions_list = trading_client.get_all_positions()
    all_positions_dict = {}

    for position in all_positions_list:
        all_positions_dict[position.symbol] = position
    return all_positions_dict


def buy_strat1(trading_client, data_struct):
    account = trading_client.get_account()
    position_allocation = round(float(account.portfolio_value)*trading_rules["max position allocation"],2)

    all_positions_dict = get_all_positions(trading_client)

    if data_struct['symbol'] in all_positions_dict:
        market_value = float(all_positions_dict[data_struct['symbol']].market_value)

        if market_value > position_allocation:
            return None
        elif (position_allocation - market_value) >= trading_rules["min buy difference"]:
            market_order_data = MarketOrderRequest(
                symbol=data_struct['symbol'],
                notional=round(position_allocation-market_value,2),
                side=OrderSide.BUY,
                time_in_force=TimeInForce.GTC
            )
            market_order = trading_client.submit_order(
                order_data=market_order_data
            )
    else:
        market_order_data = MarketOrderRequest(
            symbol=data_struct['symbol'],
            notional=round(position_allocation,2),
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC
        )

        market_order = trading_client.submit_order(
            order_data=market_order_data
        )
    return None

def sell_strat1(trading_client):
    account = trading_client.get_account()
    position_allocation = round(float(account.portfolio_value)*trading_rules["max position allocation"],2)
    all_positions = trading_client.get_all_positions()

    for position in all_positions:
        PnL = round(float(position.unrealized_plpc),2)
        market_value = round(float(position.market_value))

        if PnL >= trading_rules["minimum gain"] or PnL <= trading_rules['maximum loss']:
            market_order_data = MarketOrderRequest(
                symbol=position.symbol,
                qty=position.qty,
                side=OrderSide.SELL,
                time_in_force=TimeInForce.GTC
            )
            # Market order
            market_order = trading_client.submit_order(
                order_data=market_order_data
            )
        #if market value becomes over 200 greater than position allocatio, sell the difference to stay within bounds
        # over 200 more than our position allocation
        if (market_value - position_allocation) >= trading_rules["min sell difference"]:
            market_order_data = MarketOrderRequest(
                symbol=position.symbol,
                notional=round(market_value-position_allocation,2),
                side=OrderSide.SELL,
                time_in_force=TimeInForce.GTC
            )
            # Market order
            market_order = trading_client.submit_order(
                order_data=market_order_data
            )
    return None