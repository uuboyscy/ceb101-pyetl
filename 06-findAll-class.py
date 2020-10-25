from urllib import request
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://www.ptt.cc/bbs/joke/index.html'

req = request.Request(url, headers=headers)
res = request.urlopen(req)

htmlStr = res.read().decode('utf-8')
soup = BeautifulSoup(htmlStr, 'html.parser')

board = soup.findAll('a', class_='board')

print(board)