import discord
import os

class WenardClient(discord.Client):
    async def on_ready(self):
        pass

    async def ono_message(self, message):
        pass

def main():
    discord_token = os.environ['WENARD_TOKEN']
    if discord_token is None:
        raise KeyError('Environment variable WENARD_TOKEN not found. This must be set to a valid Discord bot token.')

    intents = discord.Intents.default()
    client = WenardClient(intents=intents)
    client.run(discord_token)

if __name__ == '__main__':
    main()
