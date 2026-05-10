# --- EMPIRE WAR CHEST TRACKER v1.0 ---
# Operator: Dominic

def calculate_gap():
    target = 1000.00
    current_balance = 751.00 # Update this to your exact PayPal/Heartland balance
    
    gap = target - current_balance
    mowing_price = 25.00
    attapoll_daily = 2.00
    
    print("="*40)
    print("🚀 EMPIRE FINANCIAL TELEMETRY")
    print("="*40)
    print(f"Current War Chest: ${current_balance:.2f}")
    print(f"Target Goal:       ${target:.2f}")
    print(f"Remaining Gap:     ${gap:.2f}")
    print("-" * 40)
    
    lawns_needed = round(gap / mowing_price, 1)
    days_of_grind = round(gap / attapoll_daily, 1)
    
    print(f">>>[ACTION] Mow {lawns_needed} more lawns to hit target.")
    print(f">>>[OR] Grind microtasks for {days_of_grind} more days.")
    print("-" * 40)
    
    if gap <= 0:
        print("✅ STATUS: EMERGENCY FUND SECURED. INITIATE INVESTMENT PHASE.")
    else:
        print("⚠️ STATUS: HARDENED NODE IN PROGRESS. KEEP GRINDING.")
    print("="*40)

if __name__ == "__main__":
    calculate_gap()