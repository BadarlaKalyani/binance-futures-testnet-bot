import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_symbol, validate_side, validate_order_type


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT orders)"
    )

    args = parser.parse_args()

    try:
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)

        if args.type == "LIMIT" and args.price is None:
            raise ValueError("LIMIT order requires --price")

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.price is not None:
            print(f"Price    : {args.price}")

        print("===================================\n")

        # Place Order
        if args.type == "MARKET":
            result = place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )
        else:
            result = place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        print("\n========== ORDER RESPONSE ==========")

        if result.get("success"):
            print(result)
            print("\n✅ Order placed successfully!")
        else:
            print(result)
            print("\n❌ Order failed!")

    except Exception as e:
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()