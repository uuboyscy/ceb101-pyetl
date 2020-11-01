from selenium.webdriver import Chrome
import requests

driver = Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)

driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookies = driver.get_cookies()

newCookies = dict()
for c in cookies:
    print(c)
    newCookies[c['name']] = c['value']

res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies=newCookies)
print(res.text)

