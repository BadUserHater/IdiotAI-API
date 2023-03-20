import discord
from discord.ext import commands
import requests
import random
import json

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=">", intents=intents)
client.remove_command("help")

@client.command()
async def askidiotai(ctx, question):
    url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    embed = discord.Embed(title=f"IdiotAI API", description=f"Question: {question}\nResponse: {response.text}", color=(16711839))
    await ctx.send(embed=embed)



client.run("BOTTOKENHERE")
