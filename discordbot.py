from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Activity(name='みんなの配信', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def check_stream(ctx):
    await ctx.send('Checking stream')


bot.run(token)
