# busbot
Ahoy sailors...


## Setup
1. Install Python >= 3.6
2. Install pipenv `python3 -m pip install pipenv`
3. Clone the repo `git clone git@github.com:behr-davide/busbot.git`
4. Install dependencies `cd busbot && python3 -m pipenv install`
5. Create a file called .env and add the discord token for the bot:
```
DISCORD_TOKEN=<my_discord_token>
```
## Running

- Local
    1. `cd busbot && python3 -m pipenv run bot.py`
- Docker
    - The following commands will build the busbot image from the `Dockerfile` and run a detached the bot script in a detached container.
      1. `docker build -t busbot:latest .`
      2. `docker run -d --name busbot --env-file .env --restart unless-stopped busbot:latest`
    - The base image in the `Dockerfile` is for the arm32v7 architecture to support running busbot on a Raspberry Pi 3 B+.  
