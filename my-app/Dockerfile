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
    && pip install -r requirements.txt
EXPOSE $PORT

CMD python bot.py