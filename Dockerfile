FROM arm32v7/python:3.8-alpine

RUN apk add build-base libffi-dev tzdata && pip install pipenv 
COPY . /app
WORKDIR /app
ENV TZ=America/New_York
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "bot.py" ]
