import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 100,
    "MSFT": 200
}

def display_stocks():
    print("\nAvailable Stocks and Prices:")
    for symbol, price in stock_prices.items():
        print(f"{symbol}: ${price}")

def get_portfolio():
    portfolio = {}
    while True:
        display_stocks()
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol. Please try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid integer quantity.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    return portfolio

def display_summary(portfolio):
    print("\n--- Portfolio Summary ---")
    total = 0
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total += value
        print(f"{stock}: {quantity} shares × ${price} = ${value}")
    print(f"Total Investment: ${total}")

def save_portfolio(portfolio):
    filename = "portfolio.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Stock", "Quantity", "Price", "Total"])
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            total = price * quantity
            writer.writerow([stock, quantity, price, total])
    print(f"\nPortfolio saved to {filename}")

def main():
    print("Welcome to the Stock Portfolio Tracker!")
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    display_summary(portfolio)
    choice = input("\nDo you want to save the portfolio? (yes/no): ").lower()
    if choice.startswith('y'):
        save_portfolio(portfolio)
    print("\nThank you for using the Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
