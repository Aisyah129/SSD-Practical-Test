import time
import requests

url = "http://127.0.0.1:5050"

for i in range(10):
    try:
        resp = requests.get(url)
        print("Connected!")
        break
    except Exception as e:
        print(f"Retry {i+1}: {e}")
        time.sleep(1)
else:
    raise Exception("Server never came online.")
