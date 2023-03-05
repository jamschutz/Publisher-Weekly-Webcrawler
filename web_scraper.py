from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from datetime import datetime

# constants
BASE_URL = 'https://www.publishersweekly.com/pw/search/index.html?q=rights%20report%20graphic&sortByDate=on&fbclid=IwAR2_ynUNmfMHwEgRUoc6B33TNWtB9xbKxx1ytsvY4nC20A8DFc0kOKtKWbg'
RIGHTS_REPORT_START = 'Rights Report:'

def get_links_from_page(start_param):
    # download webpage
    # url = f'{BASE_URL}/{target_page}?page={str(page_number)}' if page_number > 1 else f'{BASE_URL}/{target_page}'
    url = f'{BASE_URL}&start={str(start_param)}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    list_of_links = soup.find('div', id='content-main').ul.find_all('a')

    links = []
    for item in list_of_links:
        if(item.text[:len(RIGHTS_REPORT_START)]) == RIGHTS_REPORT_START:
            links.append(item['href'])


    return links



def get_paragraphs_with_graphic(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    list_of_paragraphs = soup.find_all('p', class_='article')
    date = soup.find('div', class_='article-date').text.strip()

    data = {
        'date': date,
        'paragraphs': []
    }
    
    for p in list_of_paragraphs:
        if 'graphic' in p.text:
            data['paragraphs'].append(p.text)

    return data



print(get_paragraphs_with_graphic('https://www.publishersweekly.com/pw/by-topic/childrens/childrens-book-news/article/91613-rights-report-week-of-february-20-2023.html'))
