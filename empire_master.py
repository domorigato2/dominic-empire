# EMPIRE MASTER v4.4 — DOMINIC @ 31 (COMMAND MODES, LOCAL HUSTLE)
import os, subprocess, time, random, sys
from datetime import datetime

EMP_DIR = '/home/domorigato2/projects/bots'  # absolute projects/bots path
VENV_DIR = '/home/domorigato2/empire/crypto_empire/bin/activate'  # venv path
LOG_FILE = 'empire_master.log'

def log(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {msg}")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {msg}\n")

def install_dep(dep):
    try:
        cmd = f'source {VENV_DIR} && pip install {dep}'
        subprocess.run(['bash', '-c', cmd], cwd=EMP_DIR, check=True)
        log(f"INSTALLED {dep} — READY TO ROLL")
    except Exception as e:
        log(f"INSTALL ERROR: {e}")

def run_bot(bot_name, retry=2):
    full_path = f'{EMP_DIR}/{bot_name}'
    if not os.path.exists(full_path):
        log(f"ERROR: {bot_name} not found in {EMP_DIR}")
        return
    for attempt in range(retry):
        try:
            # Auto-install bs4 for scrapers
            if 'scraper' in bot_name or 'job' in bot_name:
                install_dep('beautifulsoup4')
            log(f"RUNNING {bot_name.upper()} — EMPIRE MODE (attempt {attempt+1})")
            # Auto-venv activation
            cmd = f'source {VENV_DIR} && python3 {full_path}'
            result = subprocess.run(['bash', '-c', cmd], cwd=EMP_DIR, capture_output=False, check=True)
            log(f"{bot_name} DONE — CHECK LOGS")
            return
        except subprocess.CalledProcessError as e:
            log(f"{bot_name} CRASHED: {e} (attempt {attempt+1})")
        except Exception as e:
            log(f"{bot_name} ERROR: {e} (attempt {attempt+1})")
    log(f"{bot_name} FAILED AFTER {retry} ATTEMPTS")

def menu():
    bots = [
        'gig_hunter.py', 'upwork_hunter_pro.py', 'job_scraper.py', 'main.py',
        'ai_resume_fiverr.py', 'money_terminal.py', 'the_dopest_script_ever.py',
        'arbitrage_alert.py', 'money_ops_v5.py', 'root_dashboard.py'
    ]
    print("\n" + "="*50)
    print("EMPIRE MASTER v4.4 — DOMINIC @ 31 — LOCAL HUSTLE")
    print("="*50)
    for i, bot in enumerate(bots, 1):
        print(f"{i}. {bot}")
    print(f"{len(bots)+1}. Logs (tail -f {LOG_FILE})")
    print(f"{len(bots)+2}. All (run 3 random)")
    print(f"{len(bots)+3}. Status (check running bots)")
    print(f"{len(bots)+4}. Exit")
    choice = input("Pick your poison: ")
    try:
        choice_int = int(choice)
        if choice_int == len(bots)+1:
            subprocess.run(['tail', '-f', LOG_FILE])
        elif choice_int == len(bots)+2:
            random_bots = random.sample(bots, 3)
            for bot in random_bots:
                run_bot(bot)
                time.sleep(2)
        elif choice_int == len(bots)+3:
            subprocess.run(['pgrep', '-f', 'python3.*bots'])
        elif 1 <= choice_int <= len(bots):
            run_bot(bots[choice_int-1])
        else:
            exit()
    except ValueError:
        log(f"INVALID CHOICE: {choice} — TRY A NUMBER")
    except Exception as e:
        log(f"MENU ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'auto':
        log("EMPIRE MASTER AUTO — LAUNCHING 3 BOTS")
        random_bots = random.sample(bots, 3)
        for bot in random_bots:
            run_bot(bot)
        exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'phone':
        with open('warroom.log', 'r') as f:
            lines = f.readlines()
            gaps = [line for line in lines if 'GAP' in line]
            if gaps:
                latest_gap = gaps[-1].split('GAP ')[1].split('|')[0]
                log(f"PHONE ALERT: Latest gap ${latest_gap} — DM @upworkhires now")
        exit()
    log("EMPIRE MASTER v4.4 LAUNCHED — INPUT VALIDATION, ALL HUSTLE")
    while True:
        menu()
