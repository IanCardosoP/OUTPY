import os, json, requests 
from datetime import datetime
from coinmarketcap_api import fetch_cryptocurrency_data

GOLDEN_TARJET = 2.9

# Open json file for assets
def load_assets():
    with open('assets.json', 'r') as file:
        return json.load(file)

# update json assets file
def write_to_assets():
    with open('assets.json', 'w') as file:
        json.dump(assets, file, indent=4)

assets = load_assets()

def fetch_data():
    for asset, data in assets.items():
        assets[asset]["price"] = fetch_cryptocurrency_data(data['symbol'])
    write_to_assets()
fetch_data()

# Clear terminal
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Header      
def print_header():
    print("Assets found:")
    for asset, data in assets.items():
        total_value = data["price"] * data["quantity"]
        print(f"\t[{data['symbol']}: {data['quantity']} tokens at ${data['price']} = ${total_value:.2f} USD]")

# Sellings Log
def show_salelog():
    print("cat on salelog.txt")
    try:
        with open('salelog.txt', 'r') as log_file:
            print(log_file.read())
    except FileNotFoundError:
        print("E: salelog.txt not found (FileNotFoundError)")

# asset validation
def validate_asset(key):
    return key in assets

# LOG IN IN salelog.txt
def set_salelog(asset, percent, price, quantity_sold):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"{timestamp} | Asset: {assets[asset]['symbol']} | Percent Sold: {percent:.2f}% | "
                 f"Quantity Sold: {quantity_sold:.2f} | Sell Price: ${price:.2f} USD\n")
    
    with open('salelog.txt', 'a') as log_file:
        log_file.write(log_entry)

    return log_entry

# sell_asset
def sell_asset(asset):
    price = assets[asset]["price"]
    quantity = assets[asset]["quantity"]

    percent = (price - 2) * 5
    quantity_to_sell = quantity * (percent / 100)
    assets[asset]["quantity"] -= quantity_to_sell

    print(f"Sell {percent:.2f}% equal to {quantity_to_sell:.2f} {assets[asset]["symbol"]}")


    write_to_assets()
    print("Data has been updated.")
    print(set_salelog(asset, percent, price, quantity_to_sell))


def main_gui():
    while True:
        print_header()   
        user_input = input("Type symbol to sell, 'salelog' or 'exit': ").lower()

        if validate_asset(user_input):
            cls()
            if assets[user_input]["price"] <= GOLDEN_TARJET:
                print("It's too early to sell. Stay calm and hold strong— don't let doubt make you give up what you've built. Remember, strong hands reap the greatest rewards.")
            else: sell_asset(user_input)
        elif user_input == "salelog":
            cls()
            show_salelog()
        elif user_input == "exit":
            cls()
            break
        else:
            cls()
            print("\tE: Asset not found.")   

        
main_gui()
