from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Activity(name='みんなの配信', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_member_join(member):
    chid = 714384240426614786
    ch = bot.get_channel(chid)
    embed = discord.Embed(title=str(member.display_name)+'あめみん杯にようこそ！',description='あめみんが役職付与するまで待ってね',colour=discord.Colour.blue())
    embed.add_field(name='あめみん杯の詳細',value='[twitter](https://twitter.com/ameminn_/status/1264833889417064454?s=20)',inline=False)
    await ch.send(embed=embed)


@bot.command()
async def check_stream(ctx):
    await ctx.send('Checking stream')


bot.run(token)
