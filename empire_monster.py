# EMPIRE MONSTER v1 — DOMINIC @ 31 (LOCAL HUSTLE BEAST)
import os, subprocess, time, random
from datetime import datetime

VAULT_DIR = '/home/domorigato2/vault/bots'  # absolute vault/bots
LOG_FILE = '/home/domorigato2/vault/logs/monster.log'

def log(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {msg}")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {msg}\n")

def run_bot(bot_name):
    full_path = f'{VAULT_DIR}/{bot_name}'
    if not os.path.exists(full_path):
        log(f"ERROR: {bot_name} not found in {VAULT_DIR}")
        return
    try:
        log(f"MONSTER RUN: {bot_name.upper()} — HUSTLE MODE")
        result = subprocess.run(['python3', full_path], cwd=VAULT_DIR, capture_output=False, check=True)
        log(f"{bot_name} DONE — CHECK LOGS")
    except Exception as e:
        log(f"{bot_name} CRASHED: {e}")

def menu():
    bots = [
        'gig_hunter.py', 'upwork_hunter_pro.py', 'job_scraper.py', 'main.py',
        'ai_resume_fiverr.py', 'money_terminal.py', 'the_dopest_script_ever.py',
        'arbitrage_alert.py', 'money_ops_v5.py', 'root_dashboard.py'
    ]
    print("\n" + "="*50)
    print("EMPIRE MONSTER v1 — DOMINIC @ 31 — LOCAL HUSTLE BEAST")
    print("="*50)
    for i, bot in enumerate(bots, 1):
        print(f"{i}. {bot}")
    print(f"{len(bots)+1}. Logs (tail -f {LOG_FILE})")
    print(f"{len(bots)+2}. All (run 3 random)")
    print(f"{len(bots)+3}. Status (check PIDs)")
    print(f"{len(bots)+4}. Exit")
    choice = input("Pick your poison: ")
    if choice == str(len(bots)+1):
        subprocess.run(['tail', '-f', LOG_FILE])
    elif choice == str(len(bots)+2):
        random_bots = random.sample(bots, 3)
        for bot in random_bots:
            run_bot(bot)
            time.sleep(2)
    elif choice == str(len(bots)+3):
        subprocess.run(['pgrep', '-f', 'python3.*bots'])
    elif 1 <= int(choice) <= len(bots):
        run_bot(bots[int(choice)-1])
    else:
        exit()

if __name__ == "__main__":
    log("EMPIRE MONSTER v1 LAUNCHED — CLEAN VAULT, ALL HUSTLE")
    while True:
        menu()
