import requests
from bs4 import BeautifulSoup
import re


class Page:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)

    def get_html(self):
        return BeautifulSoup(self.page.text, 'html.parser')

    def get_headers(self):
        return self.page.headers
