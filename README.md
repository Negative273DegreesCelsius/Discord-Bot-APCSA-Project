# Discord-Bot-APCSA-Project
This is a program made for a class project. It is heavily inspired by [Geoguessr](https://www.geoguessr.com/) and uses the [Shutterstock API](https://www.shutterstock.com/developers) to generate static street view images.

## Libraries Used:
This project uses [Discord.py](https://github.com/Rapptz/discord.py) to communicate with Discord's API. 

## What Does this Bot do?
This bot tests users on their knowledge of European geography. Users are sent multiple images of a European capital and have to guess the name of the capital city or the country

## Setup
Currently, there is no way to invite this bot to your servers. You are, however, free to copy the code and host it locally.

### Required packages
[Discord.py](https://github.com/Rapptz/discord.py):

> pip install discord.py

[Shutterstock CLI API](https://www.shutterstock.com/developers/documentation/cli):

> pip install shutterstock-cli

### Create an application
Create a Discord application in the [Discord Developer Portal](https://discord.com/developers/docs), then create a bot.

Create a Shutterstock Application [here](https://www.shutterstock.com/api/pricing?utm_source=shutterstock&utm_medium=banner&utm_campaign=developer.portal). Choose a pricing plan and log in.

### Set up environment variables for Shutterstock
The Shutterstock CLI API requires that you set your Shutterstock client's key, secret, and API token. You can find the instructions in the [CLI Documentation](https://discord.com/developers/docs)

### Config file
In the same directory as the ``ExampleConfig.json`` file, create a ``Config.json`` file and copy the contents in the example config into the new ``Config.json`` file. Replace the angle brackets with your Discord bot token in the ``token`` key. Replace the angle brackets in the list in the ``authors`` key with your username(s)