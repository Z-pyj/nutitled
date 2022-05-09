from bs4 import BeautifulSoup as bs

soup = bs(open('./doubantop100.html', encoding='utf-8'))

print(soup)

