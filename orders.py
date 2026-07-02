from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"MARKET Order Request: {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Response: {order}")

        return {
            "success": True,
            "data": order
        }

    except Exception as e:
        logger.error(str(e))
        return {
            "success": False,
            "error": str(e)
        }


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"LIMIT Order Request: {side} {quantity} {symbol} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

        logger.info(f"Response: {order}")

        return {
            "success": True,
            "data": order
        }

    except Exception as e:
        logger.error(str(e))
        return {
            "success": False,
            "error": str(e)
        }