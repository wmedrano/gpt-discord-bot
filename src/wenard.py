import discord
import time
import os
import requests
import hackernews

from llm import Llm

class WenardClient(discord.Client):
    async def on_message(self, message: discord.Message):
        channel = self.channel_for_response(message)
        if channel is None:
            return
        llm = Llm()
        stories = llm.filter_relevant_elements(
            message.content.replace(self.user.mention, ''),
            hackernews.top_stories(),
            lambda s: s.title
        )
        text_response = 'No relevant posts found on HackerNews.'
        if len(stories) > 0:
            text_response = '\n'.join(
            ['# HackerNews Posts'] + [
                f'- [{story.title}]({story.url})'
                for story in stories
            ])
        await channel.send(text_response, suppress_embeds=True)

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
