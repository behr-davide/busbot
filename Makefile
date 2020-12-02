clean:
	docker stop busbot && docker container rm busbot

build:
	docker build -t busbot:latest .

deploy:
        docker run -d --name busbot --env-file .env --restart unless-stopped busbot:latest

all: clean build deploy
