FROM python:3.8-slim
ARG port

USER root
COPY . /my-app
WORKDIR /my-app

ENV PORT=$port

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /my-app \
    && chmod -R g=u /my-app \
    && pip install pip --upgrade \
    && pip install -r requirements.txt &&  apt-get install ffmpeg libsm6 libxext6  -y   
EXPOSE $PORT

CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload && python bot.py