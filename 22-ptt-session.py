import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url_landing_page = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
url_tmp = ''
url_ptt = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()

res_landing_page = ss.get(url_landing_page, headers=headers)
soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')

# Get url_tmp
url_tmp = 'https://www.ptt.cc' + soup_landing_page.select('form')[0]['action']
print(url_tmp)

# Create form data
data = dict()
input_key = soup_landing_page.select('input')[0]['name']
input_value = soup_landing_page.select('input')[0]['value']
data[input_key] = input_value
button_key = soup_landing_page.select('button')[0]['name']
button_value = soup_landing_page.select('button')[0]['value']
data[button_key] = button_value
print(data)

print(ss.cookies)

ss.post(url_tmp, data=data, headers=headers)

print(ss.cookies)

res = ss.get(url_ptt, headers=headers)
print(res.text)