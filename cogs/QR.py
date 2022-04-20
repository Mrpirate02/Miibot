import discord 
import os 
from discord.ext import commands

class QR(commands.Cog):
  def __init__(self, client):
    self.client = client 

  @commands.command()
  async def QR_Abdyy(self, ctx):
    embed_Abdyy = discord.Embed(title='QR Code for Abdyy.')
    embed_Abdyy.set_image(url='https://media.discordapp.net/attachments/760119885996097560/966366554663039026/resized-image-Promo.jpeg?width=270&height=270')
    embed_Abdyy.set_footer(text='Use !miipic_name to see a picture of a Mii.')
    await ctx.send(embed=embed_Abdyy)
      
def setup(client):
    client.add_cog(QR(client))