from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve


'''html = urlopen('https://dashakern.deviantart.com/art/Nature-Design-742194266')
soup = BeautifulSoup(html, 'html.parser')
author = soup.find('small', 'author').find('a').get_text()
print(author)'''

string = 'pure nature by MateuszPisarski'
res = string.split(' by ')
print(res)