import requests
import json
import os
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

if not os.path.exists('./dcard2'):
    os.mkdir('./dcard2')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=234672242'

res = requests.get(url, headers=headers)
# print(res.text)

jsonData = json.loads(res.text)
# print(jsonData[0])
# for k in jsonData[0].keys():
#     print(k)

for article in jsonData:
    title = article['title']
    titleUrl = 'https://www.dcard.tw/f/photography/p/' + str(article['id'])

    print(title)
    print(titleUrl)

    # print(jsonData[1]['mediaMeta'])
    for n, i in enumerate(article['mediaMeta']):
        imgUrl = i['url']
        print('\t' + imgUrl)
        # Save images
        try:
            # request.urlretrieve(imgUrl, './dcard/%s'%(title + str(n) + '.' + imgUrl.split('.')[-1]))
            resContent = requests.get(imgUrl, headers=headers)
            # with open('./dcard2/%s'%(title + str(n) + '.' + imgUrl.split('.')[-1]), 'wb') as f:
            #     f.write(resContent.content)
            with open('./dcard2/%s' % (title + imgUrl.split('/')[-1]), 'wb') as f:
                f.write(resContent.content)
        except FileNotFoundError:
            title = title.replace('/', '')
            request.urlretrieve(imgUrl, './dcard/%s'%(title + str(n) + '.' + imgUrl.split('.')[-1]))

    print('=====================')