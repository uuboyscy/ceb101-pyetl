import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

data = {
    'action': 'fm_ajax_load_more',
    'nonce': '67dd76aa6f',
    'page': 1
}

for page in range(0, 5):
    res = requests.post(url, headers=headers, data=data)

    # print(res.text)
    jsonData = json.loads(res.text)
    # print(jsonData.keys())
    # print(jsonData['data']) # HTML string
    soup = BeautifulSoup(jsonData['data'], 'html.parser')
    for a in soup.select('a'):
        print(a['onclick'].split(',')[-2])
        print(a['href'])

    data['page'] += 1