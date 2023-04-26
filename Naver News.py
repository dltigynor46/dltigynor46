import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요: ")
url = "https://search.naver.com/search.naver?query=" + keyword + "&where=news"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

news_titles = soup.select('.news_tit')

with open('result.txt', 'w', encoding='utf-8') as f:
    for title in news_titles:
        f.write(title.get_text() + '\n')
