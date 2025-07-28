import requests
from bs4 import beautifulsoap

resp = requests.get('https://msu.ru/divisions/rektorat/rector')
print(resp.text)