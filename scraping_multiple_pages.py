import time

import requests
from bs4 import BeautifulSoup
# import pprint


def all_data(pages=5):
    all_stories = []

    def sorting(hnlist):
        return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

    for page in range(1, pages + 1):
        url = f'https://news.ycombinator.com/news?p={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select('.titleline')
        votes = soup.select('.score')

        for idx, item in enumerate(links):
            a_tag = item.find('a')
            title = item.getText()
            href = a_tag.get('href', None)
            if idx<len(votes): #or if len(vote): /this mean True or != 0
                vote = votes[idx]
                if vote:
                    points = int(vote.getText().replace(' points', ''))
                    if points > 99:  # Optional: filter popular posts
                        all_stories.append({'title': title, 'link': href, 'votes': points})
        time.sleep(5)
    return sorting(all_stories)



result = all_data(5)
# for item in result:
#     print(item) --- returns all items in the appended dictionary
for n, item in enumerate(result, start=1):
    # print(f'{n} -- {item['title']}') # this numbers the scraped pages titles
    print(f"{n}. {item['title']} ({item['link']})") # to grab more than one item in the dictionary




