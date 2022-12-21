
import requests
from bs4 import BeautifulSoup as BS 
import csv 

def get_html(url):
    response = requests.get(url)
    return response.text 

def get_soup(html):
    soup = BS(html,'lxml')
    return soup


def get_buses(soup):
    bus = soup.find_all('div',class_='list-item list-label')
    info = soup.find_all('div', class_='list-item list-label new-line')
    # for bus in bus:

    
    for bus in info:
        bus.find('h2',class_='name')
        try:
            title = bus.find('h2', class_='name').text.strip()
        
        except AttributeError:
            title = ''
        
        try:
            price = bus.find('strong').text.strip()

        except AttributeError:
            price = ''
        try: 
            image=bus.find('img',class_='lazy-image').get('data-src')
        
        except AttributeError:
            image =''
        
        try:
            description=bus.find('p', class_='year-miles').text.strip()

        except AttributeError:
            description =''


        write_csv({
            'title': title,
            'price': price,
            'image': image,
            'description': description
        })

def write_csv(data):
    with open('bus.csv','a')as file:
        names =['title', 'price','image', 'description']
        write = csv.DictWriter (file, delimiter=',',fieldnames=names)
        write .writerow(data)



def main():
    for i in range(1, 1000):
        url = f'https://www.mashina.kg/commercialsearch/all/?page=166/page-{1}'
        html = get_html(url)
        soup = get_soup(html)
        get_buses(soup)
        print(f'спарсили {i} страница')


if __name__ == '__main__':
    main()

