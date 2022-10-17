FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt -y install ffmpeg

ENV TELEGRAM_TOKEN bot_token

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./app/ /app

CMD ["python3", "run_bot.py"]
