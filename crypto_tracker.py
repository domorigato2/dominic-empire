import requests
import datetime

def get_bitcoin_price():
    # Using Blockchain.info's free, highly stable API (No key needed)
    url = "https://blockchain.info/ticker"
    
    print("========================================")
    print("[*] CONNECTING TO BLOCKCHAIN.INFO API...")
    print("========================================")
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract the USD last price and symbol
            price = data["USD"]["last"]
            symbol = data["USD"]["symbol"]
            
            print("[+] CONNECTION SECURED.")
            print("----------------------------------------")
            print(f"📈 CURRENT BITCOIN PRICE: {symbol}{price:,.2f} USD")
            print("----------------------------------------")
            
            # Append the timestamped price to your local log file
            with open("bitcoin_prices.txt", "a") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] ${price:,.2f} USD\n")
                
            print("[+] Price point logged to bitcoin_prices.txt")
            print("========================================")
            
        else:
            print(f"[-] API connection failed. Status: {response.status_code}")
            
    except Exception as e:
        print(f"[!] Error contacting API: {e}")

if __name__ == "__main__":
    get_bitcoin_price()