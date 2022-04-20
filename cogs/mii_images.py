import discord 
import os 
from discord.ext import commands
import os.path

# Command for pulling a 512x512 image of Mii. 


class Mii_codes(commands.Cog):
  def __init__(self, client):
    self.client = client 
    
  @commands.command()
  async def miipic_Abdyy(self, ctx):
      embed_code = discord.Embed(title='Mii Image', color=0x074AB)
      embed_code.set_image(url='https://cdn.discordapp.com/attachments/760119885996097560/966411352283422750/68747470733a2f2f-7066326d2e636f6d_4.png')
      await ctx.send(embed=embed_code)
    

  @commands.command()
  async def miipic_Ram(self, ctx):
    embed_coderam = discord.Embed(title='Full-Sized Image.', color=0x38AADE)
    embed_coderam.set_image(url='https://cdn.discordapp.com/attachments/760119885996097560/966344038712246282/68747470733a2f2f-7066326d2e636f6d_1.png')
    await ctx.send(embed=embed_coderam)

    
def setup(client):
    client.add_cog(Mii_codes(client))