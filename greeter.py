
import discord
import asyncio
from discord.utils import find

client=discord.Client()

@client.event
async def on_guild_join(guild):
    allowedID = [536447514447183892]
    if guild.id not in allowedID:
        await guild.leave()

@client.event
async def on_member_join(member):
    guild = member.guild
    greeting = """Please welcome {0.mention} to {1.name}!
I've DM'd you the help commands for the bots on server. Please introduce yourself and make yourself at home.
""".format(member,guild)
    dm = """To get help with the bots:
~Help OwO
~Help CWC
~Help Dice
~Help Fortune
~Help 8ball
~Help Weather
https://discord.gg/XSguZkH
"""
    
    x = guild.channels
    y = False
    
    for i in x:
        if i.permissions_for(guild.me).send_messages and not y:
            x = i
            break
    
    rolez = ""
    
    for i in guild.roles:
        if i.name == "New Friends":
            rolez = i
            break
    
    await member.send(dm)
    await x.send(greeting) 
    await member.add_roles(rolez)

                
client.run('NTkxOTI4Nzg4MTYyNTc2NDE2.XQ39SA.Tm9A3cQ_mG0qCERGM6qRBtS6y1I') 

