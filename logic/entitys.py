from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from logic.mixins import RequestMixin
from services.logger import log


@dataclass
class Item(RequestMixin):
    id: str = field(init=False)
    url: str
    name: str = field(init=False)
    current_price: str
    price: str
    brand: str = field(init=False)
    soup: BeautifulSoup = field(init=False)

    def __post_init__(self) -> None:
        self.soup = self.build_soup(self.url)
        self.id = self.set_id()
        self.name = self.set_name()
        self.brand = self.set_brand()

    def set_id(self) -> str:
        item_id = self.soup.find('p', attrs={'itemprop': 'productID', 'class': 'product-page-content__article'}).text
        return item_id.split()[-1]

    def set_name(self) -> str:
        item_name = self.soup.find('h1').find('span').text.strip()
        return item_name

    def set_brand(self) -> str:
        item_brand = (
            self.soup.find('ul', class_='product-attributes__list style--product-page-short-list')
            .find('li')
            .find('a')
            .text
        )
        return item_brand.strip()

    @log
    def get_description(self) -> dict[str]:
        """
        Функция получения описании товара

        """
        return dict(
            {
                'id': self.id,
                'name': self.name,
                'link': self.url,
                'current_price': self.current_price,
                'price': self.price,
                'brand': self.brand,
            }
        )
