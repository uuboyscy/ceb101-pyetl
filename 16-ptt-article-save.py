import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('./pttArticle'):
    os.mkdir('./pttArticle')

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0, 3):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    titleSoupList = soup.select('div.title a')
    for titleSoup in titleSoupList:
        # aTag = titleSoup.select('a')[0]
        title = titleSoup.text
        articleUrl = 'https://www.ptt.cc' + titleSoup['href']
        print(title)
        print(articleUrl)
        # Request article url
        resArticle = requests.get(articleUrl, headers=headers)
        soupArticle = BeautifulSoup(resArticle.text, 'html.parser')
        articles = soupArticle.select('div[id="main-content"]')[0]
        for i in articles.select('span'):
            i.extract()
        for i in articles.select('div'):
            i.extract()

        # Article string
        articleContent = articles.text
        try:
            with open('./pttArticle/%s.txt'%(title), 'w', encoding='utf-8') as f:
                f.write(articleContent)
        except FileNotFoundError as e:
            title = title.replace('/', '-')
            with open('./pttArticle/%s.txt'%(title), 'w', encoding='utf-8') as f:
                f.write(articleContent)
        except OSError:
            pass

        print('==========')

    # Find new url
    newUrl = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    # print(newUrl)
    url = newUrl