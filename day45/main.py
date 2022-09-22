# # import lxml
import requests
from bs4 import BeautifulSoup

with open("day45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for string_data in all_anchor_tags:
# print(string_data.string)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = [
    score.getText() for score in soup.find_all(name="span", class_="score")
]


# print(article_tag)
# print(article_texts)
# print(article_links)
print(article_upvotes)
# article_upvotes_nums = [int([raw.split(" ")][0][0]) for raw in article_upvotes]
article_upvotes_nums = [int(score.split()[0]) for score in article_upvotes]
print(article_upvotes_nums)
