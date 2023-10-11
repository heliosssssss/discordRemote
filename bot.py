import discord
from discord.ext import commands
import os 

MAIN_COGS = ''

class IslamG(commands.Bot): # forked from main IslamG bot i made

    def __init__(self):
        super().__init__(
            command_prefix =".vk-", # .vk- prefix
            intents = discord.Intents.all(),
            application_id = 0, # app id
            help_command = None
        )

    async def setup_hook(self):
        for cog in MAIN_COGS:
            await self.load_extension(f'cogs.{cog}')
        await bot.tree.sync()

    async def on_ready(self):
        print('init')
        await bot.change_presence(
            status = discord.Status.do_not_disturb,
            activity = discord.Activity(type=discord.ActivityType.playing, name=f"bio") # bio here
        )

    async def getchannel(idx):
        return bot.get_channel(idx)

bot = IslamG()



@bot.command()
async def real(ctx, x):
    channel = await bot.fetch_channel(0) # channel here
    x = ctx.message.content
    y = x.replace(".vk-real", "")
    await channel.send(y)


bot.run('token') # token here
