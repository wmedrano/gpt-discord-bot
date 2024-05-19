import requests
from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class NewsStory:
    title: str
    url: str

def __get_url(element):
    siblings = element.find_next_siblings()
    if len(siblings) == 0:
        return None
    uri = siblings[0].find_all('a')[-1].attrs['href']
    url = f'https://news.ycombinator.com/{uri}'
    return url

def top_stories():
    url = 'https://news.ycombinator.com/'
    page = BeautifulSoup(requests.get(url).text, features='html.parser')
    stories = []
    for element in page.find_all(class_ = 'athing'):
        title = element.find('span', class_ = 'titleline').find('a').text
        url = __get_url(element)
        stories.append(NewsStory(title = title, url = url))
    return stories
