import requests

payload = {'key1': 'value1', 'key2': 'value2'}
res = requests.post("https://sans-foundations.com", data=payload)
print(res.url)
