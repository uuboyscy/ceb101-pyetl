from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://httpbin.org/get'
url = 'https://803c13ad001c.ngrok.io/hello_get?name=Allen&age=22'

res = request.urlopen(url=url)

resStr = res.read().decode('utf-8')
print(resStr)
print(type(resStr))