import discord
import os

class WenardClient(discord.Client):
    async def on_message(self, message: discord.Message):
        channel = self.channel_for_response(message)
        if channel is None:
            return
        await channel.send("You called?")

    def channel_for_response(self, message: discord.Message):
        if message.author == self.user:
            return None
        if not any(user == self.user for user in message.mentions):
            return None
        if not isinstance(message.channel, discord.TextChannel):
            return None
        return message.channel

def main():
    discord_token = os.environ['WENARD_TOKEN']
    if discord_token is None:
        raise KeyError('Environment variable WENARD_TOKEN not found. This must be set to a valid Discord bot token.')

    intents = discord.Intents.default()
    intents.messages = True
    client = WenardClient(intents=intents)
    client.run(discord_token)

if __name__ == '__main__':
    main()
