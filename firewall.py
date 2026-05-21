import datetime
import time

def activate_firewall():
    print("="*50)
    print("🛡️  NICOTINE FIREWALL ACTIVE  🛡️")
    print("="*50)
    
    try:
        level = int(input("Enter Craving Level (1-10): "))
        excuse = input("What is the malware's excuse for wanting a smoke? ")
        
        print("\n[*] ANALYZING MALWARE SIGNATURE...")
        time.sleep(2)  # Pauses the terminal for 2 seconds for dramatic effect
        
        print("\n>>> ARCHITECT OVERRIDE <<<")
        print(f"[-] Excuse Rejected: '{excuse}' is a biological lie.")
        print("[!] You are the Root User. You do not negotiate with receptors.")
        
        # Log the craving to a persistent file
        with open("craving_log.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            file.write(f"[{timestamp}] Level: {level}/10 | Excuse: {excuse} | Status: PACKET DROPPED\n")
            
        print("\n[+] Craving logged to persistent storage. DROP THE PACKET.")
        print("="*50)
        
    except ValueError:
        print("\n[!] ERROR: Craving level must be a number. Reboot script.")

if __name__ == "__main__":
    activate_firewall()