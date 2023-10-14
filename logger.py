from loguru import logger


def log(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Запускается => {func.__doc__.strip()}')
        result = func(*args, **kwargs)
        logger.info(f'Успешно отработала => {func.__doc__.strip()}')
        return result
    return wrapper

