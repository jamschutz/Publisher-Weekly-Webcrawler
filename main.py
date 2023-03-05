import web_scraper as ws
import json, time
from pathlib import Path
from datetime import datetime
import random


def get_all_urls():
    urls = []

    start = 0
    end = 1530
    increment = 15

    current = start

    # build sitemap 1 by 1, rotating proxies as needed
    while current <= end:
        try:
            # get articles at page number
            print(f'fetching page {str(current)}')
            urls_in_page = ws.get_links_from_page(current)

            # if we got here, proxy worked!
            urls.extend(urls_in_page)
            current += 15

            # don't spam
            time.sleep(random.uniform(0.9, 2.1))
        except Exception as e:
            # get next proxy
            print(f'{str(e)}\n\n----------port {proxies[current_proxy]} is bad. trying next one----------')
            return urls
    
    return urls



def get_all_paragraphs():
    urls = []
    with open('urls.json') as f:
        urls = json.load(f)

    relevant_paragraphs = []
    counter = 1
    for url in urls:
        print(f'getting url {counter} of {len(urls)}')
        relevant_paragraphs.extend(ws.get_paragraphs_with_graphic(url))
        counter += 1

    return relevant_paragraphs



# all_urls = get_all_urls()# save sitemap
# with open("urls.json", "w") as json_file:
#     json.dump(all_urls, json_file)
# print('done')


paragraphs = get_all_paragraphs()
with open("paragraphs.json", "w") as json_file:
    json.dump(paragraphs, json_file)
print('done')