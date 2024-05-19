import discord
import time
import hackernews

class WenardClient(discord.Client):
    async def on_message(self, message: discord.Message):
        channel = self.channel_for_response(message)
        if channel is None:
            return
        stories = [f'- [{story.title}]({story.url})' for story in hackernews.top_stories()]
        response = '\n'.join(stories)
        if len(response) > 2000:
            response = response[:2000]
        await channel.send(response)

    def channel_for_response(self, message: discord.Message):
        if message.author == self.user:
            return None
        if not any(user == self.user for user in message.mentions):
            return None
        if not isinstance(message.channel, discord.TextChannel):
            return None
        return message.channel

def run_wenard(discord_token: str):
    intents = discord.Intents.default()
    intents.messages = True
    client = WenardClient(intents=intents)
    client.run(discord_token)
