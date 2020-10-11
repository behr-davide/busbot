FROM arm32v7/python:3.8-alpine

RUN apk add build-base libffi-dev && pip install pipenv 
COPY . /app
WORKDIR /app
RUN pipenv install --deploy --ignore-pipfile

ENTRYPOINT [ "pipenv", "run", "python", "bot.py" ]
