import json

import requests

BASE = "http://127.0.0.1:5000/"

print("get".center(60,"-"))

response = requests.get(BASE + "getplayer/ponting")

res = response.json()
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 60)
print("put".center(60, "-"))
response = requests.put(BASE + 'getplayer/ponting', data = {'team': 'Australia'})
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 60)
print("patch".center(60, "-"))
data = {'name': 'Sachin Ramesh Tendulkar'}

response = requests.patch(BASE + 'getplayer/sachin', json= json.dumps(data))
res = response.json()

print(res)

print("-" * 60)
print("post".center(60, "-"))

virat = {'name': 'Virat Kholi', 'runs': 28600, 'matches': 650, 'wicket': 85}
response = requests.post(BASE + 'getplayer/virat', json = json.dumps(virat))
res = response.json()

print(res)
print("-" * 60)
print("delete".center(60, "-"))
response = requests.delete(BASE + "getplayer/lara")

res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)