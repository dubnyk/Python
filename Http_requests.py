import requests

res = requests.get("https://websitehere.com")
print(res.text)

import requests

page = requests.get("http://localhost/secret.json")
print(page.text)
print(page.json()['name'])

### requesting data

import requests

res = requests.get("https://api.site.test/users/octodog")
print(res.json())


### parsing though data

import requests
import json

res = requests.get("https://api.site.test/users/octodog")
print(json.dumps(res.json(), indent=4))
