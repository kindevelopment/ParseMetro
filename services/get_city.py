from constants.city import CITY_ID, CITY_NAME


def get_city_id(city_id: int) -> int:
    return CITY_ID.get(city_id)


def get_city_name(city_id: int) -> int:
    return CITY_NAME.get(city_id)
