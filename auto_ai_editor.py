import requests, json, os

url = "http://localhost:11434/api/generate"
with open(os.path.expanduser('/root/empire/main.py'), 'r') as f:
    code = f.read()

data = {
    "model": "deepseek-coder:1.3b",
    "prompt": f"Optimize this arbitrage bot for $204 trades. Output only the improved code:\n\n{code}",
    "stream": False
}

response = requests.post(url, json=data)
if response.status_code == 200:
    improved = response.json()['response']
    with open('/root/empire/improved_main.py', 'w') as f:
        f.write(improved)
    print("AI upgraded your bot — check improved_main.py")
else:
    print("Error — check Ollama is running")
