import lxml
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
html = requests.get(url).content
soup = BeautifulSoup(html, "lxml")
links = set(soup.find_all(name="a", href=True))

domain = url.split("//www.")[-1].split("/")[0]
sub_urls = []
for link in links:
    sub_url = link["href"]
    sub_urls.append(sub_url)
    page_name = link.string

for link in sub_urls:
    # print(link)
    # if domain in link:
    #     # print(domain)
    try:
        response = requests.get(link)
        print(response.ok)
    except:
        pass
