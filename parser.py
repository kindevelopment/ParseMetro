import re
import time
from dataclasses import dataclass
from typing import List
import json
from entitys import Item
from logger import log
from mixins import RequestMixin


@dataclass
class ParseMetro(RequestMixin):
    url: str

    @log
    def get_amount_pages(self) -> int:
        """
        Функция получения кол-ва страниц в категории

        """
        soup = self.build_soup()
        return int(soup.find('nav', attrs={'role': 'navigation', 'class': 'subcategory-or-type__pagination'}).find('ul').find_all('li')[-2].text)

    @log
    def get_all_items_in_category(self) -> List[dict[str]]:
        """
        Функция получения всех объектов в категории.

        """
        amount_pages = self.get_amount_pages()
        items_link = list()
        for num_page in range(1, amount_pages+1):
            soup = self.build_soup(f'{self.url}&page={num_page}')
            items_to_page = soup.find('div', id='products-inner').find_all('div', class_='catalog-2-level-product-card product-card subcategory-or-type__products-item catalog--common offline-prices-sorting--best-level with-prices-drop')
            for item in items_to_page:
                price_info = item.find('div', class_='product-card-prices__content-prices')
                current_price = ''.join([span.text for span in price_info.find(
                    class_='product-card-prices__actual'
                ).find(class_='product-price__sum').find_all('span') if not span.text.isalpha()])
                if price := price_info.find(class_='product-card-prices__old'):
                    price = price.find(class_='product-price__sum-rubles').text
                else:
                    price = current_price
                option_item = {
                    'url': item.find('div', class_='product-card__top').find('a', attrs={'data-qa': 'product-card-name'}).get('href'),
                    'price': price,
                    'current_price': current_price
                }
                items_link.append(option_item)
        return items_link

    @staticmethod
    def record_json(items: List[dict[str]]) -> bool:
        """
        Функция - записи в файл.

        """
        current_time = time.time()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))
        with open(f'parse-data/data - {current_time}.json', "w", encoding="utf-8") as file:
            json.dump(items, file, indent=4, ensure_ascii=False)
            return True

    @log
    def parse(self) -> None:
        """
        Функция - контроллер парсера.

        """
        items = self.get_all_items_in_category()
        main_link = re.search(r'https?://([^/]+)', self.url).group(0)
        items = [
            Item(
                url=main_link + item.get('url'),
                current_price=item.get('current_price'),
                price=item.get('price')
            ).get_description() for item in items
        ]
        self.record_json(items)


parse_water = ParseMetro(url='https://online.metro-cc.ru/category/bezalkogolnye-napitki/pityevaya-voda-kulery?from=under_search&in_stock=1')
parse_water.parse()
