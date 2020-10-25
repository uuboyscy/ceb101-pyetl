import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://www.ptt.cc/bbs/Baseball/M.1603603724.A.03C.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

articles = soup.select('div[id="main-content"]')[0]

# print(articles)
# print(articles.select('span'))
for i in articles.select('span'):
    print(i.extract())

print('===================================')
# print(articles)

for i in articles.select('div'):
    print(i.extract())

print('======================')

print(articles.text)
