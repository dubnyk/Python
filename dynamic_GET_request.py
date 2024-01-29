import requests

payload = {'key1': 'value1', 'key2': 'value2'}
res = requests.get("https://website.com", params=payload)
print(res.url)
