import asyncio
import aiohttp
from requests import session
import asyncio_new
from bs4 import BeautifulSoup
from urllib.parse import urlparse

urls = [
    'https://python.org',
    'https://www.datacamp.com',
    'https://www.wikipedia.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
]

async def fetch_title(session, url):
    print(f'Fetching {url}...')
    try:
        async with session.get(url, timeout=10) as response:
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            title = soup.title.string if soup.title else 'No title found'
    except Exception as e:
        title = f'Error fetching: {e}'

    #get website domaain name
    domain = urlparse(url).netloc.replace('www.', '')
    filename = f'title_async_{domain}.txt'

    with open(filename, 'w') as f:
        f.write(f'{url}\nTitle: {title}')
    print(f'Saved: {filename}')

async def scrape_with_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_title(session, url)
            for url in urls
        ]
        await asyncio.gather(*tasks)

asyncio.run(scrape_with_asyncio())
