from constants.city import CITY_NAME
from constants.text import Text


def create_text_for_input() -> str:
    city = [f'{index}. {city}\n' for index, city in enumerate(CITY_NAME.values(), 1)]
    text = f'{Text.INPUT_CITY.value}{"".join(city)}\n==> '
    return text
