import discord 
import os 
from discord.ext import commands
import os.path
import random

class help(commands.Cog):
  def __init__(self, client):
    self.client = client 

  @commands.command()
  async def helpmii(self, ctx):
    # Random thumbnail
    images = ['https://cdn.discordapp.com/attachments/760119885996097560/966368715690102904/68747470733a2f2f-7066326d2e636f6d_3.png', 'https://media.discordapp.net/attachments/760119885996097560/965703666986254426/68747470733a2f2f-7066326d2e636f6d_51.png?width=243&height=243', 'https://images-ext-2.discordapp.net/external/Fy9OnrysSzNObggNBWUR33ptU3XIuoZTWVi79CkXHAI/%3Fwidth%3D243%26height%3D243/https/media.discordapp.net/attachments/760119885996097560/965926443953557504/68747470733a2f2f-7066326d2e636f6d_48-u4nix_2qw-transformed_1_1.png?width=219&height=219', 'https://images-ext-2.discordapp.net/external/37-VZqUYYvbfI-QQUNuy6p49x-uP6Ed5FQ1yRFc_jZk/%3Fwidth%3D219%26height%3D219/https/images-ext-2.discordapp.net/external/C7umYLpkBw6I8ICAimwLMdnzhxdqt7-WDfH2O6BIkFU/%253Fwidth%253D243%2526height%253D243/https/media.discordapp.net/attachments/800680039272284200/966048898089091143/68747470733a2f2f-7066326d2e636f6d_53.png?width=197&height=197', 'https://media.discordapp.net/attachments/760119885996097560/965932133719891968/68747470733a2f2f-7066326d2e636f6d_52.png?width=243&height=243']    
    rando = random.choice(images)
  
    embed_help = discord.Embed(title='Mii bot help menu', description='All commands are listed below.')
    embed_help.add_field(name='Mii Commands', value='`!information` \nShows information on the bot. \n\n`!mii_name ` \nRetrives information from the Mii server, with instructions how to make a Mii \n\n`!QR_name` \nDisplays the Mii QR code for a specific Mii. \n\n`!miiimage_name` \nDisplays a bigger and higher-res image for a specifc Mii.', inline=True)
    embed_help.set_thumbnail(url=rando)
    await ctx.send(embed=embed_help)


def setup(client):
    client.add_cog(help(client))

  