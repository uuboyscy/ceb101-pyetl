import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://www.ptt.cc/bbs/movie/index%s.html'
page = 9314

for i in range(0, 3):
    print('-------------%s---------------'%(i))
    res = requests.get(url%(page), headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    titleSoupList = soup.select('div.title')
    for titleSoup in titleSoupList:
        aTag = titleSoup.select('a')[0]
        title = aTag.text
        articleUrl = 'https://www.ptt.cc' + aTag['href']
        print(title)
        print(articleUrl)
        print('==========')

    page -= 1