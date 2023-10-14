from fake_useragent import UserAgent
from loguru import logger


class Config:
    ua = UserAgent()
    logger.debug('Инициализация проекта')
    logger.add(
        '../debug-logg/debug.log', format='{time} - {message}', rotation='1 day', compression='zip', level='INFO'
    )


conf = Config()
