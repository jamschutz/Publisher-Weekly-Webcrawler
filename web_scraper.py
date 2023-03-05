from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from datetime import datetime

# constants
BASE_URL = 'https://www.publishersweekly.com/pw/search/index.html?q=rights%20report%20graphic&sortByDate=on&fbclid=IwAR2_ynUNmfMHwEgRUoc6B33TNWtB9xbKxx1ytsvY4nC20A8DFc0kOKtKWbg'
# ARTICLE_DIV_CLASS = 'card-item__content'
# ARTICLE_TITLE_CLASS = 'card-item__link'
# in format: Wednesday, Feb 15, 2023 10:36am
# DATETIME_FORMAT = '%A, %b %d, %Y %I:%M%p'


def get_links_from_page(start_param):
    # download webpage
    # url = f'{BASE_URL}/{target_page}?page={str(page_number)}' if page_number > 1 else f'{BASE_URL}/{target_page}'
    url = f'{BASE_URL}&start={str(start_param)}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    list_of_links = soup.find('div', id='content-main').ul.find_all('a')

    links = []
    for item in list_of_links:
        links.append(item['href'])


    return links

    # articles = soup.find_all('div', class_=ARTICLE_DIV_CLASS)

    # article_data = []

    # for article in articles:
    #     article_title = article.a.h4.text
    #     article_url   = article.a['href']
    #     article_date  = article.find('time')['datetime']

    #     # convert to datetime
    #     article_date = datetime.strptime(article_date, DATETIME_FORMAT)

    #     article_data.append({
    #         'title': article_title,
    #         'url': article_url,
    #         'date': article_date
    #     })

    # return article_data


print(len(get_links_from_page(15)))
