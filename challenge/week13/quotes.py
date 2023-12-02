import operator
import urllib.request as ur
from bs4 import BeautifulSoup as bs

# 웹 페이지에서 텍스트 추출
url = "https://quotes.toscrape.com/tag/life/"
html = ur.urlopen(url)
soup = bs(html.read(), "html.parser")

# 웹 페이지에서 추출한 텍스트에서 단어 빈도 계산
total_terms = set()
term_frequency_dict = {}

# 각 문장을 소문자로 변환하고, 마침표를 제거한 후, 공백을 기준으로 단어로 분리한 다음, total_terms 세트에 추가
for quote in soup.find_all("span", class_="text"):
    words = quote.get_text().lower().replace(".", "").split()
    total_terms.update(words)

# 각 문장을 소문자로 변환하고, 마침표를 제거한 후, 공백을 기준으로 단어로 분리
# 이미 딕셔너리에 있는 단어라면 빈도를 증가시키고, 없는 단어라면 새로운 키로 추가
for quote in soup.find_all("span", class_="text"):
    words = quote.get_text().lower().replace(".", "").split()
    for word in words:
        if word in term_frequency_dict:
            term_frequency_dict[word] += 1
        else:
            term_frequency_dict[word] = 1

# 빈도에 따라 내림차순으로 정렬
sorted_tf = sorted(term_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)

# 상위 5개의 단어 출력
print("-----Top-5 Terms from the Web Page-----")
for rank, (word, frequency) in enumerate(sorted_tf[:5], 1):
    print(rank, word, frequency)
