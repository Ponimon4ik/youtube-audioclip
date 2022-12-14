# Youtube-audioclip

# Телеграм бот для получения аудиодорожек из музыкальных клипов с YouTube.
Данный бот создан для возможности получения аудиофайлов 
из интересных музыкальных клипов на YouTube. 


## Используемые технологии:

+ Python
+ Python-telegram-bot
+ Pytube
+ Moviepy


## Переменные окружения:

Перед запуском проекта необходимо создать копию файла
```.env.example```, назвав его ```.env``` и установить значение токена бота

```dotenv
TELEGRAM_TOKEN= # токен бота
```

## Запуск бота локально:

- Установить зависимости из файла requirements.txt:

```shell
python3 -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```
- Запустить бота

```shell
python app/run_bot.py
```

### Запуск в docker:

- Cобрать образ.
```shell
docker build -t <image_name> .
```
- Запустить контейнер.
```shell
docker run --env-file .env --name <container_name> -t <image_name>
```

## Команды для бота:

- ```/start```: Запустить бота и получить приветственное сообщение

```text
Привет!
Данный бот извлекает аудиодорожки из видео на ютубе.
Пришли ссылку на ютуб видео и в ответ получишь аудидорожку.
```
