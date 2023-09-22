import guilded
from guilded.ext import commands
import random
import requests
import json

client = guilded.Client()
client = commands.Bot(user_id='BOTIDHERE', command_prefix='++')
client.remove_command("help")

@client.command()
async def askidiotai(ctx, question):
    url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    embed = guilded.Embed(title=f"IdiotAI API", description=f"Question: {question}\nResponse: {response.text}", color=(16711839))
    await ctx.send(embed=embed)





auth_token="BOTTOKENHERE"
client.run(auth_token)
