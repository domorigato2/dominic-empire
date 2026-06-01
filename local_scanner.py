import socket
import sys
from datetime import datetime

target = "127.0.0.1"

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan ports 1 through 1024
    for port in range(1, 9001):
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01) # Very fast timeout for local scanning
        
        # connect_ex returns an error indicator instead of throwing an exception
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
