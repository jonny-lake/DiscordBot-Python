import sys
import discord
import os
from baddieFunctions import machineLearnMeanWords as mlmw

client = discord.Client()

def removeprefix(self: str, prefix: str, /) -> str:
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]

def setBaddie(message):
    baddieUserName = removeprefix(message.content, "-setBad ")
    var = discord.utils.get(message.guild.roles, name = "Baddie")
    member = discord.utils.get(message.guild.members, user = baddieUserName)
    message.guild.members.member.add_role(var)
    return baddieUserName

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # assigns admin role to a variable if the message author is an admin
    admin = discord.utils.find(lambda r: r.name == 'Admin', message.author.roles)
    # assigns baddie role to a variable if the message author is on bad behavior
    baddie = discord.utils.find(lambda r: r.name == 'Baddie', message.author.roles)

    if(baddie in message.author.roles):
        insult = mlmw.machineLearnMeanWords()
        await message.channel.send(insult)

    elif ((message.content.startswith('-setBad') and (admin in message.author.roles))):
        badBoy = setBaddie(message)
        await message.channel.send('{} has been on bad behavior.'.format(badBoy))

    elif((message.content.startswith('-setBad') and not (admin in message.author.roles) and not (baddie in message.author.roles))):
        await message.channel.send('You are not an admin!')

client.run('OTE1MTI5NDMwODgyNTM3NDcy.YaXGsg.UuN4Spe8eBQe2nzUVrNOX6Rbh5c')