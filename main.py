import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
outdoors_list = []
indoors_list = []
msg = input("")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):  
  if message.author == client.user:
    return
  
  if message.content.startswith('-shit help'):
    await message.channel.send('Prefix [-shit] + [location]: outdoors, indoors + [option]: add, remove, roulette')

  if message.content.startswith('-shit outdoors add', msg):
    outdoors_list.append(msg)
    await message.channel.send(outdoors_list) 

  if message.content.startswith('-shit outdoors roulette'):
    await message.channel.send(random.choice(outdoors_list))
  
keep_alive()  
client.run(os.environ['bot'])

