from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

urls = ['https://scholarworks.gvsu.edu/books/']

#scrape elements
for url in urls:
    uClient = urlopen(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div",{"class":"content_block"})
    source = page_soup.find("div",{"id":"series-header"})

    data = []
    for container in containers:
        item = {}
        item['type'] = "Textbook"
        item['title'] = container.h2.text
        item['author'] = container.p.text
        item['link'] = container.a["href"]
        item['source'] = source.h2.text
        data.append(item) # add the item to the list
        print(container.h2.text)

with open("C:/Users/ramky/Desktop/webscraping/multiple.json", "w") as writeJSON:
   json.dump(data, writeJSON, ensure_ascii=False)