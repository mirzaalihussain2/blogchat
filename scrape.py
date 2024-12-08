from firecrawl import FirecrawlApp
from bs4 import BeautifulSoup
import pprint
from urllib.parse import urlparse
import re
import os

from dotenv import load_dotenv
load_dotenv()

def filter_urls_by_domain(urls, domain):
    valid_urls = []
    for url in urls:
        try:
            parsed = urlparse(url)
            # Check if the URL has a valid scheme and the desired domain
            if parsed.scheme in {"http", "https"} and parsed.netloc == domain:
                valid_urls.append(url)
        except Exception:
            continue
    return valid_urls

def extract_domain(value):
    if not isinstance(value, str):
        raise ValueError("The provided value is not a string.")
    try:
        parsed = urlparse(value)
        if parsed.scheme in {"http", "https"} and parsed.netloc:
            # Remove "www." prefix if it exists
            domain = parsed.netloc
            if domain.startswith("www."):
                domain = domain[4:]
            return domain
        else:
            raise ValueError("The provided string is not a valid URL.")
    except Exception as e:
        raise ValueError(f"Error processing the value: {e}")

web_articles = 'https://paulgraham.com/articles.html'
app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

scrape_result = app.scrape_url(
    web_articles, 
    params={
        'formats': ['links']
    }
)

# Metadata irrelevant
links = [item for item in scrape_result['links'] if isinstance(item, str)]
valid_urls = filter_urls_by_domain(links, extract_domain(web_articles))
valid_urls = valid_urls[:5]

for url in valid_urls:
    result = app.scrape_url(url, params={'formats': ['html']})
    title = result['metadata']['title']

    html_content = BeautifulSoup(result['html'], 'html.parser')

    # Replace <br> and </p> tags with newlines
    for br in html_content.find_all('br'):
        br.replace_with('\n')
    for p in html_content.find_all('p'):
        p.append('\n')

    plain_text = html_content.get_text()

    # Remove excessive whitespace (more than 2 newlines)
    plain_text = re.sub(r'\n{3,}', '\n\n', plain_text)

    # Strip whitespace from beginning and end of text
    plain_text = plain_text.strip()
    
    with open(f'{title}.txt', 'w', encoding='utf-8') as f:
        f.write(f"TITLE: {title}\n")
        f.write(plain_text)    
