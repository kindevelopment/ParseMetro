Alimov Said

# Parse Metro

Данная сборка представляет собой, парсер для парсинга категории сайта (https://online.metro-cc.ru/)

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

## Используемы инструменты
- python - 3.11
- requests
- bs4
- loguru
- blake

