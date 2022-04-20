import discord 
import os 
from discord.ext import commands
import os.path

# All Mii server related functions, for pulling Mii data.
# TODO: Fix some formatting


class Mii_Server(commands.Cog):
  def __init__(self, client):
    self.client = client 

 
  @commands.command()
  async def mii_Abdyy(self, ctx): # Abdyy
      embed_abdyy = discord.Embed(color=0x074AB) 
      embed_pic = discord.Embed(color=0x074AB)
      embed_abdyy.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      embed_abdyy.add_field(name='Name: ', value='AbdyyEee.')
      embed_abdyy.add_field(name='Gender: ', value='Male.')
      embed_abdyy.add_field(name='Favorite Color:', value='Dark blue, \nHex code: #074AB3')
      embed_abdyy.add_field(name='Skin properties. ', value='Skin tone: 2nd option (Tan)')
      embed_abdyy.add_field(name='Hair Properties: ', value='Hair Style: \nColumn 1, Row 6. \nSwapped hair.')
      embed_abdyy.add_field(name='Eyebrow Properties: ', value='Eyebrow style: \nColumn 3, Row 1 or Eyebrow number 3. \nRotate to the left by 1 \nMove 1 down. \nSmaller by 1 \nStretched thinner by 2 \nMoved apart by 2.')
      embed_abdyy.add_field(name='Eye properties: ', value='Eye Style: \nColumn 2, Row 9 or eye style number 50. . \nRotate 1 right \nMove 3 down \nStretch by 1')  
      embed_abdyy.add_field(name='Nose properties: ',  value='Default nose \nMoved 3 down \nSmaller by 2')
      embed_abdyy.add_field(name='Mouth properties:' , value='Mouth style: Column 5, Row 3 or mouth number 17 \nSmaller by 1 \nMoved 1 down \nStretched 2 down.')
      embed_abdyy.set_image(url='https://cdn.discordapp.com/attachments/760119885996097560/966368715690102904/68747470733a2f2f-7066326d2e636f6d_3.png')
      embed_abdyy.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
      embed_abdyy.set_footer(text='Based of Mii Studio/Switch Mii Maker. Works for 3DS and Wii U.')
      embed_abdyy.add_field(name='Other facial properties', value='Mole. Move 11 to the right. \n3 down. \nSmaller by 3.')
      
      await ctx.send(embed=embed_abdyy) # Keep these line at the bottom
      # await ctx.send(embed=embed_pic) removing this for now
  @commands.command()
  async def mii_Zade(self, ctx): # Zade
      embed_zade = discord.Embed(color=0x38AADE) # make sure every line begins with embed_zade. # Remember paranthesis and single quotes.
      embed_pic = discord.Embed(color=0x38AADE)
      embed_zade.set_author(name=ctx.author, icon_url=ctx.author.avatar_url) 
      embed_zade.add_field(name='Name: ', value='Zade.')
      embed_zade.add_field(name='Gender: ', value='Male.')
      embed_zade.add_field(name='Favorite Color:', value='Light blue, \nHex code: #38AADE')
      embed_zade.add_field(name='Skin properties. ', value='Skin tone: \nDefault.')
      embed_zade.add_field(name='Hair Properties: ', value='Hair Style: \nColumn 6, Row 1 or Hair style number 6 \nBlack hair.')
      embed_zade.add_field(name='Eyebrow Properties: ', value='Eyebrow Style: \nDefault. \nColored Black.')
      embed_zade.add_field(name='Eye properties: ', value='Eye style: \nColumn 5, Row 5 or Eye style number 29 \nRotate 1 left \nMove 1 up')  
      embed_zade.add_field(name='Nose properties: ', value='Nose style: \nDefault')
      embed_zade.add_field(name='Mouth properties:' , value='Mouth Style: \nColumn 4, Row 1. or Mouth style number 4 ')
      embed_zade.set_image(url='https://media.discordapp.net/attachments/760119885996097560/965703666986254426/68747470733a2f2f-7066326d2e636f6d_51.png?width=243&height=243')
      embed_zade.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
      embed_zade.set_footer(text='Based of Mii Studio/Switch Mii Maker. Works for 3DS and Wii U.')
      await ctx.send(embed=embed_zade) # Keep these line at the bottom
      await ctx.send(embed=embed_pic)

    
  @commands.command()
  async def mii_Ram(self, ctx): 
        embed_ram = discord.Embed() 
        embed_pic = discord.Embed()
        embed_ram = discord.Embed(color=0x007A31) 
        embed_pic = discord.Embed(color=0x007A31)
        embed_ram.set_author(name=ctx.author, icon_url=ctx.author.avatar_url) 
        embed_ram.add_field(name='Name: ', value='Ram.')
        embed_ram.add_field(name='Gender: ', value='Male.')
        embed_ram.add_field(name='Favorite Color:', value='Dark Green, \nHex code: #007A31')
        embed_ram.add_field(name='Skin properties. ', value='Skin tone: Lighter Pink.')
        embed_ram.add_field(name='Hair Properties: ', value='Hair Style: Column 4, Row 5')
        embed_ram.add_field(name='Eyebrow Properties: ', value='Eyebrow Style: Column 5, Row 1 or Eyebrow number 5 \nRotate 1 down. \nMove down 1')
        embed_ram.add_field(name='Eye properties: ', value='Eye style: Default.')  
        embed_ram.add_field(name='Nose properties: ', value='Nose style: \nDefault')
        embed_ram.add_field(name='Mouth properties:' , value='Mouth Number Column 5, Row 1 or Mouth Number 5 \nSmaller by 1')
        embed_ram.set_image(url='https://images-ext-2.discordapp.net/external/Fy9OnrysSzNObggNBWUR33ptU3XIuoZTWVi79CkXHAI/%3Fwidth%3D243%26height%3D243/https/media.discordapp.net/attachments/760119885996097560/965926443953557504/68747470733a2f2f-7066326d2e636f6d_48-u4nix_2qw-transformed_1_1.png?width=219&height=219')
        embed_ram.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
        embed_ram.set_footer(text='Based of Mii Studio/Switch Mii Maker. Works for 3DS and Wii U.')
        await ctx.send(embed=embed_ram) 
        await ctx.send(embed=embed_pic)

  @commands.command()
  async def mii_Aaryan(self, ctx):
      embed_aaryan = discord.Embed(color=0xD41D0F)
      embed_aaryan.set_author(name=ctx.author, icon_url=ctx.author.avatar_url) 
      embed_aaryan.add_field(name='Name:  ', value='Aaryan')
      embed_aaryan.add_field(name='Gender: ', value='Male.')
      embed_aaryan.add_field(name='Favorite Color:', value='Red, \nHex code: #D41D0F')
      embed_aaryan.add_field(name='Face properties. ', value='Skin tone: Light pink.')
      embed_aaryan.add_field(name='Hair Properties: ', value='Hair Style: Column 6, row 6 or Hair number 36 \nColored Black') 
      embed_aaryan.add_field(name='Eyebrow Properties: ', value='Default. \nColored Black.') 
      embed_aaryan.add_field(name='Eye properties: ', value='Eye style: 6th column, last row or last one.')  # Add \n before each facial movement
      embed_aaryan.add_field(name='Nose properties: ', value='Default') # Add \n before each facial movement
      embed_aaryan.add_field(name='Mouth properties:' , value='Mouth style: Row 5, column 4. \nIncrease size by 1, move upwards by 1.')
      embed_aaryan.add_field(name='Other facial properties', value='Glasses: Row 1, column 2 or glasses style 2. \nColor: Teal')
      embed_aaryan.set_image(url='https://media.discordapp.net/attachments/760119885996097560/965932133719891968/68747470733a2f2f-7066326d2e636f6d_52.png?width=243&height=243')
      embed_aaryan.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
      await ctx.send(embed=embed_aaryan)

  @commands.command()
  async def mii_Matt(self, ctx):
    embed_matt = discord.Embed(color=0xFE6E17)
    embed_matt.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed_matt.add_field(name='Name: ', value='Matt')
    embed_matt.add_field(name='Gender: ', value='Male.')
    embed_matt.add_field(name='Favorite Color:', value='Orange, \nHex code: #FE6E17')
    embed_matt.add_field(name='Skin properties. ', value='Skin tone: 1st row, 4th column or 4th skin tone. \nFace shape: 11th option. \nMakeup: Facial hair option 1.')
    embed_matt.add_field(name='Hair Properties: ', value='Hair Style: Bald. ') 
    embed_matt.add_field(name='Eyebrow Properties: ', value='Eyebrow Style: Column 5, Row 1 or Eyebrow number 5 \nMoved downwards by 4. \nRotate by 2 down. \nColored Black') 
    embed_matt.add_field(name='Eye properties: ', value='Eye style: 1st row, 6th column or eye number 38. \nMoved down by 2 \nFarther apart by 2 \nSmaller by 1.')  
    embed_matt.add_field(name='Nose properties: ', value='Nose style: 1st row, 4th column or nose number 4. \nMoved down by 2 \nSize increase by 1.') # Add \n before each facial movement
    embed_matt.add_field(name='Mouth properties:' , value='Mouth style: 2nd row, second column. \nMoved down by 2.') 
    embed_matt.add_field(name='Other facial properties', value='Facial hair: Mustache number 4. \nIncrease size by 2 \nMove down by 1. \nBeard/Goatee number 3. ')
    embed_matt.set_thumbnail(url='https://images-ext-2.discordapp.net/external/lHtmiX0tOaPw-4FdAxuYciWk-VC3uANw2CppmJiuk9A/%3Fwidth%3D140%26height%3D109/https/images-ext-2.discordapp.net/external/td2Lh5qkR0_wuAVqmAaxQ_KUuGarKjK8utLzWVBpXt0/%253Fwidth%253D175%2526height%253D136/https/media.discordapp.net/attachments/760119885996097560/964499798382243910/Mii-0.webp?width=112&height=87')
    embed_matt.set_image(url='https://media.discordapp.net/attachments/800680039272284200/966048898089091143/68747470733a2f2f-7066326d2e636f6d_53.png?width=243&height=243')
    await ctx.send(embed=embed_matt)
def setup(client):
    client.add_cog(Mii_Server(client))