import requests

url = 'http://httpbin.org/post'

data = {
    'username': 'test',
    'test': 'aaaaaa'
}

res = requests.post(url, data=data)

print(res.text)