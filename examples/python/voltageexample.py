import voltage
from voltage.ext import commands
import random
import requests
import json

client = commands.CommandsClient(">")

@client.command(description="Ask the IdiotAI Chatbot things. Example: ++askidiotai hi")
async def askidiotai(ctx, question):
    url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    embed = voltage.SendableEmbed(title=f"IdiotAI API", description=f"Question: {question}\nResponse: {response.text}", color="#FF009F")
    await ctx.send(embed=embed)



client.run("BOTTOKENHERE")
