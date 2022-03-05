import os
import requests

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

api_url = 'https://ai.iamtakagi.net/api/make_sentence'


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    activity = discord.Game(name="https://twitter.com/iamtakagi_ai")
    await bot.change_presence(activity=activity)


@slash.slash(name='takagi', description='高木が喋ります')
async def on_command(ctx: SlashContext):
    if not ctx.guild:
        return await ctx.send(
            content="このコマンドは DM で使用できません。",
            hidden=True
        )
    sentence = requests.get(
        api_url, headers={"content-type": "application/json"}).json()['sentence']
    await ctx.send(
        content=sentence, 
        hidden=True
    )

bot.run(TOKEN)
