import urllib.request as req
from bs4 import BeautifulSoup
url = "http://media.daum.net"
res = req.urlopen(url)
source = res.read()
source = source.decode("utf-8")
html = BeautifulSoup(sourse, 'html.parser')
atags = html.select('a[class=link_txt]')
print('a tag 수=', len(atags))
crawling_data = []
cnt = 0
for atags in atags:
    cnt += 1
    atagsStr = str(atags.string)
    crawling_data.append(atagsStr.strip())
    string.strip()
print('수집한 자료 확인')
print(crawling_data)
