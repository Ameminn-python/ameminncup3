import discord
from discord.ext import commands

class Sec(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def send(self,ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete(delay = 10.0)
        e = discord.Embed(title='紹介',description='実績紹介',colour=discord.Colour.blue())
        e.add_field(name='ルミくん',value='**現地集合** 埼玉県代表\Ncleverclan リーダー 'inline=false)
        await ctx.send(embed=e)
        
    
                  
        

