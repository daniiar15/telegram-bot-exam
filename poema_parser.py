# Поэма
import requests
from bs4 import BeautifulSoup

base_url = "https://bookhouse.kg"

def get_books2():
    response = requests.get(f'{base_url}/catalog/2/54/')
    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all('div', class_='book-inner uk-card uk-card-default uk-card-hover book_inner_padding uk-margin')
    parsed_books = []
    
    for i in data:
        parsed_books.append({
            'name': i.find('div', class_="uk-width-1-1 uk-padding-top-10").text.strip(),
            'author_name': i.find('div', class_="uk-text-muted mavish").text.strip(),
            'price': i.find('span').text,
            'url_img': base_url + i.find("img").get("src"),
        })
    
    return parsed_books
