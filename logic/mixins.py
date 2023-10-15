import requests
from bs4 import BeautifulSoup
from config.config import conf


class RequestMixin:
    def get_response(self, url: str | None = None) -> str:
        headers = {'User-Agent': conf.ua.random}
        cookies = {'metroStoreId': str(self.city_id)}
        response = requests.get(url if url else self.url, headers=headers, cookies=cookies)
        response.encoding = 'utf8'
        return response.text

    def build_soup(self, url: str | None = None) -> BeautifulSoup:
        response = self.get_response(url)
        soup = BeautifulSoup(response, 'lxml')
        return soup
