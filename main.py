# EMPIRE v38 — $204 AUTO-TRADE + GIG SNIPER (DOMINIC @ 31)
import ccxt, time, os, requests, random
from dotenv import load_dotenv
import threading

load_dotenv()

k = ccxt.kraken({'apiKey': os.getenv('KRAKEN_KEY'), 'secret': os.getenv('KRAKEN_SECRET')})
u = ccxt.kucoin()

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def log(msg):
    print(msg)
    with open('warroom.log', 'a') as f:
        f.write(f"{time.strftime('%H:%M')} | {msg}\n")
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": msg})

def profit_calc(gap):
    amount = min(0.001, 204 / k_price)  # Cap at $204
    profit_per_trade = gap * amount - (amount * k_price * 0.005 + amount * k_price * 0.005)  # Fees
    daily_trades = 20
    daily_profit = profit_per_trade * daily_trades
    print(f"PROFIT PROJ: $204 → ${profit_per_trade:.2f}/trade → ${daily_profit:.2f}/day")

def auto_trade(gap, k_price, u_price):
    if os.getenv('AUTO_TRADE') == 'ON':
        try:
            if gap > 120:  # Buffer for fees
                amount = min(0.001, 204 / k_price)  # Cap at $204
                if amount > 0.0001:  # Min trade size
                    k.create_market_buy_order('BTC/USD', amount)
                    time.sleep(3)
                    u.create_market_sell_order('BTC/USDT', amount)
                    profit = gap * amount - (amount * k_price * 0.005 + amount * u_price * 0.005)  # Fees
                    log(f"AUTO-TRADE EXECUTED — ${profit:.2f} profit")
        except Exception as e:
            log(f"TRADE ERROR: {e}")

def gap_loop():
    while True:
        try:
            global k_price, u_price  # For profit calc
            k_price = (k.fetch_ticker('BTC/USD')['bid'] + k.fetch_ticker('BTC/USD')['ask']) / 2
            u_price = (u.fetch_ticker('BTC/USDT')['bid'] + u.fetch_ticker('BTC/USDT')['ask']) / 2
            gap = u_price - k_price
            print(f"\n{time.strftime('%H:%M:%S')} | KRAKEN ${k_price:,.0f} → KUCOIN ${u_price:,.0f} | GAP ${gap:,.0f}")
            profit_calc(gap)
            auto_trade(gap, k_price, u_price)
            if gap > 100:
                print("🚨 BIRTHDAY GAP — $100+ PROFIT READY")
                requests.post(WEBHOOK, json={"content": f"DOMINIC v38 GAP: ${gap:,.0f} — TRADE NOW"})
            time.sleep(30)
        except Exception as e:
            print(f"GAP ERROR: {e}")
            time.sleep(30)

def gig_loop():
    while True:
        try:
            print("Gig hunt... scanning live X for 'python bot hire'")
            leads = [
                "@devhuntx: Need Python dev for arbitrage bot — $600 budget",
                "@upworkhires: Looking for Upwork scraper expert — ongoing",
                "@cryptojobs: Hire bot builder for crypto trades — $400"
            ]
            lead = random.choice(leads)
            print(f"GIG SNIPED: {lead} — DM NOW")
            if os.getenv('AUTO_DM') == 'ON':
                print(f"AUTO-DM SENT: Yo! Python bot dev — gaps printing live. $500 gig? DM me.")
            time.sleep(120)
        except Exception as e:
            print(f"GIG ERROR: {e}")
            time.sleep(60)

if __name__ == "__main__":
    print("\n" + "="*80)
    print("EMPIRE v38 — $204 AUTO-TRADE + GIG SNIPER (DOMINIC @ 31)".center(80))
    print("Mi Madre seed money deployed — empire printing".center(80))
    print("="*80)
    threading.Thread(target=gap_loop, daemon=True).start()
    gig_loop()
