from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://www.deviantart.com/popular-24-hours/')
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', 'torpedo-thumb-link')
for i in links:
    print(i['href'])



