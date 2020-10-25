import requests

url = 'https://803c13ad001c.ngrok.io/hello_get?name=Allen&age=22'

res = requests.get(url=url)

resStr = res.text
print(resStr)
print(type(resStr))
