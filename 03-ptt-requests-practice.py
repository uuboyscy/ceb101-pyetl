import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/joke/index.html'

res = requests.get(url, headers=headers)

print(res.text)