# CodeAlpha_StockPortfolioTracker

A simple console-based stock portfolio tracker built in Python as part of the CodeAlpha Python Programming internship (Task 2).

## About

The user enters stock names and quantities, and the tracker calculates the total investment using a fixed set of predefined stock prices. The final summary can optionally be saved to a text file.

## Features

- Predefined dictionary of stock prices (AAPL, TSLA, GOOGL, AMZN, MSFT)
- Add multiple stocks with quantities, one at a time
- Automatic total investment calculation
- Per-stock summary showing quantity and value
- Option to save the summary to `portfolio_summary.txt`
- Basic input validation for stock names and quantities

## Requirements

- Python 3.6+

No external dependencies — uses only the standard library.

## Usage

Run the script:

```bash
python stock_tracker.py
```

Enter a stock name and quantity when prompted. Type `done` as the stock name when you're finished adding stocks.

## Example

```
=== Stock Portfolio Tracker ===

Available stocks:
AAPL: $180
TSLA: $250
GOOGL: $140
AMZN: $145
MSFT: $330

Enter stock name and quantity. Type 'done' as stock name to finish.

Stock name: AAPL
Quantity: 10
Added 10 shares of AAPL ($1800)
Stock name: done

--- Portfolio Summary ---
AAPL: 10 shares, Value: $1800

Total Investment: $1800
```

## Concepts Used

Dictionaries, input/output, basic arithmetic, file handling.

## License

Free to use, modify, and distribute.
