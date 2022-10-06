# youtybe-audioclip

Телеграм бот для получения аудиодорожек 
из музыкальных клипов с ютюб

Перед запуском проекта необходимо создать копию файла 
.env_example, назвав его .env и установить значение токена бота

запустить бота локально 
python run_bot.py

Запуск в docker:

Необходимо собрать образ

docker build -t <image_name> .

Запустить контейнер

docker run --env TELEGRAM_TOKEN=<telegram_token> --name <container_name> -t <image_name>

