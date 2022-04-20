import discord 
import os 
from discord.ext import commands
import os.path
import random

# Information for version number, author etc etc.
# makes a neat little embed.

class infor(commands.Cog):
  def __init__(self, client):
    self.client = client 
    
  @commands.command()
  async def information(self, ctx):

      images = ['https://cdn.discordapp.com/attachments/760119885996097560/966368715690102904/68747470733a2f2f-7066326d2e636f6d_3.png', 'https://media.discordapp.net/attachments/760119885996097560/965703666986254426/68747470733a2f2f-7066326d2e636f6d_51.png?width=243&height=243', 'https://images-ext-2.discordapp.net/external/Fy9OnrysSzNObggNBWUR33ptU3XIuoZTWVi79CkXHAI/%3Fwidth%3D243%26height%3D243/https/media.discordapp.net/attachments/760119885996097560/965926443953557504/68747470733a2f2f-7066326d2e636f6d_48-u4nix_2qw-transformed_1_1.png?width=219&height=219', 'https://images-ext-2.discordapp.net/external/37-VZqUYYvbfI-QQUNuy6p49x-uP6Ed5FQ1yRFc_jZk/%3Fwidth%3D219%26height%3D219/https/images-ext-2.discordapp.net/external/C7umYLpkBw6I8ICAimwLMdnzhxdqt7-WDfH2O6BIkFU/%253Fwidth%253D243%2526height%253D243/https/media.discordapp.net/attachments/800680039272284200/966048898089091143/68747470733a2f2f-7066326d2e636f6d_53.png?width=197&height=197', 'https://media.discordapp.net/attachments/760119885996097560/965932133719891968/68747470733a2f2f-7066326d2e636f6d_52.png?width=243&height=243']    
      rando = random.choice(images)

    
      embed_info = discord.Embed(title='Information.', description='MiiBot is a powerful discord bot built for using Mii-related functions, such as pulling Mii data, images, QR codes and more. Not affilated with Nintendo in anyway shape or form, this is just a passion project.')
      embed_info.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      embed_info.add_field(name='Author.', value='The bot was created by AbdyyEee.')
      embed_info.add_field(name='Credits.', value='Mrpirate02, for extra code help \nhttps://pf2m.com/tools/mii/ for the Mii renders you see.')
      embed_info.add_field(name='Current stable version.', value='1.0', inline=False)
      embed_info.add_field(name='Technical Details', value='This bot is built with python, and the Discord.py library. \nThe code isnt that good, so dont use it.', inline=False)

      

      embed_info.set_thumbnail(url=rando)
      
    
      await ctx.send(embed=embed_info) 


def setup(client):
    client.add_cog(infor(client))
    