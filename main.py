from colorama import Fore
import asyncio
import random

import time

import discord
from discord.ext import commands
from datetime import timedelta

########### Selfbot Setup
bot = commands.Bot(command_prefix='PREFIX',
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

########## Selfbot Cmds
@bot.command(pass_context=True) 
async def tfollow(ctx, *, user):
  followers = 0
  channel_1 = bot.get_channel('BOTTING CHANNEL ID 1')
  channel_2 = bot.get_channel('BOTTING CHANNEL ID 2')

 
  times = "{:0>8}".format(str(timedelta(seconds=120)))

  await ctx.send(f'''
  Sending Followers to {user}..
  
  **DETAILS**
  > Amount Sent: 50
  > Estimated Time (Everytime after use): {times}
  > Servers being sent to: 2''')
  
  for i in range(0, 50):
    await channel1.send(f'/tfollow {user}')
    await channel2.send(f'/tfollow {user}')
    await asyncio.sleep(130)



    print(f'Followed: {user} | Followers: {followers}')
    
    
# Logging In
bot.run('TOKEN', bot=False)
