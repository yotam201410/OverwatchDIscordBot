from discord.ext import commands
from Globals import Globals

client = commands.Bot(command_prefix="!")
import discord


@client.event
async def on_ready(**kwargs):
    print("run")
    for i in client.guilds:
        if i.id == 630411122134089747:
            await i.get_channel(726068505212092426).edit(position=0)
            print("Done")


embed = discord.Embed()
print(hash(embed))

client.run(Globals.token)
