# Create a Discord Bot with us!

## Table of Contents
- [Prerequisite - Create your own Discord server](#prereq)
- [Step 1 - What is a Discord Bot and what can it do?](#step-1)
- [Step 2 - Setup Discord Developer Portal and Bot](#step-2)
- [Step 3 - Setup Discord Bot permissions](#step-3)
- [Step 4 - Inviting the Bot to your server](#step-4)
- [Step 5 - Setup Bot code environment ( PYTHON )](#step-5)
- [Step 6 - Setup Bot source code ( PYTHON )](#step-6)
- [Step 7 - Coding bot commands ( PYTHON )](#step-7)


<a id="prereq"></a>
## Prerequisite - Create your own Discord server
- Useful as a 'development environment'
- Gives you a lil playground
- Ensures you do not embarrass yourself with bad code on a production server
![image](https://github.com/user-attachments/assets/c05a2273-6df1-474d-9fdc-6e65d8e9b73c)


<a id="step-1"></a>
## Step 1 - What is a Discord Bot and what can it do?

- Non-human 'users' that can be programmed to perform many different tasks on a Discord server
- Read messages posted to channels
- Send messages to channels and direct message users
- React to messages
- Pull data from APIs
- Scrape data from websites
- So much more

We are going to make a BASIC bot that can read when a user sends message `!doug` and then send back `give me your kidneys`

<a id="step-2"></a>
## Step 2 - Setup Discord Developer Portal and Bot

- Go to: https://discord.com/build and get started

![image](https://github.com/user-attachments/assets/8d49043f-f942-4ec9-88b3-a62a178952e4)

![image](https://github.com/user-attachments/assets/13cde976-d695-4948-8f92-d4311e8c93d7)

- You will be prompted for a name of the bot. Be creative!

![image](https://github.com/user-attachments/assets/5dcbf1d0-f8d9-4fbd-8fd6-b90508f904e4)


<a id="step-3"></a>
## Step 3 - Setup Discord Bot permissions

- Check only `bot` !
![image](https://github.com/user-attachments/assets/021ce76a-ab52-4f1e-afe6-d9f85f4d0472)

- Specify your bot's permissions. We're only going to be reading messages, sending messages, and possibly reacting to messages too.
![image](https://github.com/user-attachments/assets/005e81de-d645-4260-8430-6db125b050a3)


<a id="step-4"></a>
### Step 4 - Add/Invite Discord bot to server
- YOU MUST HAVE PERMISSION TO ADD BOTS A SERVER
- Once added, you will notice that your bot is "offline" 😏

![image](https://github.com/user-attachments/assets/c77a4e05-6372-44bd-9f38-88eb3c849995)

<a id="step-5"></a>
### Step 5 - Bot source code environment setup ( PYTHON )

- Create a folder for your bot's source code.
- We will setup an environment file `.env` to hold our token ( we will get this in a second )

##### Python3  Virtual Env setup ( Recommended )
- This will help manage our dependencies

```bash
# Make sure you are in a folder you want and create a "virtual environment" in `venv` folder
python3 -m venv venv

# 'source' the activate script
source venv/bin/activate
```

##### Install dependencies

- `discord` is the package we use to interact with Discord
- `python-dotenv` is used to keep our secret tokens SECRET
- `audioop-lts` is required for `discord` package to work idk why

```bash
python3 -m pip install discord python-dotenv audioop-lts
```

##### Create a `.env` file

- `.env` will keep your Discord bot token secret!!!!

```log
# .env file
DISCORD_BOT_TOKEN="see next step to get your bot token so you put it here"
```

##### Get your bot token and save in your `.env`
![image](https://github.com/user-attachments/assets/6da403e3-7eca-4b9f-ad4b-76d805054417)
![image](https://github.com/user-attachments/assets/98ebab8d-c15e-4d47-bb60-c88565cddbe8)

<a id="step-6"></a>
### Step 6 - Bot source code prep ( PYTHON )

- Create your bot script file `bot.py`
```python
# bot.py
from dotenv import load_dotenv
import os
import discord

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is online!')

client.run(TOKEN)
```

Run this script `python3 boy.py` and see if your bot is online!

<a id="step-7"></a>
### Step 7 - Coding Bot commands

- When making changes to your Python script, you will have to stop + restart your script to test changes.

```python
# ...

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!doug'):
        # add a reaction? yes.
        await message.add_reaction('👀')

        # send a message back to channel
        await message.channel.send('give me your kidneys')

# ...
```




## Bonus
> Check out my video with a creator of a rather complex Discord bot that creates 'pick up' games for Unreal Tournament 1999
[![image](https://github.com/user-attachments/assets/cfcf4a18-5023-4826-81df-4bfc03951826)](https://www.youtube.com/live/RbAl-UB_bX4)


