import discord
import os
from keep_alive import keep_alive 
from discord.ext import commands

clients = commands.Bot(command_prefix='.')

@clients.event
async def on_ready():
  print("We are logged in as {0.user}".format(clients))

@clients.command()
async def kick(ctx, member: discord.Member,*, reason=None):
  await member.kick(reason=reason)

@clients.command()
async def ban(ctx, member: discord.Member,*, reason=None):
  print("banning")
  await member.ban(reason=reason)
  await ctx.send("***The following user has been banned \n • "+"@"+str(member)+"***") 



@clients.command() 
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user) 
      await ctx.send("***The following user has been unbanned \n • "+"@"+member+"***") 
      return

keep_alive()

my_secret = os.environ['botkey']

clients.run(my_secret)