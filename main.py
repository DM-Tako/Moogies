import discord
import os
import requests

from discord.ext import commands

from Commands import rolldice_command
from Commands import info_command
from Commands import dnd_command
from Commands import meme_generator
from Commands import foass_command
from Commands import combat_command
from Utilities import nameMapper

# Variable declaration
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  
# Look into group after
#@bot.group()
#async def players(ctx):
#  if ctx.invoked_subclass is None:
#    ctx.send('```404 Command Not Found, Find Halps through $help```')
#    return

@bot.command()
async def info(ctx):
    await ctx.send(info_command.return_command())
    return

@bot.command()
async def meme(ctx, command, arg=''):
  if(command == 'cheer'):
    embed = discord.Embed()
    embed.set_image(url=meme_generator.return_cheer())
  if(command == 'hello'):
    embed = discord.Embed()
    embed.set_image(url=meme_generator.return_hello())
  if(command == 'brain'):
    embed = discord.Embed()
    embed.set_image(url=meme_generator.return_brain())
  if(command == 'nope'):
    embed = discord.Embed()
    embed.set_image(url=meme_generator.return_nope())

  await ctx.send(nameMapper.mentionViaPersonalName(arg) + " " + command)
  await ctx.send(embed=embed)
  return

@bot.command()
async def dnd(ctx, command, category="", arg=""):
  if(command == 'list'):
    await ctx.send(dnd_command.get_Category_List())
  elif(command == 'search'):
    await ctx.send(dnd_command.search_dnd_api(category, arg, ctx.author.display_name))
  else:
    await ctx.send("```Dont pop my single brain cell, cant find such command! use $info to summon the sacred tome```")
  return

@bot.command()
async def roll(ctx, arg):
  await ctx.send(rolldice_command.return_diceRoll(arg, ctx.message.author.name))
  return

message_id = ''
combatantList = {}
waitThread=False

@bot.command()
async def fight(ctx, *args):
  if('stop' in args):
        return

  fight_emoji = '⚔️'
  death_emoji = '⚰️'
  fight_prefix = "```diff\n***Cues Intense Bard Music***\n\tFight Begins```"
  

  if len(args) == 0:
  #if args == '':
    message = await ctx.send(fight_prefix)
    
    global message_id
    

    message_id = message.id
    await message.add_reaction(fight_emoji)
    await message.add_reaction(death_emoji)
  else:
    message = await ctx.fetch_message(message_id)

    global combatantList
    

    if 'dead' in args:
      command,name = args
      del combatantList[name]   
    else:        
      combatantList = (combat_command.retrieve_players_info(combatantList, args))

    message.content = fight_prefix[:-3] + "\n\t" + combat_command.print_combatantList(combatantList) + '```'
    await message.edit(content=message.content)
    await ctx.message.delete(delay = 5)

  def check(reaction, user):
      return user == ctx.author and str(
          reaction.emoji) in [fight_emoji, death_emoji]


  while True:
    reaction, user = await bot.wait_for("reaction_add", check=check)
    
    
    if str(reaction.emoji) == fight_emoji:
      message.remove_reaction
      print("combatlist before: " + combat_command.print_combatantList(combatantList))

      firstChar = list(combatantList.keys())[0]
      print("first Char is : " + firstChar)
      combatantList[firstChar] = combatantList.pop(firstChar)

      print("sword icon combat list: " + combat_command.print_combatantList(combatantList))
      
      message.content = fight_prefix[:-3] + "\n\t" + combat_command.print_combatantList(combatantList) + '```'
      await message.edit(content=message.content)

     

  
        

## Error Handler for fight
@fight.error
async def fight_error(ctx: commands.Context , error: commands.CommandError):
  if isinstance(error, commands.CommandInvokeError):
    print(str(error))
    await ctx.send("```Error in format. Please use e.g [$fight Name 1d10+3]```", delete_after = 5)
    await ctx.message.delete(delay = 5)
  else:
    await ctx.send("```Uncatched Error(fight): Please notify admin```")


@bot.event
async def on_message(message):
  # Prevent bot from replying itself
  if message.author == bot.user:
    return

  if "Moogie".casefold() in message.content.casefold():
    await message.channel.send(foass_command.foass_praise(nameMapper.mentionViaId(message.author.id,'yes')))

  await bot.process_commands(message)
          
# Retrieve token of application
try:
  bot.run(os.getenv('TOKEN'))
except discord.HTTPException:
  r = requests.head(url="https://discord.com/api/v9")
  
  print(f"Rate limit {int(r.headers['Retry-After'])/60} minute left")



