import requests
from bs4 import BeautifulSoup
import pprint

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
headers = {'User-Agent': userAgent}

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'

dataStr = """
method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/10/25
awardAnnounceEndDate: 109/10/25
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢
"""

data = dict()
for r in dataStr.split('\n'):
    if r != '':
        data[r.split(':')[0]] = r.split(': ')[1]
data = {r.split(':')[0]: r.split(': ')[1] for r in dataStr.split('\n') if r != ''}

pprint.pprint(data)
data['awardAnnounceStartDate'] = '109/10/23'

res = requests.post(url, data=data, headers=headers)

# print(res.text)
