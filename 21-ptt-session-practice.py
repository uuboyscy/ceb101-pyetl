import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()

ss.cookies['over18'] = '1'

res = ss.get(url)

print(res.text)