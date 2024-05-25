
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/thumbs_up")

res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)
