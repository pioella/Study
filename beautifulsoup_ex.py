import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do'
params = {'currentPage': 1, 'rowPerPage': 300}
html = requests.get(url, params=params).text
soup = BeautifulSoup(html, 'html.parser')

for idx, tag in enumerate(soup.select('a[href*=jsMemPop]'), 1):
    print('[{}] {}'.format(idx, tag.text))


# with urlopen('https://www.zum.com/') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.select("span.keyword"):
#         print(anchor.get_text())
