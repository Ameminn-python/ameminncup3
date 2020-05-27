from discord.ext import commands
import discord

class Moderation(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command
    async def opp(self,ctx,name):
        guild = self.bot.get_guild(714081984443580472)
        if ctx.author.id == 598018755066593290:
            category_id = 714421979071119453
            p_cate = guild.get_channel(category_id)
            new_ch = await p_cate.category.create_voice_channel(name=name)
            new_role = await guild.create_role(name=name)
            
