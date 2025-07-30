import requests
from bs4 import BeautifulSoup

resp = requests.get('https://msu.ru/divisions/rektorat/rector')
print(resp.text)