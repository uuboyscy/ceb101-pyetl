import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

inputTags = soup.select('input')
for i in inputTags:
    try:
        if i['type'] == 'hidden':
            print(i)
            print(i['name'])
            print(i['value'])
    except:
        pass