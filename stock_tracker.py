# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}

def show_available_stocks():
    print("\nAvailable stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

def track_portfolio():
    portfolio = {}
    total_investment = 0

    show_available_stocks()
    print("\nEnter stock name and quantity. Type 'done' as stock name to finish.\n")

    while True:
        stock = input("Stock name: ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found in our list. Try again.")
            continue

        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        cost = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += cost
        print(f"Added {quantity} shares of {stock} (${cost})")

    print("\n--- Portfolio Summary ---")
    if not portfolio:
        print("No stocks added.")
        return

    for stock, quantity in portfolio.items():
        print(f"{stock}: {quantity} shares, Value: ${stock_prices[stock] * quantity}")

    print(f"\nTotal Investment: ${total_investment}")

    save = input("\nSave this summary to a file? (y/n): ").lower()
    if save == "y":
        save_to_file(portfolio, total_investment)

def save_to_file(portfolio, total_investment):
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("------------------------\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            f.write(f"{stock}: {quantity} shares, Value: ${value}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("Summary saved to portfolio_summary.txt")

def main():
    print("=== Stock Portfolio Tracker ===")
    track_portfolio()

if __name__ == "__main__":
    main()
