import threading
import requests
from bs4 import BeautifulSoup
import os

urls = [
    'https://www.nytimes.com',
    'https://www.bbc.com',
    'https://www.cnn.com',
    'https://openai.com',
    'https://www.wikipedia.org',
]

def fetch_and_save_title(url, index):
    print(f'Fetching {url}...')
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No title found'
    except Exception as e:
        title = f'Error fetching: {e}'

    #save title to a file
    with open(f'title_thread_{index+1}.txt', 'w') as f:
        f.write(f'{url}\nTitle: {title}')
    print(f'Saved: title_thread_{index+1}.txt')

def scrape_with_threading():
        threads = []
        for i, url in enumerate(urls):
            t = threading.Thread(target=fetch_and_save_title, args=(url, i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

scrape_with_threading()
  
