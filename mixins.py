from config import conf
import requests
from bs4 import BeautifulSoup


class RequestMixin:
    def get_response(self, url: str | None = None) -> str:
        headers = {'User-Agent': conf.ua.random}
        response = requests.get(url if url else self.url, headers=headers)
        response.encoding = 'utf8'
        return response.text

    def build_soup(self, url: str | None = None) -> BeautifulSoup:
        response = self.get_response(url)
        soup = BeautifulSoup(response, 'lxml')
        return soup
