import requests

# Example 1 - being Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
}
response = requests.get('https://httpbin.test/news-page', headers=headers)

# Example 2 - being Googlebot # bypass paywall
headers['User-Agent'] = 'Googlebot/2.1 (+http://www.google.com/bot.html)'
response = requests.get('https://httpbin.test/restricted-article', headers=headers)

# Example 3 - being something else
headers['User-Agent'] = 'PickleBrowser/1.337'
response = requests.get('https://httpbin.test/admin/login', headers=headers)
