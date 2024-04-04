# Ice Breaker
<img src="./icebreaker.png" alt="icebreaker" width="200"/>

A discord bot written in Python with over 49k trivia questions and over 2,500 questions from the categories of Never Have I Ever, Would You Rather, Truth, Dare, and What Would You Do.

The trivia questions are from [OpenTriviaQA](https://github.com/uberspot/OpenTriviaQA) and converted to json using [./converter.py](https://github.com/NMedvesky/icebreaker/blob/b6e48c72b737f74b39a4fd72002f04438249ac4e/converter.py).
The other questions are from [Would You Bot - Client](https://github.com/Would-You-Bot/client).

# Getting Started

## Setting Up Environment
```sh
git clone https://github.com/NMedvesky/icebreaker.git
cd icebreaker
pip install -r ./requirements.txt
```

## Config

Set the bot token in [./src/bot.py](https://github.com/NMedvesky/icebreaker/blob/b6e48c72b737f74b39a4fd72002f04438249ac4e/src/bot.py).
It is recommended to use environment variables to store the token rather than in plain text.
Also define any discord users with permission to use the `reload` command.
```py
TOKEN: str = os.environ["ICEBREAKER_TOKEN"]
ADMIN_IDS: list[int] = []
```

## Running the Bot

In a terminal window run [./src/bot.py](https://github.com/NMedvesky/icebreaker/blob/b6e48c72b737f74b39a4fd72002f04438249ac4e/src/bot.py) while in the main project directory.
```sh
python ./src/bot.py
```

After running it should output something like this.
```
2024-04-04 13:26:43 INFO     discord.client logging in using static token
18:26:44 UTC Loaded question_commands Extension
18:26:44 UTC Loaded trivia_commands Extension
2024-04-04 13:26:44 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: 909291be5319c3767bcfd81d26c00d58).
18:26:47 UTC Logged in as IceBreaker
18:26:47 UTC Bot ID 1223740925176451093
18:26:47 UTC Discord Version 2.3.2
18:26:47 UTC Python Version 3.9.12
18:26:48 UTC Tree Commands Synced 5 Commands
18:26:48 UTC Bot Online
```

## Debug Commands

`ping`
Checks the bot's latency in ms.

`uptime`
Returns the uptime of the bot.

`reload [extension]`
Reloads the selected extension. Requires user id to be in `ADMIN_IDS` list to call this command.

