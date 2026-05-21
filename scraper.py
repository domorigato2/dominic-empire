import requests
from bs4 import BeautifulSoup
import datetime

def scrape_and_save(url):
    print(f"[*] Infiltrating: {url}")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print("[+] TARGET SECURED. Extracting and saving data...\n")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('span', class_='titleline', limit=5)
            
            with open("hacker_news_leads.txt", "w", encoding="utf-8") as file:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                file.write(f"--- DATA EXTRACTION: {timestamp} ---\n")
                
                count = 1
                for item in headlines:
                    title = item.find('a').text
                    file.write(f"{count}. {title}\n")
                    print(f"{count}. {title}")
                    count += 1
                    
            print("\n[+] EXTRACTION COMPLETE. Data saved to hacker_news_leads.txt")
            
        else:
            print(f"[-] TARGET FAILED. Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"[!] CRITICAL ERROR: {e}")

if __name__ == "__main__":
    target_url = "https://news.ycombinator.com/"
    scrape_and_save(target_url)