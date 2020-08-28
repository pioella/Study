import requests
url = 'https://image-comic.pstatic.net/webtoon/662774/192/20200602115727_2138d19521a021b561c26376a0e8c579_IMAG01_1.jpg'
headers = {'Referer': 'http://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=192&weekday=wed'}
res = requests.get(url, headers=headers)
with open('test.jpg', "wb") as f:
    f.write(res.content)
