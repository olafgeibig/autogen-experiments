headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
import urllib
from bs4 import BeautifulSoup
import requests

text = 'Olaf Geibig'
text = urllib.parse.quote_plus(text)

url = 'https://google.com/search?q=' + text
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
for result in soup.select('.tF2Cxc'):
  link = result.select_one('.yuRUbf a')['href']
  print(link)
