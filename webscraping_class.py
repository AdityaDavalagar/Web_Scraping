import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
type(res)
res.text
soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(soup)
req = soup.select('.printfooter')
req
req[0]
print(req[0].getText())
