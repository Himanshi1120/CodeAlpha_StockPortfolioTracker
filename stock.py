import csv

prices = {
    "AAPL": 180, "TSLA": 250, "GOOGL": 2800, "AMZN": 3400, "MSFT": 330,
    "NFLX": 420, "META": 310, "NVDA": 710, "IBM": 140, "INTC": 34,
    "ORCL": 120, "ADBE": 530, "CRM": 230, "BABA": 90, "AMD": 160,
    "UBER": 60, "LYFT": 13, "PINS": 30, "SHOP": 65, "PYPL": 70,
    "COIN": 200, "SQ": 75, "DIS": 95, "SONY": 85, "T": 17,
    "VZ": 35, "PEP": 170, "KO": 60, "MCD": 280, "NKE": 100,
    "JPM": 160, "BAC": 40, "WMT": 160, "COST": 700, "BA": 180
}

data = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in prices:
        print("Stock not found. Try one of:", ', '.join(prices.keys()))
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        if stock in data:
            data[stock] += qty
        else:
            data[stock] = qty
    except:
        print("Invalid quantity")

total = 0
print("\nYour Stock Portfolio:")
for stock, qty in data.items():
    price = prices[stock]
    value = price * qty
    print(f"{stock}: {qty} x ${price} = ${value}")
    total += value

print(f"\nTotal Investment: ${total}")

save = input("Save result? (yes/no): ").lower()
if save == "yes":
    file_type = input("File type (txt/csv): ").lower()
    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            for stock, qty in data.items():
                f.write(f"{stock}: {qty} x ${prices[stock]} = ${qty*prices[stock]}\n")
            f.write(f"\nTotal Investment: ${total}")
        print("Saved to portfolio.txt")
    elif file_type == "csv":
        with open("portfolio.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in data.items():
                writer.writerow([stock, qty, prices[stock], qty*prices[stock]])
            writer.writerow(["", "", "Total", total])
        print("Saved to portfolio.csv")
    else:
        print("Invalid file type.")
