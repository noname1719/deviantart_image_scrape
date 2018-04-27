from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve


def steal_image(links):
    for link in links:
        html = urlopen(link)
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find('img', 'dev-content-normal')['src']
        info = soup.find('div', 'dev-title-container ').find('h1').get_text().split(' by ')
        print(img+'                '+info[0]+'              '+info[1])


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


urls = collect_links('nature', 15)
steal_image(urls)
