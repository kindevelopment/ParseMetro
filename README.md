Alimov Said

# Parse Metro

Данная сборка представляет собой, парсер для сбора информации с карточек категории "Вода" сайта (https://online.metro-cc.ru/)

## Старт
```
git clone https://github.com/kindevelopment/ParseMetro.git
```
## Запуск парсера
1) Инициализируем виртуальное окружение:
```
poetry install
```
2) Запускаем проект коммандой:
```
poetry run python -m logic.parser
```
3) Перед коммитом в свой репозиторий, запустите прекоммит командной:
```
pre-commit install
```
## Используемы инструменты
- python - 3.11
- requests
- bs4
- loguru
- blake

