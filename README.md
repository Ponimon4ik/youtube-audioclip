# youtybe-audioclip

# Телеграм бот для получения аудиодорожек из музыкальных клипов с ютюб.

### Запуск в docker:

- Cобрать образ.
```shell
docker build -t <image_name> .
```
- Запустить контейнер.
```shell
docker run --env TELEGRAM_TOKEN=<telegram_token> --name <container_name> -t <image_name>
```
