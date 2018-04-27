from bs4 import BeautifulSoup
from urllib.request import urlopen


def steal_image(links):
    pass


def collect_links(tag, max_count):
    big_black_bag = set()
    offset = 0
    while True:
        html = urlopen('https://www.deviantart.com/?q=' + tag + '&offset=' + str(offset))
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', 'torpedo-thumb-link')
        for link in links:
            big_black_bag.add(link['href'])
            if len(big_black_bag) == max_count:
                return big_black_bag
        offset += 24


for i in collect_links('mlp', 54):
    print(i)