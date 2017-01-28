# Encyclopedia

Данный скрипт генерирует из markdown-файлов статей энциклопедии [DEVMAN](https://devman.org) статический сайт.
Структура сайта задаётся конфигурационым файлом в формате json. Конфиг является обязательным параметром для скрипта.
Пример сайта [тут](https://veean.github.io).

## Установка скрипта и зависимостей
    
    git clone https://github.com/veean/19_site_generator.git
    cd 19_site_generator
    pip install -r requirements.txt
    
## Запуск скрипта 

    $python site_generator.py config.json
    
    Static site generating successfully completed!

По умолчанию скрипт будет генерировать html файлы из  markdown файлов из папки `articles/` и складывать их в папку `site/articles`.
Структура папки описывается в файле config.json. 

Для добавления новых файлов .md для генерации страниц сайта, необходимо также модифицировать файл конфигурации (config.json).

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
