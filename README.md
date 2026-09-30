# 🧾 Shop Bill Generator

A simple command-line billing tool written in pure Python. Enter items, quantities, prices and an optional discount — it prints the bill on screen and saves a receipt as a text file.

## Features

- Interactive command-line billing
- Input validation for quantity, price and discount
- Default item names (`Item_1`, `Item_2`, ...) if a name is left blank
- Optional discount percentage (0–100)
- Prints grand total, discount amount and final amount
- Saves every bill with a timestamp in the `bills/` folder

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only `os` and `datetime` from the standard library)

## Installation

```bash
git clone https://github.com/<your-username>/bill-generator.git
cd bill-generator
```

## Usage

```bash
python bill_generator.py
```

You will be asked for:

1. Number of items
2. For each item: name, quantity, price
3. Discount percentage (enter `0` for none)

## Example

```
====== SHOP BILLING ======
How many items? : 2

Item 1
Name: Pen
Qty: 10
Price: 5

Item 2
Name: Notebook
Qty: 3
Price: 40

Discount % (0 if none): 10
 BILL 
Name            Qty   Price   Total
Pen             10    5.0     50.0
Notebook        3    40.0     120.0
Grand Total = 170.0
Discount (10.0%) = 17.0
Final Amount = 153.0
Bill saved: bill_20260930_123257.txt
```

### Saved receipt (`bills/bill_20260930_123257.txt`)

```
BILL RECEIPT
Date: 2026-09-30 12:32:57

Name            Qty   Price   Total
Pen            10   5.0   50.0
Notebook       3   40.0   120.0

Grand Total = 170.0
Discount (10.0%) = 17.0
Final Amount = 153.0
```

## Project Structure

```
bill-generator/
├── bill_generator.py   # main program
├── README.md           # project documentation
├── requirements.txt    # dependencies (none)
├── LICENSE             # MIT License
└── .gitignore          # ignores generated bills and cache files
```

## How It Works

| Function        | Purpose                                              |
|-----------------|------------------------------------------------------|
| `get_number()`  | Asks for a whole number (quantity, item count)       |
| `get_price()`   | Asks for a non-negative price                        |
| `get_discount()`| Asks for a discount between 0 and 100               |
| `make_bill()`   | Collects items, prints the bill, saves the receipt   |

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
