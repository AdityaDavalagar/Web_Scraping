import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup1
import bs4
# import urllib.request, urllib.parse, urllib.error 
def make_soup(url):
	thepage = urlopen(url)
	soupdata = soup1(thepage,'html.parser')
	return soupdata

i=1
soup = make_soup("https://uwaterloo.ca")
for img in soup.findAll('img'):
	temp = img.get('src')
	if temp[:1]=="/":
		image = "https://uwaterloo.ca" + temp
	else:
		image = temp
	print(image)
	nametemp = img.get('alt')
	if len(nametemp)==0:
		filename = str(i)
		i=i+1
	else:
		filename = nametemp
	imagefile = open(filename + ".jpeg",'wb')
	imagefile.write(urlopen(image).read())
	imagefile.close()